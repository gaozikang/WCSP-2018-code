import numpy as np
from scipy.stats import norm

def amcml(signal,channel,test):
    "AMCML classifies the modulation type of the input signal using the maxium\
            likelihood classifier."
    likelihood_pool = np.zeros(len(test.modulation_pool))
    for i_modulation in range(len(test.modulation_pool)):
        sigma = np.sqrt(10**(-channel.snr/10))/np.sqrt(2)
        symbol_map = test.getsymbolmap(test.modulation_pool[i_modulation])
        if channel.antenna_size == (1, 1):
            likelihood_pool[i_modulation] = np.sum(np.log(np.mean(np.exp(-np.square(np.abs(np.tile(signal.sample,(symbol_map.size,1))\
                                           -np.tile(symbol_map.reshape(symbol_map.size,1),(1,signal.sample.size))))/(2*sigma**2))/(2*np.pi*sigma**2),axis=0)))
        else:
            alphabet_mimo = np.matmul(channel.matrix,np.array(np.meshgrid(symbol_map,symbol_map)).reshape(channel.antenna_size[0],-1))
            alphabet_power = np.mean(np.square(np.abs(alphabet_mimo)))
            alphabet_mimo = alphabet_mimo / np.sqrt(alphabet_power)
            sigma = np.sqrt(10**(-channel.snr/10))/np.sqrt(2)
            likelihood = np.empty([int(signal.sample_num/channel.antenna_size[0])])
            for i_sample in range(int(signal.sample_num/channel.antenna_size[0])):
                sample_rep = np.transpose(np.tile(signal.sample[:,i_sample],(alphabet_mimo.shape[1],1)))
                likelihood[i_sample] = np.log(np.mean(1/(2*np.pi*sigma**2)**channel.antenna_size[1]*np.exp(-1/(2*sigma**2)*\
                                       np.linalg.norm(np.abs(sample_rep-alphabet_mimo),axis=0)**2)))
            likelihood_pool[i_modulation] = likelihood.mean()
    # print(likelihood_pool)
    decision = np.argmax(likelihood_pool)
    return decision

# Define a function for empirical cumulative distribution
def ecdf(sigIn):
    quantiles = np.sort(sigIn)
    cumprob = np.arange(1,len(quantiles)+1) / len(quantiles)
    return quantiles, cumprob

########Quadrature-based K-S classifier########
def amcks_Q(signal,channel,test):
    "AMCKS classifies the modulation type of the input signal using the\
           Kolmogorov-Smirnov test classifier."
    # Calculate the noise variance from SNR
    sigma = np.sqrt(10**(-channel.snr/10))/np.sqrt(2)
    len_ModPool = len(test.modulation_pool)
    cdf = norm.cdf
    test_stat = []
    for i_receiver in range(channel.antenna_size[1]):
        # Calculate emperical distribution on in-phase segment for each receiving antenna
        x_I,emperical_I = ecdf(signal.sample[i_receiver,:].real)
        # Calculate emperical distribution on quadrature segment for each receiving antenna
        x_Q,emperical_Q = ecdf(signal.sample[i_receiver,:].imag)
        dis_I = []
        dis_Q = []
        for i_modulation in range(len_ModPool):
            # Generate alphabet symbols for the modulation
            symbol = test.getsymbolmap(test.modulation_pool[i_modulation])
            # Generate modulation symbols in a MIMO system
            alphabet_mimo = np.matmul(channel.matrix,np.array(np.meshgrid(symbol,symbol)).reshape(channel.antenna_size[0],-1))
            alphabet_power = np.mean(np.square(np.abs(alphabet_mimo)))
            alphabet_mimo = alphabet_mimo / np.sqrt(alphabet_power)
            symbol_I_MIMO = np.sort(alphabet_mimo[i_receiver,:].real)
            symbol_Q_MIMO = np.sort(alphabet_mimo[i_receiver,:].imag)
            len_I = len(symbol_I_MIMO)
            len_Q = len(symbol_Q_MIMO)
            # Calculate theoretical cumulative distribution at in-phase signal values for each receiving antenna
            cumdis_I = []
            for iSymbol_I_MIMO in range(len_I):
                cumdis_I.append(cdf(x_I,loc = symbol_I_MIMO[iSymbol_I_MIMO],scale = sigma))
            cumdis_I_aver = np.sum(cumdis_I,axis = 0) / len_I
            # Evaluate KS distance between in-phase signal emperical CDF and theoretical CDF for each receiving antenna
            dis_I.append(np.max(np.abs(emperical_I - cumdis_I_aver)))
            # Calculate theoretical cumulative distribution at quadrature signal values for each receiving antenna
            cumdis_Q = []
            for iSymbol_Q_MIMO in range(len_Q):
                cumdis_Q.append(cdf(x_Q,loc = symbol_Q_MIMO[iSymbol_Q_MIMO],scale = sigma))
            cumdis_Q_aver = np.sum(cumdis_Q,axis = 0) / len_Q
            # Evaluate KS distance between quadrature signal emperical CDF and theoretical CDF for each receiving antenna
            dis_Q.append(np.max(np.abs(emperical_Q - cumdis_Q_aver)))
        # Calcualte the KS test statistics for the modulation for each receiving antenna
        test_stat.append(np.mean([dis_I,dis_Q],axis = 0))
    # Calcualte the KS test statistics for the modulation
    test_stat = np.mean(test_stat,axis = 0)
    # Find the modulation hyphotheses with smallest test statistics
    decision = np.argmin(test_stat)
    return decision, x_I

