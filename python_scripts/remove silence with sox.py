import os

#directory of wavs with silence
srcdir = 'all_eq'
#target directory - for wavs without silence
dstdir = 'all'

tracks = [track for track in os.listdir(srcdir) if (track[-3:] == 'wav' or track[-3:] == 'WAV')]
for track in tracks:
    os.system('sox {src} {dst} silence 1 0.1 0.1% reverse silence 1 0.1 0.1% reverse'.format(src = os.path.join(srcdir,track),dst = os.path.join(dstdir,track)))