#### script for extracting yaml files with stats on PitchYINfft, GFCC and MFCC
# features of all wav files (training set)
# features are extrcted using Essentia's out-of-the-box extractors:
# http://essentia.upf.edu/documentation/extractors/
# yamls are extracted in separate folder, this will be more convenient later
import os, yaml, subprocess

#folder with training data (wav files)
srcdir = 'female_male_wav'

feats = ['pitchyinfft','mfcc','gfcc']

for feat in feats:
	dstdir = 'female_male_streaming_' + feat
	os.mkdir(dstdir)
	tracks = [track for track in os.listdir(srcdir) if (track[-3:] == 'wav' or track[-3:] == 'WAV')]
	for track in tracks:
		subprocess.Popen(['essentia_streaming_' + feat,os.path.join(srcdir,track),os.path.join(dstdir,track[:-4] + '.yaml')])
