# Some statistical functions used by amcpy package
import numpy as np

def likelihood(signal, channel, modulation_type):
    "Likelihood Function Calculate the log likelihood of signal belonging to a\
            set of bivariate normal distributions with specified\
            signal.symbol_map(means). and sigma(standard deviation)."
    # Calculate noise variance
    sigma = np.sqrt(10**(-channel.snr/10))/np.sqrt(2)

    if channel.antenna_size == (1, 1):
        likelihood = np.sum(np.log(np.mean(np.exp(-np.square(np.abs(np.tile(signal.sample,(signal.symbol_map.size,1))-\
                            np.tile(signal.symbol_map.reshape(signal.symbol_map.size,1),(1,signal.sample.size))))/(2*sigma**2))/(2*np.pi*sigma**2),axis=0)))
    else:
        alphabet_mimo = np.matmul(channel.matrix,np.array(np.meshgrid(signal.symbol_map,signal.symbol_map)).reshape(channel.antenna_size[0],-1))
        likelihood = np.empty([channel.antenna_size[1]])
        for i_receiver in range(channel.antenna_size[1]):
            likelihood[i_receiver] = np.sum(np.log(np.mean(np.exp(-np.square(np.abs(np.tile(signal.sample[i_receiver,:],(alphabet_mimo.shape[1],1))-\
                                            np.tile(np.array(alphabet_mimo[i_receiver,:]),(signal.sample.shape[1],1)).T))/(2*sigma**2))/(2*np.pi*sigma**2),axis=0)))
        likelihood = likelihood.mean()
    return likelihood


def moment(signal, pth, qth):
    "Calcuated high order moment of given signal after normalization"
    signalNorm = signal-np.mean(signal)/np.std(signal)
    moment = np.mean(signalNorm**pth * np.conj(signalNorm)**qth)
    return moment


def cumulant(signal, pth, qth):
    "Calcuated high order cumulant of given signal after normalization"
    signalNorm = signal-np.mean(signal)/np.std(signal)
    moment = np.zeros(pth,qth)
    for ith in range(pth):
        for jth in range(qth):
            moment[ith,jth] = np.mean(signalNorm**pth * np.conj(signalNorm)**qth)
    return moment
