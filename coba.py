
# app_rlc_tk.py
import os
import math
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from PIL import Image, ImageTk

# Modulmu yang sudah ada
from plot import gambarGrafik


ASSET_GRAFIK = "assets/hasilGrafik.png"   # path output gambar dari gambarGrafik()
ASSET_MATERI_IMG = "assets/materi.png"    # opsional: jika punya gambar materi


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Visualisasi Grafik RLC Seri")
        self.geometry("1000x600")
        self.configure(bg="#0f1b1f")  # tema gelap ringan

        # Variabel untuk image agar tidak kena garbage collector
        self._img_obj = None

        # ===== Layout utama: kiri (input) dan kanan (grafik + hasil) =====
        self.columnconfigure(0, weight=0)  # kiri fixed
        self.columnconfigure(1, weight=1)  # kanan fleksibel
        self.rowconfigure(0, weight=1)

        self._build_left_panel()
        self._build_right_panel()

        # Pesan awal
        self.text_hasil.insert(tk.END,
            "Silakan masukkan nilai R, L, C, Vmax, ω, dan sudut V untuk "
            "menghitung parameter RLC seri dan menampilkan grafiknya.\n"
        )

    # ---------------------------------------------------------------------
    # Panel kiri: judul + form input + tombol
    # ---------------------------------------------------------------------
    def _build_left_panel(self):
        left = ttk.Frame(self, padding=12)
        left.grid(row=0, column=0, sticky="ns")
        for i in range(12):
            left.rowconfigure(i, weight=0)
        left.rowconfigure(99, weight=1)  # spacer

        # Judul
        lbl_title = ttk.Label(
            left,
            text="Visualisasi Grafik RLC Seri\nby Muhammad Yusuf Sintara",
            anchor="center"
        )
        lbl_title.grid(row=0, column=0, sticky="ew", pady=(0, 8))

        # Form
        self.entry_R = self._make_labeled_entry(left, "Resistor (Ω)", row=1)
        self.entry_C = self._make_labeled_entry(left, "Kapasitor (F)", row=2)
        self.entry_L = self._make_labeled_entry(left, "Induktor (H)", row=3)
        self.entry_w = self._make_labeled_entry(left, "Kec.Sudut ω (rad/s)", row=4)
        self.entry_sudutV = self._make_labeled_entry(left, "Sudut V (°)", row=5)
        self.entry_Vm = self._make_labeled_entry(left, "Vmax (Volt)", row=6)

        # Tombol run
        btn_run = ttk.Button(left, text="Buat Grafik", command=self.tekan_run)
        btn_run.grid(row=7, column=0, sticky="ew", pady=(12, 6))

        # Tombol materi
        btn_materi = ttk.Button(left, text="Masih Bingung? Pelajari di sini", command=self.munculkan_materi)
        btn_materi.grid(row=8, column=0, sticky="ew")

        # Spacer
        ttk.Frame(left).grid(row=99, column=0, sticky="ns")

    def _make_labeled_entry(self, parent, label, row):
        frm = ttk.Frame(parent)
        frm.grid(row=row, column=0, sticky="ew", pady=4)
        ttk.Label(frm, text=label, width=20).pack(side="left")
        ent = ttk.Entry(frm, width=20)
        ent.pack(side="left", padx=6)
        return ent

    # ---------------------------------------------------------------------
    # Panel kanan: area gambar + area hasil teks
    # ---------------------------------------------------------------------
    def _build_right_panel(self):
        right = ttk.Frame(self, padding=12)
        right.grid(row=0, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(0, weight=3)
        right.rowconfigure(1, weight=2)

        # Area gambar (label kosong dulu)
        self.lbl_gambar = ttk.Label(right, text="hasil Grafik akan muncul di sini", anchor="center")
        self.lbl_gambar = ttk.Label(right, text="hasil Grafik akan muncul di sini", anchor="center")
        self.lbl_gambar.grid(row=0, column=0, sticky="nsew", pady=(0, 8))

        # Area hasil teks (ScrolledText)
        self.text_hasil = scrolledtext.ScrolledText(
            right, wrap="word", height=12
        )
        self.text_hasil.grid(row=1, column=0, sticky="nsew")

    # ---------------------------------------------------------------------
    # Validasi dan eksekusi perhitungan
    # ---------------------------------------------------------------------
    def cek_float(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False

    def tekan_run(self):
        # Ambil nilai dari entry
        R = self.entry_R.get().strip()
        L = self.entry_L.get().strip()
        C = self.entry_C.get().strip()
        Vm = self.entry_Vm.get().strip()        # Vmax
        w = self.entry_w.get().strip()          # omega
        sudutV = self.entry_sudutV.get().strip()  # derajat

        if not all([R, L, C, Vm, w, sudutV]):
            self._set_info("Error: Semua input harus diisi.")
            return

        if not all(map(self.cek_float, [R, L, C, Vm, w, sudutV])):
            self._set_info("Error: Semua input harus berupa angka.")
            return

        R = float(R); L = float(L); C = float(C)
        Vm = float(Vm); w = float(w); sudutV = float(sudutV)

        # Validasi fisik
        if w <= 0:
            self._set_info("Error: ω harus > 0 (rad/s).")
            return
        if C <= 0 or L < 0 or R < 0:
            self._set_info("Error: R, L, C harus bernilai fisik (R≥0, L≥0, C>0).")
            return

        try:
            # Bangkitkan grafik via modulmu dan simpan hasil PNG
            obj = gambarGrafik(R, L, C, Vm, w, sudutV)

            # Tampilkan PNG jika ada
            if os.path.exists(ASSET_GRAFIK):
                self._show_image(ASSET_GRAFIK)
            else:
                self._set_info("Peringatan: File grafik tidak ditemukan. Pastikan plot.gambarGrafik menyimpan ke assets/hasilGrafik.png")

            # Ambil hasil numerik & tampilkan
            I, Im, derajatI = obj.getArus()
            Z, Zm, derajatZ = obj.getImpedansi()
            V, Vm2, derajatV2 = obj.getTegangan()  # Vm2/derajatV2 dari obj (boleh berbeda dari input)

            # Rumus daya sesaat P(t) = P_avg + (Vm*Im/2) cos(2wt + (θv + θi))
            P_avg = obj.getDayaRerata()
            T = obj.getPeriode()

            out = (
                f"Hasil Perhitungan RLC Seri:\n"
                f"Resistor (R): {R:.2f} Ω\n"
                f"Induktor (L): {L:.2f} H\n"
                f"Kapasitor (C): {C:.6g} F\n"
                f"V(t) = {Vm2:.2f} ∠ {derajatV2:.2f}° V\n"
                f"I(t) = {Im:.2f} ∠ {derajatI:.2f}° A\n"
                f"Impedansi (Z): {Zm:.2f} ∠ {derajatZ:.2f}° Ω\n"
                f"Kecepatan Sudut (ω): {w:.6g} rad/s\n"
                f"Daya Rata-rata (P): {P_avg:.2f} W\n"
                f"Periode (T): {T:.4f} s\n"
                f"P(t) = {P_avg:.2f} + {round((Vm2 * Im) / 2, 2)} cos(2 * {w:.2f} * t + ({derajatV2:.2f} + {derajatI:.2f})) W\n"
            )
            self._set_info(out, replace=True)

        except Exception as e:
            messagebox.showerror("Kesalahan", f"Gagal menghasilkan grafik: {e}")

    # ---------------------------------------------------------------------
    # Tampilkan materi (popup)
    # ---------------------------------------------------------------------
    def munculkan_materi(self):
        pop = tk.Toplevel(self)
        pop.title("Materi")
        pop.geometry("720x800")

        # Jika kamu punya gambar materi (PNG), tampilkan gambar.
        if os.path.exists(ASSET_MATERI_IMG):
            frm = ttk.Frame(pop, padding=8)
            frm.pack(fill="both", expand=True)
            canvas = tk.Canvas(frm)
            canvas.pack(fill="both", expand=True)
            img = Image.open(ASSET_MATERI_IMG)
            self._materi_img = ImageTk.PhotoImage(img)  # simpan ref
            canvas.create_image(10, 10, image=self._materi_img, anchor="nw")
        else:
            # Fallback: teks materi ringkas
            txt = scrolledtext.ScrolledText(pop, wrap="word")
            txt.pack(fill="both", expand=True)
            txt.insert(tk.END, self._materi_text())

    # ---------------------------------------------------------------------
    # Util: set info teks & tampilkan gambar
    # ---------------------------------------------------------------------
    def _set_info(self, s: str, replace=False):
        if replace:
            self.text_hasil.delete("1.0", tk.END)
        self.text_hasil.insert(tk.END, s + ("\n" if not s.endswith("\n") else ""))

    def _show_image(self, path: str):
        img = Image.open(path)
        # Optional: sesuaikan ukuran agar pas panel kanan
        img = img.resize((700, 320), Image.LANCZOS)
        self._img_obj = ImageTk.PhotoImage(img)
        self.lbl_gambar.configure(image=self._img_obj, text="")

    def _materi_text(self) -> str:
        return (
            "Rangkaian RLC Seri — rangkuman materi\n\n"
            "1. Apa itu RLC Seri?\n"
            "Rangkaian RLC terdiri dari Resistor (R), Induktor (L), dan Kapasitor (C) yang dihubungkan seri.\n"
            "• Resistor (R): Menghambat arus, mengubah energi listrik menjadi panas.\n"
            "• Induktor (L): Menyimpan energi dalam medan magnet, menahan perubahan arus.\n"
            "• Kapasitor (C): Menyimpan energi dalam medan listrik, menahan perubahan tegangan.\n\n"
            "2. Tegangan dan Arus AC\n"
            "V(t) = Vmax cos(ω t + θv), I(t) = Imax cos(ω t + θi)\n\n"
            "3. Impedansi Z\n"
            "Z = R + j(ωL - 1/ωC), |Z| = sqrt(R^2 + (ωL - 1/ωC)^2), ∠Z = arctan((ωL - 1/ωC)/R)\n\n"
            "4. Daya\n"
            "Daya rata-rata P = V_rms I_rms cos φ, dan daya sesaat P(t) ≈ P_avg + (Vmax Imax/2) cos(2ωt + θv + θi).\n"
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
