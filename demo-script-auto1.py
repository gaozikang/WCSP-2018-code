#!/usr/bin/python3
import amcgen
import amctest
import amcout
import amcmethod

modulation_type = ['2psk','4psk','4qam','16qam']
for modulation in modulation_type:
    print("Testing Signal:", amcout.nameconvert(modulation))
    for snr in range(-4,-3):
        channel = amcgen.Channel(['awgn'], snr, (2, 4), 0, 0)
        # correct_num = 0
        a = 0
        b = 0
        c = 0
        d = 0
        iteration_num = 10
        while iteration_num > 0:
            signal = amcgen.Signal(modulation, 16, 'random')
            signal.applychannel(channel)
            # Classify signal modulatin
            test = amctest.Test()
            test.modulation_pool = ['2psk','4psk','4qam','16qam']  # Define modulation candidates
            # print("Testing Channel:", channel.type)
            # print("AMC Method: amcml")
            decision, x_I = amcmethod.amcks_Q(signal, channel, test)
            iteration_num = iteration_num - 1
            if test.modulation_pool[decision] == '2psk':
                a = a + 1
            elif test.modulation_pool[decision] == '4psk':
                b = b + 1
            elif test.modulation_pool[decision] == '4qam':
                c = c + 1
            elif test.modulation_pool[decision] == '16qam':
                d = d + 1
            # print("Classification Result:", amcout.nameconvert(test.modulation_pool[decision]))
            # if test.modulation_pool[decision] == signal.modulation_type:
                # correct_num = correct_num + 1
                # print("Classification is successful!\n")
                # else:
                    # print("Classification failed.\n")
        # print(a,b,c,d)
