###### receives a speech sound clip (wav, mp3, ogg and flac formats tested)
###### and returns the speaker's gender (male/female)
### uses Essentia's out-of-the-box-extractors
# http://essentia.upf.edu/documentation/extractors/
# k-NN from scikit-learn ML library
# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
# uses sox to remove silence
# http://sox.sourceforge.net/

import os, yaml, subprocess, numpy as np
#pandas.pydata.org
import pandas as pd
#https://github.com/scikit-learn/scikit-learn/tree/master/sklearn/externals
from sklearn.externals import joblib

    
def speaker_gender(track):

    # remove silence longer than 0.1 second
    new_track = 'out.wav'
    os.system('sox {src} {dst} silence 1 0.1 0.1% reverse silence 1 0.1 0.1% reverse'.format(src = track,dst = new_track))

    # extract statistics of sound's PitchYINfft, MFCC and GFCC features into 
    # yaml files
    pitch_ymlf = new_track[:-4] + '_pitch.yaml'
    mfcc_ymlf = new_track[:-4] + '_mfcc.yaml'
    gfcc_ymlf = new_track[:-4] + '_gfcc.yaml'

    subprocess.call(['essentia_streaming_pitchyinfft',new_track,pitch_ymlf])
    subprocess.call(['essentia_streaming_mfcc',new_track,mfcc_ymlf])
    subprocess.call(['essentia_streaming_gfcc',new_track,gfcc_ymlf])
    os.remove(new_track)

    # convert yaml with PitchYINfft into pandas DataFrame,keeping only median
    # (just because for the task at hand is proven through feature selection
    # more relevant than the other two available measures - mean&var)
    pitch_dict = {}
    pitch_df = pd.DataFrame()

    f = open(pitch_ymlf)
    pitch_dict = yaml.safe_load(f)
    f.close()

    pitch_df['pitch_median'] = [round(pitch_dict['tonal']['pitch']['median'],4)]

    os.remove(pitch_ymlf)

    # convert yaml with MFCC into pandas DataFrame,keeping only mean and var
    # ALSO proceed to "flatten" values ---> one coefficient-one value
    mfcc_dict = {}
    mfcc_df = pd.DataFrame()

    f = open(mfcc_ymlf)
    mfcc_dict = yaml.safe_load(f)
    f.close()

    for i in range(13):
        mfcc_df['mfcc_mean_'+ str(i)] = [round(mfcc_dict['lowlevel']['mfcc']['mean'][i],4)]

    for i in range(13):
        mfcc_df['mfcc_var_'+ str(i)] = [round(mfcc_dict['lowlevel']['mfcc']['var'][i],4)]

    os.remove(mfcc_ymlf)

    # GFCC, same as in MFCC 
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
    
    os.remove(gfcc_ymlf)

    # concat all DataFrames into one
    df = pd.concat([mfcc_df,gfcc_df,pitch_df], axis=1)

    # FEATURE SELECTION: was ran elseplace (k=15 Best features using ANOVA F-value score function)
    # and the selected features corresponded to the DataFrames indices seen below
    chosen_feats_ind = np.array([ 3,  4, 11, 14, 24, 25, 30, 35, 37, 38, 46, 47, 48, 50, 51])
    df = df.iloc[:,chosen_feats_ind]
    X = np.array(df)

    # Load model
    model = joblib.load('kNN_clfr/kNN.pkl')

    #Predict
    predicted_gender = model.predict(X)[0]

    print 'The speaker is {g}'.format(g = predicted_gender)

    return predicted_gender