def amccvm_Q(signal,channel,test):
    "AMCCVM classifies the modulation type of the input signal using the\
            Cramer–Von Mises test classifier."
    # Calculate the noise variance from SNR
    sigma = np.sqrt(10**(-channel.snr/10))/np.sqrt(2)
    cdf = norm.cdf
    m = len(test.modulation_pool)
    test_stat = []
    for i_receiver in range(channel.antenna_size[1]):
        x_I = np.sort(signal.sample[i_receiver,:].real)
        x_Q = np.sort(signal.sample[i_receiver,:].imag)
        len_x_I = len(x_I)
        len_x_Q = len(x_Q)
        cvm_I = []
        cvm_Q = []
        for i_modulation in range(m):
            # Generate alphabet symbols for the modulation
            symbol = test.getsymbolmap(test.modulation_pool[i_modulation])
            # Generate modulation symbols in a MIMO system
            alphabet_mimo = np.matmul(channel.matrix,np.array(np.meshgrid(symbol,symbol)).reshape(channel.antenna_size[0],-1))
            alphabet_power = np.mean(np.square(np.abs(alphabet_mimo)))
            alphabet_mimo = alphabet_mimo / np.sqrt(alphabet_power)
            symbol_I_MIMO = np.sort(alphabet_mimo[i_receiver,:].real)
            symbol_Q_MIMO = np.sort(alphabet_mimo[i_receiver,:].imag)
            len_I = len(symbol_I_MIMO)
            len_Q = len(symbol_Q_MIMO)
            # Calculate theoretical cumulative distribution at in-phase signal values for each receiving antenna
            cumdis_I = []
            for iSymbol_I_MIMO in range(len_I):
                icumdis_I = cdf(x_I,loc = symbol_I_MIMO[iSymbol_I_MIMO],scale = sigma)
                cumdis_I.append(icumdis_I)
            cumdis_I_aver = np.sum(cumdis_I,axis = 0) / len_I
            icvm_I = np.sum(np.square(cumdis_I_aver - ((2 * np.arange(1,len_x_I + 1)) - 1) / (2 * len_x_I))) + 1 / (12 * len_x_I)
            cvm_I.append(icvm_I)
            # Calculate theoretical cumulative distribution at quadrature signal values for each receiving antenna
            cumdis_Q = []
            for iSymbol_Q_MIMO in range(len_Q):
                icumdis_Q = cdf(x_Q,loc = symbol_Q_MIMO[iSymbol_Q_MIMO],scale = sigma)
                cumdis_Q.append(icumdis_Q)
            cumdis_Q_aver = np.sum(cumdis_Q,axis = 0) / len_Q
            icvm_Q = np.sum(np.square(cumdis_Q_aver - ((2 * np.arange(1,len_x_Q + 1)) - 1) / (2 * len_x_Q))) + 1 / (12 * len_x_Q)
            cvm_Q.append(icvm_Q)
        # Calcualte the KS test statistics for the modulation for each receiving antenna
        itest_stat = np.mean([cvm_I,cvm_Q],axis = 0)
        test_stat.append(itest_stat)
    # Calcualte the KS test statistics for the modulation    print(decision)
    test_stat = np.mean(test_stat,axis = 0)
    # Find the modulation hyphotheses with smallest test statistics
    decision = np.argmin(test_stat)
    return decision

