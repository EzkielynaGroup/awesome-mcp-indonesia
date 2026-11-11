# Awesome MCP Indonesia [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Server Model Context Protocol (MCP) untuk layanan, data, bahasa, dan pembayaran di Indonesia.

Daftar kurasi server MCP yang berguna untuk developer dan UMKM Indonesia: data pemerintah dan statistik, cuaca dan gempa BMKG, KBBI, hukum, pembayaran, dan marketplace lokal, ditambah panduan berbahasa Indonesia untuk memasang MCP di Claude Desktop, Claude Code, Cursor, dan OpenCode. Setiap repo dicek manual (README, lisensi, commit terbaru) dan semua tautan dicek ulang tiap minggu oleh skrip.

**English summary:** A curated list of MCP (Model Context Protocol) servers that are useful in Indonesia: government open data and statistics (BPS, BMKG, regional open data portals), the KBBI dictionary, Indonesian law, local payment gateways (DOKU, Xendit, Midtrans docs), marketplaces (Tokopedia, Shopee), plus step-by-step guides in Indonesian for installing MCP servers in Claude Desktop, Claude Code, Cursor and OpenCode. Every repository was checked by hand (README, license, recent commits) and links are re-checked weekly.

## Contents

- [Panduan Pemasangan](#panduan-pemasangan)
- [Data Pemerintah dan Statistik](#data-pemerintah-dan-statistik)
- [Cuaca dan Kebencanaan](#cuaca-dan-kebencanaan)
- [Bahasa Indonesia](#bahasa-indonesia)
- [Hukum dan Regulasi](#hukum-dan-regulasi)
- [Pembayaran](#pembayaran)
- [Marketplace dan E-commerce](#marketplace-dan-e-commerce)
- [Kalender, Wilayah, dan Utilitas](#kalender-wilayah-dan-utilitas)
- [AI dan Media](#ai-dan-media)
- [Registri dan Direktori](#registri-dan-direktori)
- [Daftar Terkait](#daftar-terkait)
- [FAQ](#faq)


## Panduan Pemasangan

Panduan langkah demi langkah berbahasa Indonesia, dicek terhadap dokumentasi tiap aplikasi.

| Panduan                                           | Isi                                                                                                          |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [Claude Desktop](panduan/claude-desktop.md)       | Server lokal lewat `claude_desktop_config.json`, server remote lewat konektor atau `mcp-remote`, lokasi log. |
| [Claude Code](panduan/claude-code.md)             | Perintah `claude mcp add`, variabel lingkungan, header, scope, dan timeout.                                  |
| [Cursor](panduan/cursor.md)                       | File `mcp.json` global atau per proyek untuk server lokal dan remote.                                        |
| [OpenCode](panduan/opencode.md)                   | Blok `mcp` di konfigurasi OpenCode dan perintah `opencode mcp add`.                                          |
| [Pemecahan Masalah](panduan/pemecahan-masalah.md) | `npx` di Windows, `uvx`, API key, portal gov.id, log, dan keamanan dasar.                                    |

## Data Pemerintah dan Statistik

- [API Indonesia](https://apiindonesia.id) - Server MCP remote untuk wilayah, kode pos, hari libur, jadwal salat, KBBI, dan gempa BMKG, perlu API key dengan model kredit berbayar dan bonus kredit awal.
- [BPS MCP Server](https://github.com/setiapam/bps-mcp-server) - Puluhan alat untuk endpoint Web API BPS dan pencarian AllStats, jalan dengan `npx`, perlu kunci Web API BPS.
- [DML BPS MCP](https://github.com/digimetalab/dml-bps-mcp) - Server MCP BPS lain dengan alat tambahan untuk SIMDASI, SDGs, serta klasifikasi KBLI dan KBKI.
- [idn-econ-mcp](https://github.com/anYoneo/idn-econ-mcp) - Data ekonomi Indonesia dan ASEAN (inflasi, PDB, kurs terhadap Rupiah) dari World Bank, IMF, dan ECB tanpa API key.
- [indonesia-civic-stack](https://github.com/suryast/indonesia-civic-stack) - SDK Python dan server MCP untuk belasan sumber data publik seperti BPOM, BPJPH, AHU, OJK, dan BMKG, sebagian portal hanya bisa diakses dari IP Indonesia.
- [MCP Satu Data Aceh](https://github.com/abdrhmn09/MCP_SatuDataAceh) - Server MCP untuk katalog Portal Satu Data Aceh dan Web API BPS, tersedia juga versi hosted.
- [mcp-indonesia](https://github.com/wirawibowo/mcp-indonesia) - Satu server untuk wilayah, kode pos, BMKG, kurs termasuk JISDOR, validasi format NIK dan NPWP, hari libur, jadwal salat, dan cek entitas OJK.

## Cuaca dan Kebencanaan

- [bmkg-api](https://github.com/dhanyyudi/bmkg-api) - Server MCP Python (`uvx bmkg-api-mcp`) dan server remote untuk prakiraan cuaca desa, gempa, peringatan dini, dan pencarian wilayah dari data BMKG.
- [mcp-bmkg](https://github.com/EzkielynaGroup/mcp-bmkg) - Server MCP satu file tanpa API key untuk gempa terkini dan prakiraan cuaca tingkat desa dari data terbuka BMKG.

## Bahasa Indonesia

- [kbbi-mcp](https://github.com/gaato/kbbi-mcp) - Cari arti kata di KBBI lewat `uvx kbbi-mcp`, klien buatan komunitas yang tidak berafiliasi dengan Badan Bahasa.
- [kbbi-mcp-server](https://github.com/mlengse/kbbi-mcp-server) - Kamus KBBI, pemenggalan suku kata, dan stemmer bahasa Indonesia, dokumentasi berbahasa Indonesia, lisensi GPL-3.0.

## Hukum dan Regulasi

- [Indonesia Law (Pipeworx)](https://github.com/pipeworx-io/mcp-indonesia-law) - Cari UU, Perpu, PP, Perpres, dan putusan uji materi MK dari JDIH Setneg dan DPR lewat server remote, 50 panggilan per hari tanpa akun.
- [Indonesia Regulatory MCP](https://github.com/IndoTender/indonesia-regulatory-mcp) - Server remote IndoTender untuk registrasi produk BPOM, merek DJKI, dan pendaftaran PSE Komdigi, masuk dengan akun Google.

## Pembayaran

- [DOKU MCP Server](https://developers.doku.com/accept-payments/doku-mcp-server) - Server MCP remote dari DOKU dengan 30+ alat untuk tautan pembayaran, QRIS, virtual account, e-wallet, dan status transaksi, tersedia sandbox.
- [mcp-midtrans](https://github.com/rissets/mcp-midtrans) - Server MCP berisi dokumentasi Midtrans (API, metode pembayaran, contoh kode) untuk membantu integrasi, tidak memanggil API Midtrans.
- [mcp-qris](https://github.com/EzkielynaGroup/mcp-qris) - Server MCP offline untuk membaca, memvalidasi, menambah nominal, dan merender payload QRIS sebagai SVG, tanpa memindahkan uang.
- [xendit-mcp](https://github.com/mrslbt/xendit-mcp) - Server MCP buatan komunitas untuk invoice, payout, saldo, dan transaksi Xendit, fitur yang memindahkan uang nonaktif secara bawaan.

## Marketplace dan E-commerce

- [shopee-indonesia-mcp](https://github.com/WilliamAxelC/shopee-indonesia-mcp) - Server MCP dan REST buatan komunitas untuk produk, harga, ulasan, dan flash sale di shopee.co.id, tidak berafiliasi dengan Shopee.
- [tokopedia-mcp](https://github.com/bintangtimurlangit/tokopedia-mcp) - Server MCP tanpa login untuk mencari produk, filter, ulasan, dan toko di Tokopedia, buatan komunitas dan tunduk pada ketentuan layanan Tokopedia.

## Kalender, Wilayah, dan Utilitas

- [mcp-hari-libur-indonesia](https://github.com/EzkielynaGroup/mcp-hari-libur-indonesia) - Server MCP offline untuk hari libur nasional dan cuti bersama sesuai SKB 3 Menteri, plus hitung hari kerja.
- [mcp-rupiah](https://github.com/EzkielynaGroup/mcp-rupiah) - Server MCP offline untuk terbilang, format dan baca nominal Rupiah, serta kalkulator PPN sesuai aturan 2025+.
- [mcp-wilayah-indonesia](https://github.com/EzkielynaGroup/mcp-wilayah-indonesia) - Server MCP offline untuk kode wilayah Kemendagri dari provinsi sampai desa, tahan salah ketik, dengan kode adm4 BMKG.

## AI dan Media

- [AI Model Status MCP](https://github.com/EzkielynaGroup/ai-model-status-mcp) - Server MCP tanpa API key untuk melihat model AI mana yang aktif, cepat, populer, atau berharga rendah dari data publik.
- [Ezkielyna Audio MCP](https://github.com/EzkielynaGroup/ezkielyna-audio-mcp) - Server MCP untuk teks ke suara dan transkripsi file audio lokal termasuk bahasa Indonesia lewat API Ezkielyna.
- [Ezkielyna Image MCP](https://github.com/EzkielynaGroup/ezkielyna-image-mcp) - Server MCP satu file untuk membuat dan mengedit gambar dari file lokal lewat API Ezkielyna, perlu API key berbayar.
- [Ezkielyna MCP](https://github.com/EzkielynaGroup/ezkielyna-mcp) - Server MCP untuk meminta pendapat kedua dari model AI lain, membandingkan jawaban, dan pencarian web lewat API Ezkielyna.

## Registri dan Direktori

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - Daftar kurasi komunitas untuk server MCP dari seluruh dunia.
- [Glama MCP Servers](https://glama.ai/mcp/servers) - Direktori server MCP open source dengan pencarian dan hasil inspeksi.
- [MCP Registry](https://registry.modelcontextprotocol.io) - Registri server MCP yang dikelola proyek Model Context Protocol, bisa dicari dengan kata kunci seperti `indonesia`.
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - Server referensi dan contoh dari proyek Model Context Protocol.
- [Model Context Protocol](https://modelcontextprotocol.io) - Spesifikasi dan dokumentasi protokol MCP.

## Daftar Terkait

- [Indonesia Government APIs](https://github.com/suryast/indonesia-gov-apis) - Katalog sumber data dan API pemerintah Indonesia beserta catatan akses.
- [Awesome AI Indonesia](https://github.com/EzkielynaGroup/awesome-ai-indonesia#readme) - Sumber daya AI untuk developer dan UMKM Indonesia: model, dataset, regulasi, dan akses API.

## FAQ

**Apa itu MCP?** MCP (Model Context Protocol) adalah standar terbuka agar asisten AI seperti Claude, Cursor, atau OpenCode bisa memanggil alat dan data dari luar, misalnya cek gempa terkini atau mencari data BPS. Server MCP adalah program kecil yang menyediakan alat-alat itu.

**Bagaimana cara memasang server MCP di Claude Desktop?** Buka Settings, tab Developer, klik Edit Config, lalu tambahkan server di dalam `mcpServers` dan mulai ulang Claude Desktop sepenuhnya. Langkah lengkap dengan contoh ada di panduan Claude Desktop pada bagian Panduan Pemasangan.

**Apa beda server MCP lokal dan remote?** Server lokal (stdio) berjalan di komputer Anda lewat perintah seperti `npx` atau `uvx`, sedangkan server remote berjalan di internet dan diakses lewat URL. Server lokal tidak mengirim data ke pihak ketiga kecuali alatnya memang memanggil API luar.

**Apakah ada server MCP untuk pembayaran QRIS di Indonesia?** DOKU menyediakan server MCP sendiri yang bisa membuat pembayaran QRIS dan virtual account, dan ada server komunitas untuk Xendit. Uji dulu di mode sandbox dan jangan beri asisten AI akses produksi tanpa batasan.

**Apakah server MCP aman dipakai?** Server MCP berjalan dengan izin akun Anda, jadi pasang hanya dari sumber yang kodenya bisa dibaca, simpan API key di variabel lingkungan, dan setujui tiap pemanggilan alat secara sadar. Daftar ini mencantumkan lisensi dan status komunitas tiap entri, tetapi tidak mengaudit keamanannya.

**Apakah server MCP di daftar ini gratis?** Sebagian besar server open source gratis dijalankan, tetapi beberapa butuh API key layanan asalnya (misalnya BPS, Xendit, DOKU) dan server remote tertentu memakai kuota atau kredit berbayar. Model biayanya disebut di deskripsi tiap entri.

## Contributing

Kontribusi sangat diterima. Baca [panduan kontribusi](CONTRIBUTING.md) untuk kriteria entri, format, dan cara mengusulkan server MCP baru.

## Footnotes

- Semua repo dan tautan dicek pada 11 November 2026 (README, lisensi, dan aktivitas commit) dan tautan dicek ulang tiap minggu oleh skrip di folder `scripts/`.
- Pengungkapan: pengelola daftar ini, Ezekiel Lieberhart, juga mengelola Ezkielyna, gateway API AI independen, dan beberapa server MCP di organisasi EzkielynaGroup. Server tersebut hanya dicantumkan jika memenuhi kriteria yang sama dengan entri lain.
- Server buatan komunitas untuk layanan pihak ketiga (misalnya Xendit, Tokopedia, Shopee, KBBI) tidak berafiliasi dengan pemilik layanan tersebut. Patuhi ketentuan layanan masing-masing.
