#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Ezekiel Lieberhart (Ezkielyna)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.
"""Tiny link checker for awesome lists. Python 3.8+, standard library only, no secrets needed.

Usage:  python3 scripts/check_links.py README.md CONTRIBUTING.md [more.md ...]

- Finds http(s) links in Markdown files, skipping anything inside HTML comments (<!-- ... -->), so entries that are
  parked in comments (for example repos that are not public yet) are not checked.
- github.com/<owner>/<repo> links are checked through the GitHub REST API when GITHUB_TOKEN is set (the token that
  GitHub Actions provides automatically is enough). Missing repos fail; archived repos are reported as warnings.
- Other links: HEAD, then GET on failure. 2xx/3xx = ok. 401/403/429/999 and timeouts = warning (many sites block
  bots), 404/410/5xx and DNS errors = failure.
- Patterns in .linkcheck-ignore (one regex per line, # for comments) are skipped.
Exit code 1 when at least one link fails.
"""
import concurrent.futures
import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; awesome-list-link-check/1.0; +https://github.com/sindresorhus/awesome)"
TIMEOUT = float(os.environ.get("LINKCHECK_TIMEOUT", "20"))
WORKERS = int(os.environ.get("LINKCHECK_WORKERS", "8"))
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
SOFT = {401, 403, 405, 406, 429, 451, 999}

LINK_RE = re.compile(r"\]\((https?://(?:[^()\s]|\([^()\s]*\))+)\)|<(https?://[^>\s]+)>|^\[[^\]]+\]:\s*(https?://\S+)", re.M)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
CODE_RE = re.compile(r"```.*?```", re.S)
GH_REPO_RE = re.compile(r"^https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)/?(?:#.*)?$")


def extract(path):
    text = open(path, encoding="utf-8").read()
    text = COMMENT_RE.sub("", text)
    text = CODE_RE.sub("", text)
    links = []
    for m in LINK_RE.finditer(text):
        url = next(g for g in m.groups() if g)
        links.append(url.rstrip(".,;"))
    return links


def load_ignore():
    pats = []
    if os.path.exists(".linkcheck-ignore"):
        for line in open(".linkcheck-ignore", encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                pats.append(re.compile(line))
    return pats


def request(url, method, headers=None):
    """Return (status, first bytes of body)."""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*", **(headers or {})})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        body = r.read(262144) if method == "GET" else b""
        return r.status, body


def check_github(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        _, body = request(url, "GET", {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"})
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "fail", "repo not found (404)"
        return "warn", f"GitHub API HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return "warn", f"GitHub API error: {e.__class__.__name__}"
    try:
        if json.loads(body).get("archived"):
            return "warn", "repo is archived"
    except ValueError:
        pass
    return "ok", "repo exists"


def check(url, hops=0):
    m = GH_REPO_RE.match(url)
    if TOKEN and m:
        return check_github(m.group(1), m.group(2))
    last = None
    for attempt in range(2):
        for method in ("HEAD", "GET"):
            try:
                status, _ = request(url, method)
                if status < 400:
                    return "ok", f"HTTP {status}"
            except urllib.error.HTTPError as e:
                # Older Python versions do not follow 308 redirects: follow them by hand.
                location = e.headers.get("Location") if e.headers else None
                if 300 <= e.code < 400 and location and hops < 5:
                    return check(urllib.parse.urljoin(url, location), hops + 1)
                last = e.code
                if e.code in (404, 410) and method == "GET":
                    return "fail", f"HTTP {e.code}"
                continue
            except (urllib.error.URLError, socket.timeout, ConnectionError, TimeoutError) as e:
                reason = getattr(e, "reason", e)
                if isinstance(reason, socket.gaierror):
                    return "fail", "DNS lookup failed"
                last = f"{reason.__class__.__name__}"
                continue
            except Exception as e:  # noqa: BLE001
                last = e.__class__.__name__
                continue
        time.sleep(2)
    if isinstance(last, int) and last in SOFT:
        return "warn", f"HTTP {last} (site blocks bots or needs login; check by hand)"
    if isinstance(last, int):
        return "fail", f"HTTP {last}"
    return "warn", f"no response ({last}); check by hand"


def main(argv):
    files = argv[1:] or ["README.md"]
    ignore = load_ignore()
    urls = []
    for f in files:
        for u in extract(f):
            if u not in urls and not any(p.search(u) for p in ignore):
                urls.append(u)
    print(f"Checking {len(urls)} unique links in {', '.join(files)}")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(check, u): u for u in urls}
        for fut in concurrent.futures.as_completed(futs):
            results[futs[fut]] = fut.result()
    counts = {"ok": 0, "warn": 0, "fail": 0}
    for u in urls:
        state, msg = results[u]
        counts[state] += 1
        if state != "ok":
            print(f"{state.upper():4}  {u}  ({msg})")
    print(f"\nok={counts['ok']} warn={counts['warn']} fail={counts['fail']}")
    return 1 if counts["fail"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
