### receives a yaml with a sound's mfcc stats, returns pandas
# DataFrame including only mean and var but "flattened" -->
# one coefficient - one value

import os, yaml, pandas as pd, numpy as np
#https://github.com/saurabhnagrecha/Pandas-to-ARFF
import pandas2arff

def mfcc_yaml2df(mfcc_ymlf):
    mfcc_dict = {}
    mfcc_df = pd.DataFrame()
    
    f = open(mfcc_ymlf)
    mfcc_dict = yaml.safe_load(f)
    f.close()

    for i in range(13):
        mfcc_df['mfcc_mean_'+ str(i)] = [round(mfcc_dict['lowlevel']['mfcc']['mean'][i],4)]

    for i in range(13):
        mfcc_df['mfcc_var_'+ str(i)] = [round(mfcc_dict['lowlevel']['mfcc']['var'][i],4)]

    # convert DataFrame to csv and arff
    pitch_df.to_csv('str_pitch_gender.csv')
    pandas2arff.pandas2arff(pitch_df,filename='str_pitch_gender.arff',wekaname = 'gender')
    
    return mfcc_df



