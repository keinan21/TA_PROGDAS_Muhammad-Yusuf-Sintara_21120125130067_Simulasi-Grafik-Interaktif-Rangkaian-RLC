
# Visualisasi Grafik Sinusoidal Tegangan, Arus, dan Daya RLC Seri

Deskripsi Singkat
-----------------
Aplikasi GUI berbasis Python untuk mensimulasikan rangkaian **RLC seri** pada mode sinus steady‑state
(phasor). Pengguna dapat mengatur parameter **R**, **L**, **C**, **Vmax** (puncak), **ω** (kecepatan sudut),
dan **θv** (sudut fase tegangan), lalu menampilkan kurva **v(t)**, **i(t)**, dan **p(t)**. Panel informasi
menyajikan nilai ringkas seperti **|Z|, ∠Z, Imax, ∠I, φ, Pavg, cos φ (power factor)**. Proyek ini
disusun modular: engine perhitungan terpisah dari layer plotting dan GUI.

Tools & Alat yang Digunakan
---------------------------
• **VS Code** — IDE utama untuk pengembangan kode Python & integrasi modul.  
• **Gluonix Designer** — desain UI drag‑and‑drop (membuat layout, tombol, frame, image).  
• **Canva** — pembuatan/penyusunan aset gambar (ikon dan materi).  
• **Python Toolkit** — `tkinter`, `matplotlib`, `numpy`, `math`, `cmath` untuk GUI, plotting, dan numerik.

Palet Warna (UI)
----------------
• `#222831`  → Background utama  
• `#393E46`  → Panel/Frame sekunder  
• `#00ADB5`  → Aksen & tombol utama  
• `#EEEEEE`  → Teks & area plot

Struktur Proyek (Ringkas)
-------------------------
```bash
Tugas Akhir/\
├─ GUI_TA.py                # Entrypoint GUI (hasil desain Gluonix + logic binding)\
├─ perhitungan.py           # Engine phasor: impedansi, arus, fase, daya, generator sinyal waktu\
├─ plot.py                  # Fungsi rendering ke PNG (v/i/p), opsi subplots/twin axis\
├─ assets/                  # Ikon/gambar: omega.ico, omega.png, hasilGrafik.png, rumus*.png, animasi/*.gif\
├─ Gluonix/ , Nucleon/     # Library runtime dari Gluonix Designer (widget N_*, Runner, dll.)\
├─ Data/                    # Basis data desain (NGD.dll) & cache File/\
└─ README.md                # Dokumen ini\
```
Fitur & Progres Akhir
---------------------
```
[x] Input parameter: **R (Ω), L (H), C (F), Vmax (V), ω (rad/s), θv (°)**  
[x] Perhitungan impedansi: `Z = R + j(ωL − 1/(ωC))`  
[x] Phasor tegangan & arus: `V = rect(Vmax, θv)`, `I = V / Z` → `Imax = |I|`, `θi = ∠I`  
[x] Sinyal waktu (basis cos): `v(t) = Vmax·cos(ωt + θv)` dan `i(t) = Imax·cos(ωt + θi)`  
[x] Daya sesaat:
    `p(t) = (Vmax·Imax/2)·cos(φ) + (Vmax·Imax/2)·cos(2ωt + θv + θi)` dengan `φ = θv − θi`  
[x] Daya rata-rata: `Pavg = (Vmax·Imax/2)·cos(φ)`  
[x] Panel informasi: **|Z|, ∠Z, Imax, ∠I, φ, Pavg, cos φ**  
[x] Plot **v(t)**, **i(t)**, **p(t)**: opsi **3 subplot (sharex)** atau **twin y‑axis**  
[x] Popup **Materi** (Gluonix): konten teori & gambar rumus (LaTeX→PNG)  
[x] Tema gelap konsisten (palet di atas); legend & grid rapi  
[x] Integrasi gambar ke widget **Image.Set(path)** (hasil render Matplotlib → PNG)
```
Rumus Inti (Phasor, basis cos)
------------------------------
• `ω = 2πf`,  `T = 2π/ω`  
• `Z = R + j(ωL − 1/(ωC))`  
• `V = rect(Vmax, θv)`  
• `I = V / Z` ; `Imax = |I|` ; `θi = ∠I`  
• `v(t) = Vmax·cos(ωt + θv)`  
• `i(t) = Imax·cos(ωt + θi)`  
• `φ = θv − θi`  
• `p(t) = (Vmax·Imax/2)·cos(φ) + (Vmax·Imax/2)·cos(2ωt + θv + θi)`  
• `Pavg = (Vmax·Imax/2)·cos(φ)`  


