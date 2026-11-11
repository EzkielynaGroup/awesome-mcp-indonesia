# Pemecahan masalah MCP

Masalah yang paling sering muncul saat memasang server MCP, dan cara mengatasinya.

## Server tidak muncul sama sekali

1. Mulai ulang aplikasi sepenuhnya (Quit, lalu buka lagi). Claude Desktop dan Cursor membaca konfigurasi saat mulai.
2. Cek JSON dengan validator: koma berlebih atau tanda kutip yang hilang membuat seluruh file diabaikan.
3. Path di konfigurasi harus absolut, bukan relatif.
4. Jalankan perintah server langsung di terminal, misalnya `npx -y bps-mcp-server` atau `uvx kbbi-mcp`. Jika ada error di sana, server juga gagal di aplikasi. Server stdio yang sehat biasanya diam menunggu input; tekan Ctrl+C untuk keluar.

## `npx` atau `uvx` tidak ditemukan

- Pasang [Node.js](https://nodejs.org/) LTS untuk `npx`, atau [uv](https://docs.astral.sh/uv/getting-started/installation/) untuk `uvx`, lalu mulai ulang aplikasi.
- Aplikasi desktop tidak selalu membaca PATH dari shell Anda. Jika `which npx` (macOS/Linux) atau `where npx` (Windows) menunjukkan lokasinya, tulis path lengkap itu di `command`.
- Di Windows, jika `npx` tetap tidak ditemukan, bungkus dengan `cmd /c`:

```json
{
  "mcpServers": {
    "tokopedia": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@bintangtimurlangit/tokopedia-mcp"]
    }
  }
}
```

- Di Windows, jika log Claude Desktop menyebut `${APPDATA}` dalam path, tambahkan nilai `APPDATA` yang sudah diperluas (misalnya `C:\\Users\\nama\\AppData\\Roaming\\`) ke `env` server tersebut, dan pastikan npm terpasang global.

## API key ditolak

- Pastikan nama variabel persis seperti di README server (misalnya `BPS_API_KEY`), tanpa spasi atau tanda kutip berlebih.
- Simpan kunci di `env` atau variabel lingkungan, bukan di `args`, supaya tidak tercetak di log.
- Setelah mengganti kunci, mulai ulang aplikasi atau sesi agen.

## Server gov.id lambat atau ditolak

Beberapa portal pemerintah (misalnya BMKG atau portal yang dipakai indonesia-civic-stack) hanya stabil dari IP Indonesia atau membatasi bot. Jika server berjalan di luar Indonesia (VPS luar negeri, CI), coba dari jaringan Indonesia atau pakai opsi proxy yang disediakan server tersebut.

## Alat dipanggil tetapi gagal tanpa pesan jelas

- Lihat log: Claude Desktop di `~/Library/Logs/Claude` (macOS) atau `%APPDATA%\Claude\logs` (Windows); Cursor di panel Output, pilihan **MCP Logs**; Claude Code lewat `/mcp`.
- Naikkan timeout bila server lambat saat mulai: `MCP_TIMEOUT=10000 claude` untuk Claude Code, atau `mcp.timeout` untuk OpenCode.
- Uji server secara terpisah dengan [MCP Inspector](https://github.com/modelcontextprotocol/inspector): `npx @modelcontextprotocol/inspector <perintah server>`.

## Keamanan dasar

- Pasang server hanya dari sumber yang kodenya bisa Anda baca, dan perhatikan alat yang bisa menulis file atau memindahkan uang.
- Untuk pembayaran (DOKU, Xendit), mulai dari kunci sandbox dan batasi nominal.
- Jangan commit file konfigurasi berisi API key (`.mcp.json`, `.cursor/mcp.json`, `opencode.json`) ke repositori publik.
