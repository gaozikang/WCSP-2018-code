import numpy as np
import matplotlib.pyplot as plt

'''
########Quadrature-based K-S classifier########
X = np.arange(-10,11)
y_BPSK = [81.36,86.65,92.43,96.23,98.62,99.75,99.99,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
y_QPSK = [37.99,41.09,44.25,47.14,49.70,52.53,55.91,60.28,66.86,75.77,84.86,92.63,97.56,99.69,99.96,100,100,100,100,100,100]
y_4QAM = [12.10,13.43,15.01,17.32,19.93,22.93,27.08,32.44,39.21,49.32,58.94,69.67,78.27,86.02,92.55,97.27,99.38,99.90,100,100,100]
y_16QAM = [33.38,36.00,37.53,39.57,41.70,42.98,44.91,47.93,51.19,55.17,61.34,68.49,76.27,84.16,90.86,95.87,98.67,99.67,99.97,100,100]
plt.figure(figsize=(10,8))
plt.plot(X, y_BPSK, color = 'r',marker = '*',linestyle = '-',label = 'BPSK',linewidth=3)
plt.plot(X, y_QPSK, color = 'b',marker = 'x',linestyle = '-',label = 'QPSK',linewidth=3)
plt.plot(X, y_4QAM, color = 'k',marker = '+',linestyle = '-',label = '4-QAM',linewidth=3)
plt.plot(X, y_16QAM, color = 'g',marker = 'D',linestyle = '-',label = '16-QAM',linewidth=3)
# 设置坐标轴范围
plt.xlim((-10, 10))
plt.ylim((0, 100))
# 设置坐标轴刻度
plt.xticks(np.arange(-10, 11, 2),fontsize=25)
plt.yticks(fontsize=25)
# 设置刻度线朝向
plt.tick_params(direction='in')
# 设置坐标轴名称
plt.xlabel('SNR(dB)',fontsize=25)
plt.ylabel('Classificition Accuracy(%)',fontsize=25)
plt.title('Quadrature-based K-S classifier',fontsize=25)
plt.legend(fontsize=25)
plt.grid(linestyle = 'dotted')
plt.show()
'''
'''
########Quadrature-based C-V M classifier########
X = np.arange(-10,11)
y_BPSK = [88.42,92.98,96.68,98.87,99.75,99.97,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
y_QPSK = [44.25,47.04,49.54,51.65,53.69,56.72,60.74,65.71,72.93,81.37,89.16,95.60,98.98,99.92,100,100,100,100,100,100,100]
y_4QAM = [13.27,14.90,16.50,18.60,21.17,24.78,29.87,36.94,45.70,56.44,68.21,78.73,86.64,92.29,96.41,99.03,99.89,99.99,100,100,100]
y_16QAM = [33.45,35.61,37.41,39.22,40.79,42.81,45.23,48.72,53.33,59.02,65.28,72.70,80.64,87.91,93.61,97.76,99.36,99.89,99.98,100,100]
plt.figure(figsize=(10,8))
plt.plot(X, y_BPSK, color = 'r',marker = '*',linestyle = '-',label = 'BPSK',linewidth=3)
plt.plot(X, y_QPSK, color = 'b',marker = 'x',linestyle = '-',label = 'QPSK',linewidth=3)
plt.plot(X, y_4QAM, color = 'k',marker = '+',linestyle = '-',label = '4-QAM',linewidth=3)
plt.plot(X, y_16QAM, color = 'g',marker = 'D',linestyle = '-',label = '16-QAM',linewidth=3)
# 设置坐标轴范围
plt.xlim((-10, 10))
plt.ylim((0, 100))
# 设置坐标轴刻度
plt.xticks(np.arange(-10, 11, 2),fontsize=25)
plt.yticks(fontsize=25)
# 设置刻度线朝向
plt.tick_params(direction='in')
# 设置坐标轴名称
plt.xlabel('SNR(dB)',fontsize=25)
plt.ylabel('Classificition Accuracy(%)',fontsize=25)
plt.title('Quadrature-based C-V M classifier',fontsize=25)
plt.legend(fontsize=25)
plt.grid(linestyle = 'dotted')
plt.show()
'''
'''
########Quadrature-based A-D classifier########
X = np.arange(-10,11)
y_BPSK = [91.07,95.11,97.84,99.40,99.94,99.99,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
y_QPSK = [43.11,45.55,47.88,50.11,52.14,55.20,59.74,65.98,73.78,82.63,91.04,96.93,99.52,99.98,100,100,100,100,100,100,100]
y_4QAM = [12.37,13.65,15.06,17.28,19.73,23.99,29.05,36.03,45.53,56.60,68.32,78.72,87.23,93.19,97.50,99.52,99.95,100,100,100,100]
y_16QAM = [38.73,40.57,42.71,44.43,46.23,48.78,51.84,56.13,61.94,68.19,74.88,82.28,89.18,94.70,98.25,99.61,99.93,100,100,100,100]
plt.figure(figsize=(10,8))
plt.plot(X, y_BPSK, color = 'r',marker = '*',linestyle = '-',label = 'BPSK',linewidth=3)
plt.plot(X, y_QPSK, color = 'b',marker = 'x',linestyle = '-',label = 'QPSK',linewidth=3)
plt.plot(X, y_4QAM, color = 'k',marker = '+',linestyle = '-',label = '4-QAM',linewidth=3)
plt.plot(X, y_16QAM, color = 'g',marker = 'D',linestyle = '-',label = '16-QAM',linewidth=3)
# 设置坐标轴范围
plt.xlim((-10, 10))
plt.ylim((0, 100))
# 设置坐标轴刻度
plt.xticks(np.arange(-10, 11, 2),fontsize=25)
plt.yticks(fontsize=25)
# 设置刻度线朝向
plt.tick_params(direction='in')
# 设置坐标轴名称
plt.xlabel('SNR(dB)',fontsize=25)
plt.ylabel('Classificition Accuracy(%)',fontsize=25)
plt.title('Quadrature-based A-D classifier',fontsize=25)
plt.legend(loc = 'lower right', fontsize=25)
plt.grid(linestyle = 'dotted')
plt.show()
'''

