import os
import re
import pandas as pd

def sort_csv_for_channel(data_path):
    # Lista per memorizzare i file per ogni canale
    channels = {'Ch1': [], 'Ch2': []}
    
    # Regex per estrarre il numero e il canale dal nome del file
    pattern = re.compile(r'([+-]?\d+)_Ch(\d)\.csv')
    
    # Itera attraverso i file nella cartella
    for filename in os.listdir(data_path):
        match = pattern.match(filename)
        if match:
            displacement = int(match.group(1))
            channel = f'Ch{match.group(2)}'
            channels[channel].append((displacement, filename))
    
    # Ordina i file per numero per ogni canale
    for channel in channels:
        channels[channel].sort()
        channels[channel] = [filename for _, filename in channels[channel]]
    return channels


def get_data_from_csv(filename, base_path:str=r'Quantum-Imaging\HBT_data'):
    file_path = os.path.join(base_path, filename)
    print(file_path)
    df=pd.read_csv(file_path, header=None)
    df=df.iloc[:,-2:] #select only the last two columns
    df.columns = ['Time', 'Intensity'] #change name only to the last two columns

    return df

def make_datasets(channels):
    dataset = {}
    for channel in channels:
        data = {int(re.match(r'([+-]?\d+)_Ch\d\.csv', filename).group(1)): get_data_from_csv(filename)['Intensity'] for filename in channels[channel]}
        dataset[channel] = pd.DataFrame.from_dict(data, orient='index')

    return dataset

