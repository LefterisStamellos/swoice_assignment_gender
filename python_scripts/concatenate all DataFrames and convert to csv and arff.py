import pandas as pd
#https://github.com/saurabhnagrecha/Pandas-to-ARFF
import pandas2arff

#read csvs with feature values to DataFrames and concatenate to one combined DataFrame
mfcc_df = pd.read_csv('str_mfcc_gender.csv').iloc[:,1:-1]
gfcc_df = pd.read_csv('str_gfcc_gender.csv').iloc[:,1:-1]
pitch_df = pd.read_csv('str_pitch_gender.csv').iloc[:,1:]
df = pd.concat([mfcc_df,gfcc_df,pitch_df], axis=1)

#convert DataFrame with all feature values to csv and arff 
df.to_csv('str_mfcc_and_gfcc_and_pitch_gender.csv')
pandas2arff.pandas2arff(df,filename='str_mfcc_and_gfcc_and_pitch_gender.arff',wekaname = 'gender')