Tentang Materi (Konten & Komponen)
----------------------------------
• **Apa itu RLC Seri** — kombinasi **Resistor (R)**, **Induktor (L)**, **Kapasitor (C)** seri; digunakan pada filter, resonansi, dan kontrol daya AC.  
• **Fase Tegangan vs Arus** — induktor membuat arus **tertundanya** (lagging, v mendahului i), kapasitor membuat arus **mendahului** (leading).  
• **Efek L & C** — `X_L = ωL` bertambah saat f naik; `X_C = 1/(ωC)` menurun saat f naik.  
• **Popup Materi (Gluonix)** — komponen: `FrameMateri`, `TextMateri` (penjelasan),
  `GambarRumus` (Image), `ButtonTutup` (Bind → Close).  
• **Rumus ditampilkan sebagai gambar** — convert LaTeX→PNG, lalu `Image.Set(<path>)`.


Instalasi & Menjalankan
-----------------------
1) Siapkan Python 3.10+ dan virtual environment (opsional).  
2) Instal dependency:
   • `pip install matplotlib numpy`  
   • `tkinter` biasanya sudah tersedia di CPython (Linux perlu paket sistem TK).  
3) Jalankan aplikasi:
   • `python GUI_TA.py`

Penggunaan
----------
• Isi parameter R, L, C, Vmax, ω, θv di panel input.  
• Klik **Hitung/Run** untuk menampilkan grafik dan ringkasan.  
• Klik **Materi** untuk membuka jendela popup teori & rumus (gambar LaTeX).  
• Grafik disimpan otomatis (mis. `assets/hasilGrafik.png`) dan dimuat ke widget image.

Catatan Teknis & Batasan
------------------------
• Semua besaran tegangan/arus memakai **nilai puncak (peak)**, bukan RMS.  
• Dekat **resonansi** (`ω ≈ ω₀`), impedansi total mengecil → arus sangat besar; sesuaikan skala plot.  
• Runtime **Gluonix/Nucleon** menggunakan basis Tk; beberapa modul (mis. `NGD.dll`) optimal di Windows.  
• Untuk interaktivitas Matplotlib (toolbar), gunakan embed canvas; versi awal memakai render ke PNG lalu `Image.Set(path)` untuk stabilitas.

Roadmap (Selesai)
-----------------
• Engine phasor & generator sinyal waktu — **DONE**  
• Plot v/i/p & panel ringkas — **DONE**  
• Popup Materi + aset LaTeX→PNG — **DONE**  
• Tema gelap & konsistensi gaya — **DONE**  
• Debounce & preset (resonansi) — **NEXT (opsional)**

Kontribusi (kalo mau)
----------
Pull request dipersilakan untuk:
• Penambahan mode **Bode plot** (|I| & ∠I vs frekuensi).  
• Preset **Induktif/Kapasitif** dan parser unit (mH, μF, kΩ).  
• Export data CSV dan seting profil eksperimen.

Kredit
------
• **Pengembang:** Muhammad Yusuf Sintara  
• **Tools:** VS Code, Gluonix Designer, Canva  
• **Terima kasih:** semua yang membantu dalam debugging, binding event, dan integrasi gambar di Gluonix.
