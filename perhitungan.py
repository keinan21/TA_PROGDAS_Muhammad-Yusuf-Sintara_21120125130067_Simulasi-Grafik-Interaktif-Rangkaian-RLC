import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

class hitung:
    def __init__ (self, resistor, induktor, kapasitor, vmax, kecepatanSudut, derajatV):
        self.resistor = resistor
        self.induktor = induktor
        self.kapasitor = kapasitor
        self.vmax = vmax
        self.kecepatanSudut = kecepatanSudut
        self.derajatV = derajatV

        self.impedansi = self.hitungImpedansi(resistor, induktor, kapasitor, kecepatanSudut)
        self.magnitudoZ = abs(self.impedansi)
        self.radianZ = cmath.phase(self.impedansi)
        self.derajatZ = math.degrees(self.radianZ)

        self.tegangan = self.hitungV(vmax, derajatV)
        self.magnitudoV = abs(self.tegangan)
        self.radianV = math.radians(derajatV)

        self.arus = self.tegangan / self.impedansi
        self.magnitudoI = abs(self.arus)
        self.radianI = cmath.phase(self.arus)
        self.derajatI = math.degrees(self.radianI)

        self.dayaRerata = self.hitungDayaRerata(self.magnitudoI, self.magnitudoV, self.radianI, self.radianV)
        self.radianDaya = self.radianV - self.radianI
        self.derajatDaya = math.degrees(self.radianDaya)
        self.faktorDaya = math.cos(self.radianDaya)

        self.periode = self.hitungPeriode(self.kecepatanSudut)
        self.frekuensi = 1 / self.periode



    @staticmethod
    def hitungImpedansi(R, L, C, w):
        Z = complex(R, w*L - 1/(w*C))
        return Z

    @staticmethod
    def hitungV(amplitudo, sudut):
        V = cmath.rect(amplitudo, math.radians(sudut))
        return V

    @staticmethod
    def hitungDayaRerata(imax, vmax,radianI, radianV):
        return (1/2) * imax * vmax * math.cos(radianV - radianI)

    @staticmethod
    def hitungPeriode(w):
        return 2 * math.pi / w

    def getResistor(self):
        return self.resistor

    def getInduktor(self):
        return self.induktor

    def getKapasitor(self):
        return self.kapasitor

    def getTegangan(self):
        return self.tegangan, self.magnitudoV, self.derajatV
    
    def getArus(self):
        return self.arus, self.magnitudoI, self.derajatI

    def getKecepatanSudut(self):
        return self.kecepatanSudut

    def getImpedansi(self):
        return self.impedansi, self.magnitudoZ, self.derajatZ


    

class plot(hitung):
    def __init__(self, resistor, induktor, kapasitor, vmax, kecepatanSudut, derajatV):
        super().__init__(resistor, induktor, kapasitor, vmax, kecepatanSudut, derajatV)
        self.jangkaWaktu = np.linspace(0, 2*self.periode, 1000)
        self.plotTegangan = self.magnitudoV * np.cos(self.kecepatanSudut * self.jangkaWaktu + self.radianV)
        self.plotArus = self.magnitudoI * np.cos(self.kecepatanSudut * self.jangkaWaktu + self.radianI)
        self.plotDaya = self.dayaRerata + (self.magnitudoV * self.magnitudoI / 2) * np.cos(self.radianI + self.radianV + 2 * self.kecepatanSudut * self.jangkaWaktu)

    def getPlotTegangan(self):
        return self.plotTegangan

    def getPlotArus(self):
        return self.plotArus
    
    def getPlotDaya(self): 
        return self.plotDaya

    def getJangkaWaktu(self):
        return self.jangkaWaktu
        
