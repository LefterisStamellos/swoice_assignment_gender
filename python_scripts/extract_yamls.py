# http://essentia.upf.edu/documentation/extractors/
# is given a sound file (wav,mp3,ogg,flac formats tested)
# returns yaml files with stats on said sound's
# PitchYINfft, MFCC and GFCC features

import subprocess

def extract_yamls(track):

	pitch_ymlf = track[:-4] + '_pitch.yaml'
	mfcc_ymlf = track[:-4] + '_mfcc.yaml'
	gfcc_ymlf = track[:-4] + '_gfcc.yaml'

	subprocess.call(['essentia_streaming_pitchyinfft',track,pitch_ymlf])
	subprocess.call(['essentia_streaming_mfcc',track,mfcc_ymlf])
	subprocess.call(['essentia_streaming_gfcc',track,gfcc_ymlf])

	return 