def amcad_Q(signal,channel,test):
    "AMCAD classifies the modulation type of the input signal using the\
           Anderson-Darling test classifier."
    # Calculate the noise variance from SNR
    sigma = np.sqrt(10**(-channel.snr/10))/np.sqrt(2)
    cdf = norm.cdf
    m = len(test.modulation_pool)
    test_stat = []
    for i_receiver in range(channel.antenna_size[1]):
        x_I = np.sort(signal.sample[i_receiver,:].real)
        x_Q = np.sort(signal.sample[i_receiver,:].imag)
        len_x_I = len(x_I)
        len_x_Q = len(x_Q)
        ad_I = []
        ad_Q = []
        for i_modulation in range(m):
            # Generate alphabet symbols for the modulation
            symbol = test.getsymbolmap(test.modulation_pool[i_modulation])
            # Generate modulation symbols in a MIMO system
            alphabet_mimo = np.matmul(channel.matrix,np.array(np.meshgrid(symbol,symbol)).reshape(channel.antenna_size[0],-1))
            alphabet_power = np.mean(np.square(np.abs(alphabet_mimo)))
            alphabet_mimo = alphabet_mimo / np.sqrt(alphabet_power)
            symbol_I_MIMO = np.sort(alphabet_mimo[i_receiver,:].real)
            symbol_Q_MIMO = np.sort(alphabet_mimo[i_receiver,:].imag)
            len_I = len(symbol_I_MIMO)
            len_Q = len(symbol_Q_MIMO)
            # Calculate theoretical cumulative distribution at in-phase signal values for each receiving antenna
            cumdis_I = []
            for iSymbol_I_MIMO in range(len_I):
                icumdis_I = cdf(x_I,loc = symbol_I_MIMO[iSymbol_I_MIMO],scale = sigma)
                cumdis_I.append(icumdis_I)
            cumdis_I_aver = np.sum(cumdis_I,axis = 0) / len_I
            iad_I = (-len_x_I - (1 / len_x_I) * np.sum(((2 * np.arange(1,len_x_I + 1)) - 1) * np.log(cumdis_I_aver) + \
                    (2 * len_x_I + 1 - 2 * np.arange(1,len_x_I + 1)) * np.log(1 - cumdis_I_aver)))
            ad_I.append(iad_I)
            # Calculate theoretical cumulative distribution at quadrature signal values for each receiving antenna
            cumdis_Q = []
            for iSymbol_Q_MIMO in range(len_Q):
                icumdis_Q = cdf(x_Q,loc = symbol_Q_MIMO[iSymbol_Q_MIMO],scale = sigma)
                cumdis_Q.append(icumdis_Q)
            cumdis_Q_aver = np.sum(cumdis_Q,axis = 0) / len_Q
            iad_Q = (-len_x_Q - (1 / len_x_Q) * np.sum(((2 * np.arange(1,len_x_Q + 1)) - 1) * np.log(cumdis_Q_aver) + \
                    (2 * len_x_Q + 1 - 2 * np.arange(1,len_x_Q + 1)) * np.log(1 - cumdis_Q_aver)))
            ad_Q.append(iad_Q)
        # Calcualte the KS test statistics for the modulation for each receiving antenna
        itest_stat = np.mean([ad_I,ad_Q],axis = 0)
        test_stat.append(itest_stat)
    # Calcualte the KS test statistics for the modulation
    test_stat = np.mean(test_stat,axis = 0)
    # Find the modulation hyphotheses with smallest test statistics
    decision = np.argmin(test_stat)
    return decision
