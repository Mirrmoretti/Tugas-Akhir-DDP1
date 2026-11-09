# CyberShield: Phone Simulator 🛡️📱
### Game Simulasi Edukasi Kesadaran Anti-Penipuan Digital (Scam Awareness)
**Tugas Akhir Mata Kuliah: Dasar-Dasar Pemrograman 1 (DDP 1)**

---

## 📌 Latar Belakang & Deskripsi Proyek
Kejahatan siber berbasis manipulasi psikologis (*social engineering*) dan rekayasa perangkat lunak jahat (*malware*) semakin marak menyasar masyarakat Indonesia. Modus seperti pengiriman file berformat **.apk** berkedok kurir paket/undangan pernikahan, pencurian kode OTP perbankan, penipuan lowongan kerja paruh waktu berbayar, hingga tautan phishing undian palsu telah merugikan ribuan korban.

**CyberShield: Phone Simulator** adalah permainan simulasi smartphone interaktif berbasis GUI (**Tkinter**) yang dirancang untuk melatih naluri dan literasi keamanan digital publik. Pemain berperan sebagai pengguna ponsel yang menerima berbagai pesan masuk dan harus menentukan tindakan terbaik dengan menganalisis tanda-tanda bahaya (*red flags*). Setiap keputusan berdampak langsung pada **Saldo Tabungan** dan **Tingkat Kewaspadaan (Awareness)** pemain.

---

## ✨ Fitur Utama
1. **Simulasi Tampilan Smartphone Modern:**
   - Status bar dinamis: Jam, baterai, sinyal 4G, saldo tabungan, dan bar kewaspadaan (*trust/awareness meter*).
   - Antarmuka ruang obrolan (*chat bubble*) dengan identitas pengirim, tag keamanan, waktu, dan pratinjau lampiran file/link.
2. **Bank Skenario Kasus Nyata (8 Kasus):**
   - **Modus Kurir Ekspedisi .APK:** File resi palsu penyadap SMS OTP.
   - **Phishing Perbankan:** CS bank palsu menuntut kode OTP pembatalan tarif.
   - **Lowongan Kerja Freelance (Job Scam):** Misi like & subscribe video berkedok deposit modal bodong.
   - **Pesan Sah / Sahabat:** Menguji apakah pemain bisa bersikap kritis tanpa menjadi paranoid berlebihan.
   - **Undangan Pernikahan .APK:** Trojan pembobol m-banking lewat undangan digital palsu.
   - **Pencatutan Identitas Teman (Impersonation):** Mengaku kerabat ganti nomor meminta transfer darurat.
   - **Hadiah & Undian Palsu:** Tautan situs phishing berkedok hadiah e-commerce.
   - **Surat Tilang ETLE Palsu .APK:** Pencatutan institusi penegak hukum (Polri).
3. **Umpan Balik Edukatif (Feedback & Red Flags):**
   - Setiap kali pemain mengambil keputusan, muncul dialog penjelasan yang membedah *tanda bahaya (red flags)* dan *tips keamanan nyata*.
4. **Sistem Evaluasi & Rapor Akhir:**
   - Menghitung gelar literasi pemain (misal: *Cyber Security Sentinel*, *Warga Digital Waspada*, atau *Korban Penipuan Digital*).
5. **Penyimpanan Skor Permanen (File I/O Leaderboard):**
   - Menyimpan 10 skor tertinggi ke file `data/highscores.json`.

---

## 💻 Penerapan Konsep Pemrograman DDP 1
Proyek ini mengimplementasikan konsep-konsep inti yang diajarkan pada mata kuliah Dasar-Dasar Pemrograman 1:

| Konsep DDP 1 | Implementasi dalam Kode |
| :--- | :--- |
| **Object-Oriented Programming (OOP)** | Pembuatan class `Choice`, `Scenario`, `GameState`, serta pewarisan (*inheritance*) class `tk.Frame` dan `tk.Tk` pada komponen antarmuka antarlayar. |
| **Modularitas & Abstraksi** | Pemisahan kode menjadi package `models`, `ui`, `screens`, dan file `config.py` agar bersih dan mudah dirawat. |
| **Struktur Data (`dict`, `list`, `tuple`)** | Pengelolaan kumpulan pilihan aksi, daftar riwayat tindakan, dan parsing JSON ke objek Python. |
| **File I/O (JSON Handling)** | Membaca berkas skenario (`data/scenarios.json`) dan membaca/menulis data peringkat (`data/highscores.json`). |
| **Kontrol Alur (Branching & Looping)** | Percabangan `if/elif/else` untuk validasi skor dan status permainan; perulangan `for` untuk merender daftar pesan chat dan tombol pilihan. |
| **Penanganan Eksepsi (`try-except`)** | Menangani error saat pembacaan file dan eksekusi antarmuka GUI. |

---

## 📂 Struktur Direktori Proyek

```text
Tugas-Akhir-DDP1/
│
├── main.py                     # Entry point utama aplikasi
├── config.py                   # Konstanta warna, font, dan konfigurasi layar HP
├── README.md                   # Dokumentasi lengkap proyek
│
├── models/                     # Modul logika bisnis (OOP)
│   ├── __init__.py
│   ├── scenario.py             # Class Scenario dan Choice
│   └── game_state.py           # Class GameState (skor, saldo, File I/O)
│
├── data/                       # Penyimpanan berkas data (File I/O)
│   ├── scenarios.json          # Dataset 8 kasus penipuan siber & pesan sah
│   └── highscores.json         # Penyimpanan leaderboard skor pemain
│
└── ui/                         # Modul antarmuka GUI (Tkinter)
    ├── __init__.py
    ├── app.py                  # Window utama & pengatur perpindahan layar
    └── screens/
        ├── __init__.py
        ├── start_screen.py     # Layar awal & registrasi nama pemain
        ├── game_screen.py      # Layar simulasi ponsel & chat interaktif
        ├── end_screen.py       # Layar rapor hasil & rangkuman edukasi
        └── leaderboard_screen.py # Layar papan peringkat skor tertinggi
```

---

## 🚀 Cara Menjalankan Game

### Opsi 1: Lewat PyCharm
1. Buka folder proyek `Tugas-Akhir-DDP1` di **PyCharm**.
2. Pastikan Python Interpreter sudah terkonfigurasi (Python 3.10+).
3. Klik kanan pada file [`main.py`](file:///c:/Users/Fatta/Desktop/Tugas-Akhir-DDP1/main.py) lalu pilih **Run 'main'**.

### Opsi 2: Lewat Terminal / Command Prompt
Buka terminal di direktori proyek dan ketik:
```bash
python main.py
```

---

## 🎮 Panduan Bermain
1. Masukkan nama kamu di halaman depan, lalu klik **Mulai Simulasi Ponsel**.
2. Di setiap kasus, baca pesan teks, nomor pengirim, serta file/link lampiran dengan seksama.
3. Pilih salah satu dari tindakan yang tersedia:
   - Waspadai file berekstensi `.apk` dan tautan website gratisan/aneh.
   - Jangan pernah membagikan kode OTP atau PIN kepada siapapun.
   - Jangan mudah tergiur tawaran kerja dengan syarat deposit uang muka.
4. Baca umpan balik (*feedback*) untuk memahami mengapa tindakanmu aman atau berbahaya.
5. Selesaikan seluruh kasus hingga akhir dan periksa gelar kewaspadaanmu di **Rapor Hasil**!
