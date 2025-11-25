
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from perhitungan import plot

def gambarGrafik(resistor, induktor, kapasitor, vmax, kecepatanSudut, derajatV):
    obj = plot(resistor, induktor, kapasitor, vmax, kecepatanSudut, derajatV)

    V = obj.getPlotTegangan()
    I = obj.getPlotArus()
    P = obj.getPlotDaya()
    t = obj.getJangkaWaktu()

    mpl.style.use("dark_background")

    fig, (ax_tegangan, ax_daya) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    plot_tegangan, = ax_tegangan.plot(t, V, label='Tegangan (V)', color='deepskyblue', linewidth=1.8, zorder=3)
    ax_tegangan.set_ylabel('Tegangan (V)', family="monospace", color='deepskyblue')

    ax_arus = ax_tegangan.twinx()
    plot_arus, = ax_arus.plot(t, I, label='Arus (A)', color='orange', linewidth=1.8, zorder=2)
    ax_arus.set_ylabel('Arus (A)', family="monospace", color='orange')

    if len(I):
        ymin = np.nanmin(I)
        ymax = np.nanmax(I)
        if np.isfinite(ymin) and np.isfinite(ymax) and ymin != ymax:
            pad = 0.05 * (ymax - ymin)
            ax_arus.set_ylim(ymin - pad, ymax + pad)

    ax_tegangan.grid(True, which='both', alpha=0.25)

    lines_top = [plot_tegangan, plot_arus]
    labels_top = [l.get_label() for l in lines_top]
    ax_tegangan.legend(lines_top, labels_top, loc='upper right')

    plotP, = ax_daya.plot(t, P, label='Daya (W)', color='lime', linewidth=1.8)
    ax_daya.set_ylabel('Daya (W)', family="monospace", color='lime')
    ax_daya.set_xlabel('Waktu (s)', family="monospace")
    ax_daya.grid(True, which='both', alpha=0.25)
    ax_daya.legend(loc='upper right')

    fig.suptitle('Plot RLC Seri: Tegangan, Arus, dan Daya', fontsize=16, family="monospace")
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    plt.savefig('assets/hasilGrafik.png', dpi=600)

    return obj


