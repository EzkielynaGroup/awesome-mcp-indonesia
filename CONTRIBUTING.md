# Panduan Kontribusi

Terima kasih sudah mau membantu. Daftar ini dikurasi: tujuannya memuat server MCP yang berguna untuk Indonesia dan benar-benar bisa dipakai, bukan semua repo yang menyebut "MCP".

*English: contributions are welcome. Open a pull request that adds one server in the format below and explain in the PR why it is useful in Indonesia. Descriptions are written in Indonesian; if you cannot write Indonesian, write English and a maintainer will translate it.*

## Kriteria entri

Sebuah server MCP diterima jika:

1. **Relevan untuk Indonesia.** Memakai data atau layanan Indonesia (pemerintah, statistik, cuaca, hukum, pembayaran, marketplace, logistik), mendukung bahasa Indonesia, atau dibuat khusus untuk pengguna di Indonesia.
2. **Benar-benar berfungsi.** Ada README yang menjelaskan alat (tools) dan cara memasang; ada kode yang bisa dijalankan atau endpoint remote yang merespons; repo tidak diarsipkan dan bukan sekadar kerangka kosong atau "work in progress".
3. **Lisensi jelas** untuk server yang dijalankan sendiri. Layanan remote (hosted) boleh tanpa kode sumber, asal cara akses, autentikasi, dan model biayanya dijelaskan di halaman publik.
4. **Aman secara bawaan.** Alat yang bisa memindahkan uang, menghapus data, atau menulis file harus dijelaskan di README; lebih baik lagi jika nonaktif secara bawaan atau perlu konfirmasi.
5. **Deskripsi jujur dan netral.** Satu kalimat faktual: apa yang dilakukan, perlu API key atau tidak, gratis atau berbayar. Tanpa klaim pemasaran seperti "terbaik", "termurah", "tanpa batas", atau "resmi".
6. **Status afiliasi disebut.** Server buatan komunitas untuk layanan pihak ketiga ditulis sebagai "buatan komunitas" atau "tidak berafiliasi dengan ...". Server yang disediakan pemilik layanannya sendiri boleh disebut demikian.

Tidak diterima: server yang mengambil data pribadi tanpa dasar hukum, melewati login atau CAPTCHA, menjual akses ke data curian, atau dipasarkan untuk konten tanpa pengaman.

## Format

```markdown
- [Nama](https://github.com/pemilik/repo) - Deskripsi singkat yang diawali huruf kapital dan diakhiri titik.
```

- Tambahkan entri di bagian yang paling cocok, urut abjad menurut nama di dalam bagian.
- Satu baris per entri, tanpa hard-wrap.
- Jalankan pengecek tautan sebelum membuka PR:

```bash
python3 scripts/check_links.py README.md CONTRIBUTING.md panduan/*.md
```

## Panduan pemasangan

Perbaikan panduan di folder `panduan/` juga diterima. Setiap perintah dan contoh konfigurasi harus dicek terhadap dokumentasi aplikasi terbaru; cantumkan tautan sumbernya di akhir panduan.

## Pengungkapan kepentingan

Pengelola daftar ini, Ezekiel Lieberhart, juga mengelola **Ezkielyna**, gateway API AI independen untuk developer Indonesia, dan beberapa server MCP di organisasi GitHub **EzkielynaGroup**. Agar adil:

- Server EzkielynaGroup hanya dimasukkan jika memenuhi kriteria yang sama seperti entri lain, dan ditandai jika memerlukan API key berbayar.
- Repo yang belum publik disimpan sebagai komentar HTML di README dan baru diaktifkan setelah publik.
- Usulan server lain, termasuk yang bersaing dengan proyek EzkielynaGroup, diperlakukan sama. Jika menurut Anda ada entri yang tidak netral, buka issue.

## Pemeriksaan tautan otomatis

Workflow `.github/workflows/link-check.yml` menjalankan `scripts/check_links.py` setiap Senin dan pada setiap PR yang mengubah file Markdown. Skrip hanya memakai pustaka standar Python dan token bawaan GitHub Actions (tanpa secret tambahan). `WARN` berarti situs memblokir bot atau perlu login, jadi dicek manual; `FAIL` berarti tautan mati dan entri perlu diperbaiki atau dihapus. Repo yang diarsipkan muncul sebagai `WARN` dan sebaiknya dikeluarkan dari daftar.

## Lisensi

Dengan berkontribusi, Anda setuju kontribusi Anda pada daftar dan panduan dirilis di bawah [CC0 1.0](LICENSE). Skrip di folder `scripts/` berlisensi MIT (teks lisensi ada di kepala berkas skrip).
