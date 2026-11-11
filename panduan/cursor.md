# Memasang server MCP di Cursor

Cursor membaca server MCP dari file `mcp.json`. Dicek terhadap dokumentasi Cursor pada 11 November 2026.

## Lokasi file

| Berlaku untuk | Lokasi |
|---|---|
| Satu proyek | `.cursor/mcp.json` di folder proyek |
| Semua proyek | `~/.cursor/mcp.json` di folder home |

## Server lokal (stdio)

```json
{
  "mcpServers": {
    "tokopedia": {
      "command": "npx",
      "args": ["-y", "@bintangtimurlangit/tokopedia-mcp"]
    },
    "bps": {
      "command": "npx",
      "args": ["-y", "bps-mcp-server"],
      "env": { "BPS_API_KEY": "ganti-dengan-kunci-anda" }
    },
    "kbbi": {
      "command": "uvx",
      "args": ["kbbi-mcp"]
    }
  }
}
```

- `command` wajib dan harus ada di PATH sistem atau ditulis dengan path lengkap.
- `args` dan `env` opsional.

## Server remote (URL)

```json
{
  "mcpServers": {
    "bmkg": {
      "url": "https://mcp-bmkg.dhanypedia.com/mcp"
    },
    "contoh-dengan-header": {
      "url": "https://api.example.com/mcp",
      "headers": { "Authorization": "Bearer token-anda" }
    }
  }
}
```

## Mengaktifkan dan memakai

- Buka **Customize** di sidebar Cursor, cari servernya, lalu nyalakan atau matikan dengan toggle. Server yang dimatikan tidak dimuat.
- Agen Cursor memakai alat MCP yang relevan secara otomatis; Anda juga bisa menyebut nama alatnya di chat.
- Secara bawaan Cursor meminta persetujuan sebelum memakai alat MCP. Klik panah di samping nama alat untuk melihat argumennya.
- Jika server gagal, buka panel **Output** (Cmd+Shift+U di macOS, Ctrl+Shift+U di Windows/Linux) dan pilih **MCP Logs**.

Jangan commit `.cursor/mcp.json` yang berisi API key ke repositori publik.

Masalah lain ada di [Pemecahan Masalah](pemecahan-masalah.md).

Sumber: [Model Context Protocol (MCP)](https://cursor.com/docs/mcp) di dokumentasi Cursor.
