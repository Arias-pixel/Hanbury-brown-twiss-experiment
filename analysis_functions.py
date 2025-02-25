
import numpy as np
import pandas as pd

def g2(channels_dict, normalize:bool=True):
    mean_dict = {}
    for channel in channels_dict:
        mean_dict[channel] = np.mean(channels_dict[channel], axis=1)

    intensity_product=np.sum(channels_dict['Ch1'] * channels_dict['Ch2'], axis=1)/channels_dict['Ch1'].shape[1]
    mean_product = mean_dict['Ch1'] * mean_dict['Ch2']

    if normalize:
        g2 = intensity_product/mean_product
    else:   
        g2 = intensity_product

    return g2

def gaussian(x, A, mu, sigma):
    return A * np.exp(- (x - mu)**2 / (2 * sigma**2))
