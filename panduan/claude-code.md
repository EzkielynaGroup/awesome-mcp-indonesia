# Memasang server MCP di Claude Code

Claude Code adalah agen coding di terminal. Server MCP ditambahkan dengan perintah `claude mcp add`. Dicek terhadap dokumentasi Claude Code pada 11 November 2026.

## Pola dasar

```bash
claude mcp add [opsi] <nama> -- <perintah> [argumen...]
```

Tanda `--` memisahkan opsi milik Claude Code (`--transport`, `--env`, `--scope`) dari perintah yang menjalankan server. Semua yang ada setelah `--` diteruskan apa adanya ke server.

## Server lokal (stdio)

Tanpa API key:

```bash
claude mcp add --transport stdio tokopedia -- npx -y @bintangtimurlangit/tokopedia-mcp
```

Server Python lewat `uvx`:

```bash
claude mcp add --transport stdio kbbi -- uvx kbbi-mcp
```

Dengan API key lewat `--env` (boleh diulang untuk beberapa variabel):

```bash
claude mcp add --env BPS_API_KEY=ganti-dengan-kunci-anda --transport stdio bps -- npx -y bps-mcp-server
```

Catatan: letakkan minimal satu opsi lain (misalnya `--transport stdio`) di antara `--env` dan nama server. Jika nama server langsung mengikuti `--env`, CLI akan membacanya sebagai pasangan `KEY=value` lain dan menolaknya.

## Server remote (HTTP)

```bash
claude mcp add --transport http bmkg https://mcp-bmkg.dhanypedia.com/mcp
```

Dengan header, misalnya token:

```bash
claude mcp add --transport http contoh https://api.example.com/mcp --header "Authorization: Bearer token-anda"
```

## Scope: di mana konfigurasi disimpan

| Scope | Berlaku untuk | Dibagi ke tim | Disimpan di |
|---|---|---|---|
| `local` (bawaan) | Proyek saat ini saja | Tidak | `~/.claude.json` |
| `project` | Proyek saat ini saja | Ya, lewat version control | `.mcp.json` di root proyek |
| `user` | Semua proyek Anda | Tidak | `~/.claude.json` |

Contoh: `claude mcp add --scope user --transport stdio kbbi -- uvx kbbi-mcp` membuat server KBBI tersedia di semua proyek. Jangan menaruh API key di `.mcp.json` yang di-commit ke Git.

## Mengelola server

```bash
claude mcp list            # daftar server
claude mcp get bps         # detail satu server
claude mcp remove bps      # hapus server
```

Di dalam sesi Claude Code, ketik `/mcp` untuk melihat status server dan login ke server remote yang memakai OAuth.

## Timeout dan keluaran besar

- Server lambat saat mulai: `MCP_TIMEOUT=10000 claude` memberi waktu 10 detik.
- Keluaran alat yang besar dibatasi; batasnya bisa diubah dengan variabel `MAX_MCP_OUTPUT_TOKENS` sebelum menjalankan Claude Code.

Masalah lain ada di [Pemecahan Masalah](pemecahan-masalah.md).

Sumber: [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp).
