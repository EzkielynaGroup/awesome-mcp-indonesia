# Memasang server MCP di Claude Desktop

Panduan ini berlaku untuk Claude Desktop di macOS, Windows, dan Linux. Dicek terhadap dokumentasi Model Context Protocol pada 11 November 2026.

## Yang perlu disiapkan

- Claude Desktop versi terbaru (menu Claude, lalu **Check for Updates...**).
- Untuk server berbasis Node.js: [Node.js](https://nodejs.org/) versi LTS. Cek dengan `node --version`.
- Untuk server berbasis Python: [uv](https://docs.astral.sh/uv/getting-started/installation/), yang menyediakan perintah `uvx`. Cek dengan `uvx --version`.

## 1. Buka file konfigurasi

Buka menu **Claude** di menu bar sistem (bukan pengaturan di dalam jendela chat), pilih **Settings...**, buka tab **Developer**, lalu klik **Edit Config**. File akan dibuat jika belum ada. Lokasinya:

| Sistem | Lokasi |
|---|---|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

## 2. Tambahkan server

Semua server ada di dalam objek `mcpServers`. Nama kunci (misalnya `tokopedia`) bebas, asal unik.

Server Node.js tanpa API key:

```json
{
  "mcpServers": {
    "tokopedia": {
      "command": "npx",
      "args": ["-y", "@bintangtimurlangit/tokopedia-mcp"]
    }
  }
}
```

Server yang butuh API key: taruh kunci di `env`, jangan di `args`.

```json
{
  "mcpServers": {
    "bps": {
      "command": "npx",
      "args": ["-y", "bps-mcp-server"],
      "env": { "BPS_API_KEY": "ganti-dengan-kunci-anda" }
    }
  }
}
```

Server Python lewat `uvx`:

```json
{
  "mcpServers": {
    "kbbi": {
      "command": "uvx",
      "args": ["kbbi-mcp"]
    }
  }
}
```

Beberapa server sekaligus cukup dipisah koma di dalam `mcpServers` yang sama. Pastikan JSON valid (tanpa koma di akhir objek terakhir).

## 3. Mulai ulang Claude Desktop

Tutup Claude Desktop sepenuhnya (Quit, bukan hanya menutup jendela), lalu buka lagi. Setelah itu klik tombol **+** di kiri bawah kotak chat, arahkan ke **Connectors**, lalu **Manage connectors** untuk melihat server dan alat-alatnya. Claude akan meminta persetujuan setiap kali ingin memakai alat.

## Server remote (URL)

Untuk server yang diakses lewat URL (misalnya `https://mcp-bmkg.dhanypedia.com/mcp`), Claude Desktop menyediakan konektor kustom di pengaturan **Connectors** bila fitur itu tersedia di paket Anda. Cara lain yang berjalan di semua paket adalah menjembatani URL itu menjadi server lokal dengan [`mcp-remote`](https://github.com/punkpeye/mcp-remote):

```json
{
  "mcpServers": {
    "bmkg": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp-bmkg.dhanypedia.com/mcp"]
    }
  }
}
```

Server remote yang butuh header (misalnya `Authorization`) juga bisa lewat `mcp-remote` dengan opsi `--header`; baca README server tersebut untuk contoh yang tepat.

## Melihat log

| Sistem | Folder log |
|---|---|
| macOS | `~/Library/Logs/Claude` |
| Windows | `%APPDATA%\Claude\logs` |
| Linux | `~/.config/Claude/logs` |

File `mcp.log` berisi log koneksi umum, dan `mcp-server-NAMA.log` berisi keluaran stderr dari server bernama NAMA. Di macOS: `tail -n 20 -f ~/Library/Logs/Claude/mcp*.log`.

Masalah lain (misalnya `npx` tidak ditemukan di Windows) ada di [Pemecahan Masalah](pemecahan-masalah.md).

Sumber: [Connect to local MCP servers](https://modelcontextprotocol.io/docs/develop/connect-local-servers) di modelcontextprotocol.io.
