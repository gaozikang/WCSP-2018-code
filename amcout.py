import matplotlib.pyplot as plt

class testoutput(object):
    """docstring for [object Object]."""
    def __init__(self, arg):
        self.arg = arg

def nameconvert(modulationType):
    if modulationType == '2pam':
        modulationName = '2-PAM'
    elif modulationType == '4pam':
        modulationName = '4-PAM'
    elif modulationType == '8pam':
        modulationName = '8-PAM'
    elif modulationType == '2psk':
        modulationName = 'BPSK'
    elif modulationType == '4psk':
        modulationName = 'QPSK'
    elif modulationType == '8psk':
        modulationName = '8-PSK'
    elif modulationType == '4qam':
        modulationName = '4-QAM'
    elif modulationType == '16qam':
        modulationName = '16-QAM'
    elif modulationType == '64qam':
        modulationName = '64-QAM'
    elif modulationType == '256qam':
        modulationName = '256-QAM'
    return modulationName


def constplot(signal, title):
    "plot signal constellation on a two-dimentional plane"
    # Initialize markers
    marker = ['o', 'x', 's', 'D']
    color = ['k', 'b', 'r', 'g']
    # Define plot figure size
    plt.figure(figsize=(8, 8), dpi=100)
    for iSignal in range(signal.shape[0]):
        plt.plot(
            signal[iSignal, :].real,
            signal[iSignal, :].imag,
            linestyle='',
            marker=marker[iSignal],
            color=color[iSignal],
            mfc='none')
    plt.title(title)
    plt.xlabel('In-phase Component')
    plt.ylabel('Quadrature Component')
    plt.grid(True)
    plt.show()


def boxplot(signal, title):
    plt.boxplot(signal)
    plt.show()
    pass