########Maxium Likelihood classifier########
X = np.arange(-10,11)
y_BPSK = [99.46,99.96,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
y_QPSK = [54.45,59.59,66.02,73.89,83.64,91.97,97.74,99.74,100,100,100,100,100,100,100,100,100,100,100,100,100]
y_4QAM = [40.70,43.77,48.37,54.87,63.18,71.54,80.99,89.90,96.96,99.61,100,100,100,100,100,100,100,100,100,100,100]
y_16QAM = [27.03,30.59,36.44,43.63,54.01,66.80,79.73,90.12,96.70,99.62,99.98,100,100,100,100,100,100,100,100,100,100]
plt.figure(figsize=(10,8))
plt.plot(X, y_BPSK, color = 'r',marker = '*',linestyle = '-',label = 'BPSK',linewidth=3)
plt.plot(X, y_QPSK, color = 'b',marker = 'x',linestyle = '-',label = 'QPSK',linewidth=3)
plt.plot(X, y_4QAM, color = 'k',marker = '+',linestyle = '-',label = '4-QAM',linewidth=3)
plt.plot(X, y_16QAM, color = 'g',marker = 'D',linestyle = '-',label = '16-QAM',linewidth=3)
# 设置坐标轴范围
plt.xlim((-10, 10))
plt.ylim((0, 100))
# 设置坐标轴刻度
plt.xticks(np.arange(-10, 11, 2),fontsize=25)
plt.yticks(fontsize=25)
# 设置刻度线朝向
plt.tick_params(direction='in')
# 设置坐标轴名称
plt.xlabel('SNR(dB)',fontsize=25)
plt.ylabel('Classificition Accuracy(%)',fontsize=25)
plt.title('Maxium Likelihood classifier',fontsize=25)
plt.legend(loc = 'lower right', fontsize=25)
plt.grid(linestyle = 'dotted')
plt.show()

'''
########Average classifier########
X = np.arange(-10,11)
y_KS = [41.2075,44.2925,47.305,50.065,52.4875,54.5475,56.9725,60.1625,64.315,70.065,76.285,82.6975,88.025,92.4675,95.8425,98.285,99.5125,99.8925,99.9925,100,100]
y_CVM = [44.8475,47.6325,50.0325,52.085,53.85,56.07,58.96,62.8425,67.99,74.2075,80.6625,86.7575,91.565,95.03,97.505,99.1975,99.8125,99.97,99.995,100,100]
y_AD= [46.32,48.72,50.8725,52.805,54.51,56.99,60.1575,64.535,70.3125,76.855,83.56,89.4825,93.9825,96.9675,98.9375,99.7825,99.97,100,100,100,100]
y_ML = [55.41,58.4775,62.7075,68.0975,75.2075,82.5775,89.615,94.94,98.415,99.8075,99.995,100,100,100,100,100,100,100,100,100,100]
plt.figure(figsize=(10,8))
plt.plot(X, y_KS, color = 'r',marker = '*',linestyle = '-',label = 'K-S test',linewidth=3)
plt.plot(X, y_CVM, color = 'b',marker = 'x',linestyle = '-',label = 'C-v-M test',linewidth=3)
plt.plot(X, y_AD, color = 'k',marker = '+',linestyle = '-',label = 'A-D test',linewidth=3)
plt.plot(X, y_ML, color = 'g',marker = 'D',linestyle = '-',label = 'ML',linewidth=3)
# 设置坐标轴范围
plt.xlim((-10, 10))
plt.ylim((0, 100))
# 设置坐标轴刻度
plt.xticks(np.arange(-10, 11, 2),fontsize=25)
plt.yticks(fontsize=25)
# 设置刻度线朝向
plt.tick_params(direction='in')
# 设置坐标轴名称
plt.xlabel('SNR(dB)',fontsize=25)
plt.ylabel('Classificition Accuracy(%)',fontsize=25)
# plt.title('Maxium Likelihood classifier',fontsize=20)
plt.legend(loc = 'lower right', fontsize=25)
plt.grid(linestyle = 'dotted')
plt.show()
'''
