import sys
sys.path.append('C:\ProgramData\miniconda3\envs\DGU01\Lib\site-packages')
import math
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

def chastotniy_analiz_mx(m_aplituda, chastota_diskretizasii, N_tochechnoe):
    mx = []
    for m in range(m_aplituda):
        mx.append(m * chastota_diskretizasii/N_tochechnoe)
    return mx

def chastotniy_analiz(m_aplituda, chastota_diskretizasii, N_tochechnoe):
    return m_aplituda * chastota_diskretizasii/N_tochechnoe

def Xm_amplituda(deystvitelnaya_chast, mnimaya_chast):
    return math.sqrt(math.pow(deystvitelnaya_chast, 2) + math.pow(mnimaya_chast, 2))

def Xps_moshnost(deystvitelnaya_chast, mnimaya_chast):
    return math.pow(deystvitelnaya_chast, 2) + math.pow(mnimaya_chast, 2)

def fazoviy_ugol(deystvitelnaya_chast, mnimaya_chast):
    return math.degrees(math.asin(deystvitelnaya_chast/mnimaya_chast))

pi = math.pi
A1 = 1
A2 = 0.5
F1 = 1000
F2 = 2000
RF1 = 0
RF2 = 3*pi / 4
fs = 8000
N_tochechnoe = 8
ts = 1/fs

mx = []
Xmnimaya_y = []
Xdeystivtelnaya_y = []
Xmagy = []
Xpsy = []
Xrfy = []

for m in range(N_tochechnoe):
    Xm = 0
    for n in range(N_tochechnoe):
        xin = A1 * math.sin(2 * pi * F1 * n * ts + RF1) + A2 * math.sin(2 * pi * F2 * n * ts + RF2)
        Xm += xin * math.cos(2 *pi * chastotniy_analiz(n, m, N_tochechnoe)) - 1j * xin * math.sin(2 * pi * chastotniy_analiz(n, m, N_tochechnoe))

    Xmag = Xm_amplituda(Xm.real, Xm.imag)
    Xps = Xps_moshnost(Xm.real, Xm.imag)
    Xrf = fazoviy_ugol(Xm.imag, Xmag)

    Xdeystivtelnaya_y.append(Xm.real)
    Xmnimaya_y.append(Xm.imag)
    Xmagy.append(Xmag)
    Xpsy.append(Xps)
    Xrfy.append(Xrf)

    #print("%.4f %sj" % (Xm.real, Xm.imag))
    #print("Ximag %.4f" % Xm.imag)
    #print("Xmag %s" % Xmag)
    #print("Xps %s" % Xps)
    #print("Xf %s" % Xrf)


font1 = {'family': 'serif', 'color': 'blue', 'size': 12}
font2 = {'family': 'serif', 'color': 'black', 'size': 11}

mx = chastotniy_analiz_mx(8, 8, 8)
x = np.array(mx)
y = np.array(Xmagy)
plt.subplot(2, 2, 1)
plt.plot(x,y, 'o')
plt.vlines(x = mx, ymin = [0], ymax = Xmagy,
           colors = 'teal')
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.title("Модуль X(m)", fontdict=font1)
plt.xlabel("m (КГц)", fontdict=font2)


x = np.array(mx)
y = np.array(Xdeystivtelnaya_y)
plt.subplot(2, 2, 2)
plt.plot(x,y, 'o')
plt.vlines(x = mx, ymin = [0], ymax = Xdeystivtelnaya_y,
           colors = 'teal')
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.title("Действитальная част X(m)", fontdict=font1)
plt.xlabel("m (КГц)", fontdict=font2)

x = np.array(mx)
y = np.array(Xrfy)
plt.subplot(2, 2, 3)
plt.plot(x,y, 'o')
plt.vlines(x = mx, ymin = [0], ymax = Xrfy,
           colors = 'teal')

plt.axhline(y=0, color='black', linewidth=0.5, linestyle='-')
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.title("Фаза X(m) в градусах, Xf(m)", fontdict=font1)
plt.xlabel("m (КГц)", fontdict=font2)

x = np.array(mx)
y = np.array(Xmnimaya_y)
plt.subplot(2, 2, 4)
plt.plot(x,y, 'o')
plt.vlines(x = mx, ymin = [0], ymax = Xmnimaya_y,
           colors = 'teal')

plt.axhline(y=0, color='black', linewidth=0.5, linestyle='-')
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.title("Мнимая част X(m)", fontdict=font1)
plt.xlabel("m (КГц)", fontdict=font2)

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
