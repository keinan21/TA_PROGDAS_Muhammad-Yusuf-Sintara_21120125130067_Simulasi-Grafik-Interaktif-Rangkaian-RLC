from plot import gambarGrafik
import time

#--------------------------------------------------------------------------------------------------------------
# Gluonix Runtime
#--------------------------------------------------------------------------------------------------------------


if __name__=='__main__':
    from Nucleon.Runner import * ###!REQUIRED ------- Any Script Before This Won't Effect GUI Elements
#################################################################################################################################
#################################################################################################################################
#--------------------------------------------------------------------------------------------------------------
# Developer Programming Start
#--------------------------------------------------------------------------------------------------------------


    
    R_input  = Root.FrameInput.InputResistor
    L_input  = Root.FrameInput.InputInduktor
    C_input  = Root.FrameInput.InputKapasitor
    Vm_input = Root.FrameInput.InputVmax
    w_input  = Root.FrameInput.InputW
    sudutV_input = Root.FrameInput.InputSudutV

    tombol_run     = Root.FrameUtama.ButtonHasil
    tombol_materi  = Root.FrameUtama.ButtonMateri
    gambar_grafik  = Root.FrameUtama.FrameGrafik.GambarGrafik
    teks_info      = Root.FrameHasil.TextHasil

    teks_info.Set("Silakan masukkan nilai R, L, C, Vmax, ω, dan sudut V untuk menghitung parameter RLC seri dan menampilkan grafiknya.")


    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False


    def tekanRun():
        print("Tombol Hasil Ditekan")
        R = R_input.Get()
        L = L_input.Get()
        C = C_input.Get()
        Vm = Vm_input.Get()
        w = w_input.Get()
        sudutV = sudutV_input.Get()

        if R == "" or L == "" or C == "" or Vm == "" or w == "" or sudutV == "":
            teks_info.Set("Error: Semua input harus diisi.")
            return
        
        if is_float(R) and is_float(L) and is_float(C) and is_float(Vm) and is_float(w) and is_float(sudutV):
            R = float(R)
            L = float(L)
            C = float(C)
            Vm = float(Vm)
            w = float(w)
            sudutV = float(sudutV)

            obj = gambarGrafik(R, L, C, Vm, w, sudutV)
            gambar_grafik.Set("assets/hasilGrafik.png")

            I, Im, derajatI = obj.getArus()
            Z, Zm, derajatZ = obj.getImpedansi()
            V, Vm, derajatV = obj.getTegangan()

            teks_info.Set(f"""Hasil Perhitungan RLC Seri:
Resistor (R): {R:.2f} Ω
Induktor (L): {L:.2f} H
Kapasitor (C): {C:.2f} F
V(t) = {Vm:.2f} ∠ {derajatV:.2f}° V 
I(t) = {Im:.2f} ∠ {derajatI:.2f}° A
Impedansi (Z): {Zm:.2f} ∠ {derajatZ:.2f}° Ω
Kecepatan Sudut (ω): {w} rad/s
Daya Rata-rata (P): {obj.getDayaRerata():.2f} W
Periode (T): {obj.getPeriode():.2f} s
P(t) = {obj.getDayaRerata():.2f} + {round((Vm * Im) / 2, 2)} cos(2 * {w:.2f} * t + ({derajatV:.2f} - {derajatI:.2f})) W
            """)

        else:
            teks_info.Set("Error: Semua input harus berupa angka.")
            return

    tombol_run.Bind(On_Click=lambda E: tekanRun())


    def munculkanMateri():
        Popup1 = Create_Popup(1)
        Popup1.Show()


    tombol_materi.Bind(On_Click=lambda E: munculkanMateri())
    

        
    
    
#-------------------------------------------------------------------------------------------------------------
# Developer Programming End
# -------------------------------------------------------------------------------------------------------------------------------
#################################################################################################################################
#################################################################################################################################
    Root.Start() ###!REQUIRED ------- Any Script After This Will Not Execute
#################################################################################################################################