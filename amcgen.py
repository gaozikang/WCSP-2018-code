import numpy as np


class Channel(object):
    "declaration for channel class"

    def __init__(self, type=['awgn'], snr=20, antenna_size=(1, 1), freq_off=0, phase_off=0):
        self.type = type
        self.snr = snr
        self.antenna_size = antenna_size
        np.random.seed(0)
        self.matrix = np.random.randn(antenna_size[1], antenna_size[0]) + 1j * np.random.randn(antenna_size[1], antenna_size[0])
        self.freq_off = freq_off
        self.phase_off = phase_off

class Signal(object):
    "declaration for signal class"

    def __init__(self, modulation_type='4qam', sample_num=128, index_method='random'):
        self.modulation_type = modulation_type
        self.sample_num = sample_num
        self.index_method = index_method
        self.getsymbolmap()
        self.genmodsig()

    def getsymbolmap(self):
        "GETALPHABET    Generate set of alphabet according to modulation type."
        # Create basic mapping of signal symbols
        if self.modulation_type == '2pam':
            symbol_map = np.array([1, -1])
        elif self.modulation_type == '4pam':
            symbol_map = np.array([-3, -1, 1, 3])
        elif self.modulation_type == '8pam':
            symbol_map = np.array([-7, -5, -3, -1, 1, 3, 5, 7])
        elif self.modulation_type == '2psk':
            symbol_map = np.array([1j, -1j])
        elif self.modulation_type == '4psk':
            symbol_map = np.array([1, 1j, -1, -1j])
        elif self.modulation_type == '8psk':
            symbol_map = np.array([1.4142, 1 + 1j, 1.4142j, -1 + 1j,
                                   -1.4142, -1 - 1j, -1.4142j, 1 - 1j])
        elif self.modulation_type == '4qam':
            symbol_map = np.array([1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j])
        elif self.modulation_type == '16qam':
            symbol_map = np.array([3 + 3j, 3 + 1j, 3 - 1j, 3 - 3j, 1 + 3j, 1 + 1j, 1 - 1j,
                                   1 - 3j, -1 + 3j, -1 + 1j, -1 - 1j, -1 - 3j, -3 + 3j, -3 + 1j, -3 - 1j, -3 - 3j])
        elif self.modulation_type == '64qam':
            symbol_map = np.array([1 + 1j, 3 + 1j, 1 + 3j, 3 + 3j, 7 + 1j, 5 + 1j, 7 + 3j,
                                   5 + 3j, 1 + 7j, 3 + 7j, 1 + 5j, 3 + 5j, 7 + 7j, 5 + 7j, 7 + 5j, 5 + 5j, 1 - 1j,
                                   1 - 3j, 3 - 1j, 3 - 3j, 1 - 7j, 1 - 5j, 3 - 7j, 3 - 5j, 7 - 1j, 7 - 3j, 5 - 1j,
                                   5 - 3j, 7 - 7j, 7 - 5j, 5 - 7j, 5 - 5j, -1 + 1j, -1 + 3j, -3 + 1j, -3 + 3j,
                                   -1 + 7j, -1 + 5j, -3 + 7j, -3 + 5j, -7 + 1j, -7 + 3j, -5 + 1j, -5 + 3j,
                                   -7 + 7j, -7 + 5j, -5 + 7j, -5 + 5j, -1 - 1j, -3 - 1j, -1 - 3j, -3 - 3j,
                                   -7 - 1j, -5 - 1j, -7 - 3j, -5 - 3j, -1 - 7j, -3 - 7j, -1 - 5j, -3 - 5j,
                                   -7 - 7j, -5 - 7j, -7 - 5j, -5 - 5j])
        elif self.modulation_type == '256qam':
            symbol_map = np.array([1 + 1j, 1 + 3j, 1 + 5j, 1 + 7j, 1 + 9j, 1 + 11j, 1 + 13j,
                                   1 + 15j, 1 - 1j, 1 - 3j, 1 - 5j, 1 - 7j, 1 - 9j, 1 - 11j, 1 - 13j, 1 - 15j,
                                   3 + 1j, 3 + 3j, 3 + 5j, 3 + 7j, 3 + 9j, 3 + 11j, 3 + 13j, 3 + 15j, 3 - 1j,
                                   3 - 3j, 3 - 5j, 3 - 7j, 3 - 9j, 3 - 11j, 3 - 13j, 3 - 15j, 5 + 1j, 5 + 3j,
                                   5 + 5j, 5 + 7j, 5 + 9j, 5 + 11j, 5 + 13j, 5 + 15j, 5 - 1j, 5 - 3j, 5 - 5j,
                                   5 - 7j, 5 - 9j, 5 - 11j, 5 - 13j, 5 - 15j, 7 + 1j, 7 + 3j, 7 + 5j, 7 + 7j,
                                   7 + 9j, 7 + 11j, 7 + 13j, 7 + 15j, 7 - 1j, 7 - 3j, 7 - 5j, 7 - 7j, 7 - 9j,
                                   7 - 11j, 7 - 13j, 7 - 15j, 9 + 1j, 9 + 3j, 9 + 5j, 9 + 7j, 9 + 9j, 9 + 11j,
                                   9 + 13j, 9 + 15j, 9 - 1j, 9 - 3j, 9 - 5j, 9 - 7j, 9 - 9j, 9 - 11j, 9 - 13j,
                                   9 - 15j, 11 + 1j, 11 + 3j, 11 + 5j, 11 + 7j, 11 + 9j, 11 + 11j, 11 + 13j,
                                   11 + 15j, 11 - 1j, 11 - 3j, 11 - 5j, 11 - 7j, 11 - 9j, 11 - 11j, 11 - 13j,
                                   11 - 15j, 13 + 1j, 13 + 3j, 13 + 5j, 13 + 7j, 13 + 9j, 13 + 11j, 13 + 13j,
                                   13 + 15j, 13 - 1j, 13 - 3j, 13 - 5j, 13 - 7j, 13 - 9j, 13 - 11j, 13 - 13j,
                                   13 - 15j, 15 + 1j, 15 + 3j, 15 + 5j, 15 + 7j, 15 + 9j, 15 + 11j, 15 + 13j,
                                   15 + 15j, 15 - 1j, 15 - 3j, 15 - 5j, 15 - 7j, 15 - 9j, 15 - 11j, 15 - 13j,
                                   15 - 15j, -1 + 1j, -1 + 3j, -1 + 5j, -1 + 7j, -1 + 9j, -1 + 11j, -1 + 13j,
                                   -1 + 15j, -1 - 1j, -1 - 3j, -1 - 5j, -1 - 7j, -1 - 9j, -1 - 11j, -1 - 13j,
                                   -1 - 15j, -3 + 1j, -3 + 3j, -3 + 5j, -3 + 7j, -3 + 9j, -3 + 11j, -3 + 13j,
                                   -3 + 15j, -3 - 1j, -3 - 3j, -3 - 5j, -3 - 7j, -3 - 9j, -3 - 11j, -3 - 13j,
                                   -3 - 15j, -5 + 1j, -5 + 3j, -5 + 5j, -5 + 7j, -5 + 9j, -5 + 11j, -5 + 13j,
                                   -5 + 15j, -5 - 1j, -5 - 3j, -5 - 5j, -5 - 7j, -5 - 9j, -5 - 11j, -5 - 13j,
                                   -5 - 15j, -7 + 1j, -7 + 3j, -7 + 5j, -7 + 7j, -7 + 9j, -7 + 11j, -7 + 13j,
                                   -7 + 15j, -7 - 1j, -7 - 3j, -7 - 5j, -7 - 7j, -7 - 9j, -7 - 11j, -7 - 13j,
                                   -7 - 15j, -9 + 1j, -9 + 3j, -9 + 5j, -9 + 7j, -9 + 9j, -9 + 11j, -9 + 13j,
                                   -9 + 15j, -9 - 1j, -9 - 3j, -9 - 5j, -9 - 7j, -9 - 9j, -9 - 11j, -9 - 13j,
                                   -9 - 15j, -11 + 1j, -11 + 3j, -11 + 5j, -11 + 7j, -11 + 9j, -11 + 11j,
                                   -11 + 13j, -11 + 15j, -11 - 1j, -11 - 3j, -11 - 5j, -11 - 7j, -11 - 9j,
                                   -11 - 11j, -11 - 13j, -11 - 15j, -13 + 1j, -13 + 3j, -13 + 5j, -13 + 7j,
                                   -13 + 9j, -13 + 11j, -13 + 13j, -13 + 15j, -13 - 1j, -13 - 3j, -13 - 5j,
                                   -13 - 7j, -13 - 9j, -13 - 11j, -13 - 13j, -13 - 15j, -15 + 1j, -15 + 3j,
                                   -15 + 5j, -15 + 7j, -15 + 9j, -15 + 11j, -15 + 13j, -15 + 15j, -15 - 1j,
                                   -15 - 3j, -15 - 5j, -15 - 7j, -15 - 9j, -15 - 11j, -15 - 13j, -15 - 15j])
        # Normalize symbol map with unit power
        symbol_map_power = np.mean(np.square(np.abs(symbol_map)))
        symbol_map = symbol_map / np.sqrt(symbol_map_power)
        self.symbol_map = symbol_map

    def genmodsig(self):
        "GENMODSIG   Generate i.i.d modulated signal samples with unit power"
        # Generate random signal modulation index
        if self.index_method == 'random':
            # Create uniform random index of signal samples, e.g. 0,2,2,1,3,1
            index = np.floor(np.random.rand(self.sample_num)* self.symbol_map.size)
            self.index = index.astype(int)
        elif self.index_method == 'sequential':
            # Create sequential index of signal samples, e.g. 1,2,3,1,2,3
            sequence = range(self.symbol_map.size)
            self.index = np.tile(sequence, int(self.sample_num / self.symbol_map.size))
        elif self.index_method == 'sequential-block':
            # Create block sequential index of signal samples, e.g. 1,1,2,2,3,3
            sequence = range(self.symbol_map.size)
            self.index = np.repeat(sequence, int(self.sample_num / self.symbol_map.size))
        # Map the signal samples to symbols
        sample = np.take(self.symbol_map, self.index).reshape(1, self.sample_num)
        # Normalise symbol
        # Calculate signal power
        sample_power = np.mean(np.square(np.abs(sample)))
        # symbol_map = np.divide(symbol_map, np.sqrt(symbolPower))
        self.sample = sample / np.sqrt(sample_power)

    def applychannel(self, channel):
        if channel.antenna_size != (1, 1):  # if apply mimo configuration
            # Create transmitting signal matrix
            signal_transmit = self.sample.reshape(channel.antenna_size[0], self.sample_num // channel.antenna_size[0])
        # Generate channel matrix
            self.sample = np.matmul(channel.matrix, signal_transmit)
            sample_power = np.mean(np.square(np.abs(self.sample)))
            self.sample = self.sample / np.sqrt(sample_power)
        # Apply channel effects
        if 'fading' in channel.type:  # if apply fading channel
            # Phase offset vector
            phase_vector = np.cos(channel.phase_off) + np.sin(channel.phase_off) * 1j
            # Frequence offset vector
            freq_vector = np.cos(channel.freq_off * np.pi * np.tile((np.arange(self.sample_num / channel.antenna_size[0]) + 1), (channel.antenna_size[1], 1))) + np.sin(
                channel.freq_off * np.pi * np.tile((np.arange(self.sample_num / channel.antenna_size[0]) + 1), (channel.antenna_size[1], 1))) * 1j
            # Apply phase and freqence offset to signal
            self.sample = np.multiply(self.sample, freq_vector) * phase_vector
        if 'awgn' in channel.type:  # if apply additive white gaussian noise
            # Determine the dimension of input signal data
            noise = np.random.randn(*self.sample.shape) + 1j * np.random.randn(*self.sample.shape)
            signal_power = np.mean(np.square(np.absolute(self.sample)))
            noise_power = np.mean(np.square(np.absolute(noise)))
            noise_scale = np.sqrt(signal_power / noise_power) * (np.power(10, -channel.snr / 20.0))
            self.sample = self.sample + noise * noise_scale
