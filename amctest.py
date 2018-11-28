import numpy as np


class Test(object):
    """declaration for class Test"""

    def __init__(self, modulation_pool=['2psk', '4psk', '4qam', '16qam']):
        self.modulation_pool = modulation_pool

    def getsymbolmap(self, modulation_type):
        "GETALPHABET    Generate set of alphabet according to modulation type."
        # Create basic mapping of signal symbols
        if modulation_type == '2pam':
            symbol_map = np.array([1, -1])
        elif modulation_type == '4pam':
            symbol_map = np.array([-3, -1, 1, 3])
        elif modulation_type == '8pam':
            symbol_map = np.array([-7, -5, -3, -1, 1, 3, 5, 7])
        elif modulation_type == '2psk':
            symbol_map = np.array([1j, -1j])
        elif modulation_type == '4psk':
            symbol_map = np.array([1, 1j, -1, -1j])
        elif modulation_type == '8psk':
            symbol_map = np.array([1.4142, 1 + 1j, 1.4142j, -1 + 1j,
                                   -1.4142, -1 - 1j, -1.4142j, 1 - 1j])
        elif modulation_type == '4qam':
            symbol_map = np.array([1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j])
        elif modulation_type == '16qam':
            symbol_map = np.array([3 + 3j, 3 + 1j, 3 - 1j, 3 - 3j, 1 + 3j, 1 + 1j, 1 - 1j,
                                   1 - 3j, -1 + 3j, -1 + 1j, -1 - 1j, -1 - 3j, -3 + 3j, -3 + 1j, -3 - 1j, -3 - 3j])
        elif modulation_type == '64qam':
            symbol_map = np.array([1 + 1j, 3 + 1j, 1 + 3j, 3 + 3j, 7 + 1j, 5 + 1j, 7 + 3j,
                                   5 + 3j, 1 + 7j, 3 + 7j, 1 + 5j, 3 + 5j, 7 + 7j, 5 + 7j, 7 + 5j, 5 + 5j, 1 - 1j,
                                   1 - 3j, 3 - 1j, 3 - 3j, 1 - 7j, 1 - 5j, 3 - 7j, 3 - 5j, 7 - 1j, 7 - 3j, 5 - 1j,
                                   5 - 3j, 7 - 7j, 7 - 5j, 5 - 7j, 5 - 5j, -1 + 1j, -1 + 3j, -3 + 1j, -3 + 3j,
                                   -1 + 7j, -1 + 5j, -3 + 7j, -3 + 5j, -7 + 1j, -7 + 3j, -5 + 1j, -5 + 3j,
                                   -7 + 7j, -7 + 5j, -5 + 7j, -5 + 5j, -1 - 1j, -3 - 1j, -1 - 3j, -3 - 3j,
                                   -7 - 1j, -5 - 1j, -7 - 3j, -5 - 3j, -1 - 7j, -3 - 7j, -1 - 5j, -3 - 5j,
                                   -7 - 7j, -5 - 7j, -7 - 5j, -5 - 5j])
        elif modulation_type == '256qam':
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
        return symbol_map

    def demo(self, signal, channel):
        print("Testing Signal:", amcout.nameconvert(signal.modulation_type))
        print("Testing Channel:", channel.type)
        print("AMC Method: amcml")
        decision = amcmethod.amcml(signal, channel, test)
        print("Classification Result:", amcout.nameconvert(test.modulation_pool[decision]))
        if test.modulation_pool[decision] == signal.modulation_type:
            print("Classification is successful!\n")
        else:
            print("Classification failed.\n")
