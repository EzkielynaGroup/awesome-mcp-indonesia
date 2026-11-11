# Publish notes: awesome-mcp-indonesia

Built locally on 11 Nov 2026. Nothing pushed. Owner runs the steps below.

## GitHub

- **Description (<= 120 chars):** `Server MCP untuk Indonesia (BPS, BMKG, KBBI, hukum, QRIS, marketplace) + panduan pasang MCP berbahasa Indonesia.`
- **Homepage:** leave empty (or the repo URL).
- **Topics (14):** `awesome`, `awesome-list`, `mcp`, `mcp-server`, `mcp-servers`, `model-context-protocol`, `indonesia`, `bahasa-indonesia`, `claude-desktop`, `claude-code`, `cursor`, `opencode`, `open-data`, `ai-agents`
  (`awesome` and `awesome-list` are required by awesome-lint's `awesome-github` rule.)

```bash
cd awesome-mcp-indonesia   # the local repo folder
bash <path-to>/gh_public_check.sh .   # the org leak check; must print CLEAN
gh repo create EzkielynaGroup/awesome-mcp-indonesia --public --source . --remote origin \
  --description "Server MCP untuk Indonesia (BPS, BMKG, KBBI, hukum, QRIS, marketplace) + panduan pasang MCP berbahasa Indonesia."
git push -u origin main
gh repo edit EzkielynaGroup/awesome-mcp-indonesia --add-topic awesome,awesome-list,mcp,mcp-server,mcp-servers,model-context-protocol,indonesia,bahasa-indonesia,claude-desktop,claude-code,cursor,opencode,open-data,ai-agents
```

## Enable the parked entries (HTML comments in README.md)

EzkielynaGroup MCP servers that were not public on 11 Nov 2026 are parked in HTML comments:

- "Cuaca dan Kebencanaan": `mcp-bmkg`
- "Pembayaran": `mcp-qris`
- "Kalender, Wilayah, dan Utilitas" (whole section + its ToC line, also commented): `mcp-hari-libur-indonesia`, `mcp-rupiah`, `mcp-wilayah-indonesia`
- "AI dan Media": `ai-model-status-mcp`, `ezkielyna-audio-mcp`, `ezkielyna-mcp`
- "Daftar Terkait": `awesome-ai-indonesia`

When a repo is public, move its line out of the comment (keep alphabetical order), replace the `mcp-rupiah` TODO with the final
description, and run `python3 scripts/check_links.py README.md CONTRIBUTING.md panduan/*.md`.
The parked descriptions were taken from each repo's README/PUBLISH.md on 11 Nov 2026; re-read them at publish time.

## After publishing

1. `npx awesome-lint` reports only `awesome-github` before publishing (needs a GitHub remote); it passes once the repo exists with the topics above.
2. The `Link check` workflow runs weekly and opens an issue when a link dies. No secrets needed.
3. sindresorhus/awesome: same constraints as the AI list (30 days, human curation, no AI-generated lists). Earliest ~12 Dec 2026.
4. Other places to link it from (owner decides): the EzkielynaGroup org profile, `tips-ai-indonesia`, and the README of each
   EzkielynaGroup MCP server.

## Things to re-check before publishing

- Community servers change fast. Re-run the link check and glance at the last commit date of each repo; drop anything archived.
- Guides in `panduan/` were checked against the Claude Code, Cursor, OpenCode and modelcontextprotocol.io docs on 11 Nov 2026.
  OpenCode changed its config format (now `mcp.servers`); re-check if OpenCode ships a new major version.
