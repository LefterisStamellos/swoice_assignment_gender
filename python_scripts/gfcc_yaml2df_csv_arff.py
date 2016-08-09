### receives a yaml with a sound's gfcc stats, returns pandas
# DataFrame including only mean and var but "flattened" -->
# one coefficient - one value 

import os, yaml, subprocess, pandas as pd, numpy as np
#https://github.com/saurabhnagrecha/Pandas-to-ARFF
import pandas2arff

def gfcc_yaml2df(gfcc_ymlf):
    gfcc_dict = {}
    gfcc_df = pd.DataFrame()        

    f = open(gfcc_ymlf)
    gfcc_dict = yaml.safe_load(f)
    f.close()

    for i in range(13):
        gfcc_arr = np.array([])
        for j in range(len(gfcc_dict['lowlevel']['gfcc'])):
            gfcc_arr = np.append(gfcc_arr,gfcc_dict['lowlevel']['gfcc'][j][i])
            gfcc_df['gfcc_mean_'+ str(i)] = [round(np.mean(gfcc_arr),4)]

    for i in range(13):
        gfcc_arr = np.array([])
        for j in range(len(gfcc_dict['lowlevel']['gfcc'])):
            gfcc_arr = np.append(gfcc_arr,gfcc_dict['lowlevel']['gfcc'][j][i])
            gfcc_df['gfcc_var_'+ str(i)] = [round(np.var(gfcc_arr),4)]

    # convert DataFrame to csv and arff
    pitch_df.to_csv('str_pitch_gender.csv')
    pandas2arff.pandas2arff(pitch_df,filename='str_pitch_gender.arff',wekaname = 'gender')
    
    return gfcc_df


