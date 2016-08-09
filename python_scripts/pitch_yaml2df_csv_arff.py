### receives a yaml with a sound's pitchyinfft stats, returns pandas
# DataFrame including whichever list of stats is given 
# (available stats: mean, var, median)

import os, yaml, pandas as pd, numpy as np
#https://github.com/saurabhnagrecha/Pandas-to-ARFF
import pandas2arff

def pitch_yaml2df(pitch_ymlf,stats = ['median']):
    pitch_dict = {}
    pitch_df = pd.DataFrame()
    
    f = open(pitch_ymlf)
    pitch_dict = yaml.safe_load(f)
    f.close()

    for stat in stats:
        pitch_df['pitch_' + stat] = [round(pitch_dict['tonal']['pitch'][stat],4)]
        
    # convert DataFrame to csv and arff
    pitch_df.to_csv('str_pitch_gender.csv')
    pandas2arff.pandas2arff(pitch_df,filename='str_pitch_gender.arff',wekaname = 'gender')
    
    return pitch_df

