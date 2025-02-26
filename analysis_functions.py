import numpy as np
import pandas as pd

def g2(channels_dict, normalize:bool=True):
    """
    Calculate the second order correlation function g2 from the channels_dict dictionary. 
    Args: channels_dict(dictionary): The dictionary should contain the channels as keys and the data ad PandaDataframes as values.
          normalize(bool): If True, the g2 is normalized by the product of the mean intensities of the two channels. Default is True.  
    """
    mean_dict = {}
    #compute the temporal mean of each channel signal (axis=1 is the time axis)
    for channel in channels_dict:
        mean_dict[channel] = np.mean(channels_dict[channel], axis=1)


    time_interval=channels_dict['Ch1'].shape[1] #channels_dict['Ch2'].shape[1]

    #compute the intensity product
    intensity_product=np.sum(channels_dict['Ch1'] * channels_dict['Ch2'], axis=1)/time_interval

    mean_product = mean_dict['Ch1'] * mean_dict['Ch2']

    if normalize:
        g2 = intensity_product/mean_product
    else:   
        g2 = intensity_product

    return g2


def gaussian(x, A, mu, sigma):
    return 1 + A * np.exp(- (x - mu)**2 / (2 * sigma**2))
