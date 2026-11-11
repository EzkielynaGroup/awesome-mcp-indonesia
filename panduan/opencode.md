# Memasang server MCP di OpenCode

OpenCode adalah agen coding open source di terminal. Server MCP diatur di blok `mcp` pada konfigurasi OpenCode, atau ditambahkan dengan perintah `opencode mcp add`. Dicek terhadap dokumentasi OpenCode pada 11 November 2026; format konfigurasi OpenCode pernah berubah, jadi bila contoh di bawah ditolak, cek versi Anda dan halaman sumber di akhir panduan.

## Cara cepat: perintah CLI

```bash
# server lokal (stdio): perintah server ditulis setelah --
opencode mcp add tokopedia -- npx -y @bintangtimurlangit/tokopedia-mcp

# server lokal dengan variabel lingkungan
opencode mcp add bps --env 'BPS_API_KEY={env:BPS_API_KEY}' -- npx -y bps-mcp-server

# server remote
opencode mcp add bmkg --url https://mcp-bmkg.dhanypedia.com/mcp

# untuk semua proyek, tambahkan --global
opencode mcp add kbbi --global -- uvx kbbi-mcp

opencode mcp list
```

Bawaan `opencode mcp add` menulis ke konfigurasi proyek. Beri tanda kutip tunggal pada nilai `{env:NAMA}` agar shell tidak mengubahnya; OpenCode akan membaca nilai variabel `NAMA` dari lingkungan Anda saat berjalan.

## Lewat file konfigurasi

Server lokal memakai `"type": "local"` dan `command` berupa array:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "servers": {
      "bps": {
        "type": "local",
        "command": ["npx", "-y", "bps-mcp-server"],
        "environment": {
          "BPS_API_KEY": "{env:BPS_API_KEY}"
        }
      },
      "kbbi": {
        "type": "local",
        "command": ["uvx", "kbbi-mcp"]
      }
    }
  }
}
```

Server remote memakai `"type": "remote"` dan `url`, dengan `headers` bila perlu:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "servers": {
      "bmkg": {
        "type": "remote",
        "url": "https://mcp-bmkg.dhanypedia.com/mcp"
      }
    }
  }
}
```

- Untuk mematikan server tanpa menghapusnya, tambahkan `"disabled": true`.
- Timeout diatur dalam milidetik di `mcp.timeout` (kunci `startup`, `catalog`, `execution`), dan bisa ditimpa per server.

Masalah lain ada di [Pemecahan Masalah](pemecahan-masalah.md).

Sumber: [MCP servers](https://opencode.ai/docs/mcp-servers/) di dokumentasi OpenCode.
