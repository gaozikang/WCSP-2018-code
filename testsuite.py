#!/usr/bin/python3
import numpy as np
import amcgen
import amcmethod

# Testing maximum likelihood classifier for SISO awgn signal
modulation_pool = ['2psk', '4qam', '16qam', '64qam']
snr_pool = range(-5, 20)
realization_num = 1024
sample_num = 1000

# Set default channel paraters
channel = amcgen.Channel()
channel.channel_type = ['awgn', 'fading']
channel.antenna_size = (1, 1)
channel.snr = 10
channel.phase_off = np.pi * 0
channel.freq_off = 0.000

# # Generate and save testing signal
# for i_modulation in range(len(modulation_pool)):
#     for i_snr in range(len(snr_pool)):
#         channel.snr = snr_pool[i_snr]
#         signal = amcgen.genmodsig(modulation_pool[i_modulation], sample_num, 'random')

# Create result matrix
mean_results = np.zeros([len(snr_pool), len(modulation_pool)])

# Perform iterative testing process
for i_modulation in range(len(modulation_pool)):
    for i_snr in range(len(snr_pool)):
        realization_decision = np.empty([realization_num, 1])
        realization_result = np.zeros([realization_num, 1])
        # Define channel parameters
        channel = amcgen.Channel()
        channel.channel_type = ['awgn', 'fading']
        channel.snr = snr_pool[i_snr]
        channel.phase_off = np.pi * 0
        channel.freq_off = 0.000
        # Generate testing signal
        signal = amcgen.genmodsig(modulation_pool[i_modulation], sample_num,
                                  'random')
        for i_realization in range(realization_num):
            # SISO or MIMO system
            if channel.antenna_size != (1, 1):  # if apply mimo configuration
                signal.sample, channel.matrix = amcgen.mimo(
                    signal.sample, channel.antenna_size)
            # Apply channel effects
            if 'fading' in channel.channel_type:  # if apply fading channel
                signal.sample = amcgen.fading(signal.sample, channel)
            if 'awgn' in channel.channel_type:  # if apply additive white gaussian noise
                signal.sample = amcgen.awgn(signal.sample, channel.snr)
            # Classify the current signal realization
            realization_decision[i_realization] = amcmethod.amcml(
                signal.sample, modulation_pool, channel)
            if modulation_pool[realization_decision[i_realization, 0].astype(
                    int)] == modulation_pool[i_modulation]:
                realization_result[i_realization] = 1
        mean_results[i_snr, i_modulation] = realization_result.mean()

print(mean_results)
