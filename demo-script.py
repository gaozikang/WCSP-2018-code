#!/usr/bin/python3
import amcgen
import amctest
import amcout
import amcmethod


#Define channel and generate signal
channel = amcgen.Channel(['awgn'], -10, (2, 4), 0, 0)
signal = amcgen.Signal('4qam', 1024, 'random')

signal.applychannel(channel)

#Plot signal constellation
figure_title = amcout.nameconvert(signal.modulation_type)
amcout.constplot(signal.sample, figure_title)

# Classify signal modulatin
# test = amctest.Test()
# test.modulation_pool = ['2psk', '4psk', '4qam', '16qam']  # Define modulation candidates
# print("Testing Signal:", amcout.nameconvert(signal.modulation_type))
# print("Testing Channel:", channel.type)
# print("AMC Method: amcml")
# decision = amcmethod.amcml(signal, channel, test)
# print("Classification Result:", amcout.nameconvert(test.modulation_pool[decision]))
# if test.modulation_pool[decision] == signal.modulation_type:
    # print("Classification is successful!\n")
# else:
    # print("Classification failed.\n")
