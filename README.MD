
# RLC Series Simulator

## 📌 Deskripsi Singkat
Aplikasi **GUI berbasis Python** untuk mensimulasikan rangkaian **RLC seri**.  
Pengguna dapat mengatur parameter **R**, **L**, **C**, **Vmax**, **ω (kecepatan sudut)**, dan **θv (sudut fase tegangan)**, lalu melihat kurva:

- Tegangan: `v(t)`
- Arus: `i(t)`
- Daya sesaat: `p(t)`

Aplikasi juga menampilkan informasi ringkas seperti:

- |Z|, ∠Z
- Imax, ∠I
- Beda fase (φ)
- Daya rata-rata (Pavg)
- Power factor (cos φ)

Dirancang **sederhana**, **modular**, dan **mudah dikembangkan**.

---

## 🎨 Palet Warna (UI)
- `#222831` — Background utama
- `#393E46` — Panel/Frame sekunder
- `#00ADB5` — Aksen & tombol utama
- `#EEEEEE` — Teks & area plot

---

## 📂 Struktur Proyek
``` bash
rlc_sim/
├─ README.md
├─ main.py
├─ perhitungan.py
├─ assets/
└─ screenshots/
```
---
---

## ✅ Checklist Fitur (Target)
- [ ] Input parameter: R (Ω), L (H), C (F), Vmax (V), ω (rad/s), θv (°)
- [ ] Perhitungan impedansi: `Z = R + j(ωL − 1/(ωC))`
- [ ] Phasor tegangan & arus: `V = rect(Vmax, θv)`, `I = V / Z`
- [ ] Sinyal waktu berbasis cosinus: `v(t)`, `i(t)` dengan fase masing-masing
- [ ] Daya sesaat:  `p(t) = (Vmax·Imax/2)·cos(φ) + (Vmax·Imax/2)·cos(2ωt + θv + θi)`
- [ ] Daya rata-rata: `Pavg = (Vmax·Imax/2)·cos(φ)`
- [ ] Informasi ringkas: |Z|, ∠Z, Imax, ∠I, φ, Pavg, Power Factor
- [ ] Plot `v(t)`, `i(t)`, `p(t)` dalam satu figure (3 subplot, sharex)
- [ ] Tegangan komponen (opsional): VR, VL, VC (phasor & waktu)
- [ ] Preset (opsional): Resonansi (ω₀), Induktif dominan, Kapasitif dominan
- [ ] Tema gelap konsisten (palet di atas)
- [ ] Debounce update saat slider/entry berubah

---

## 🔍 Rumus Inti (Phasor, basis cos)
- ω = 2πf,  T = 2π/ω
- Z = R + j(ωL − 1/(ωC))
- V = rect(Vmax, θv)
- I = V / Z ; Imax = |I| ; θi = ∠I
- v(t) = Vmax·cos(ωt + θv)
- i(t) = Imax·cos(ωt + θi)
- φ = θv − θi
- p(t) = (Vmax·Imax/2)·cos(φ) + (Vmax·Imax/2)·cos(2ωt + θv + θi)
- Pavg = (Vmax·Imax/2)·cos(φ)

---

## 📦 Prasyarat
- Python 3.9+ (disarankan)
- Paket:
  - `tkinter`
  - `matplotlib`
  - `numpy`
  - `math`
  - `cmath`

---

## 👤 Kredit
- **Pengembang:** Muhammad Yusuf Sintara  
- **Asisten Praktek:** Mas Farel