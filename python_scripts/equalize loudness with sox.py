import os

#directory of wavs before equal loudness filter application
srcdir = 'all'
#target directory - for wavs of equal loudness
dstdir = 'all_eq'

tracks = [track for track in os.listdir(srcdir) if (track[-3:] == 'wav' or track[-3:] == 'WAV')]
for track in tracks:
    os.system('sox {src} {dst} gain -n -3'.format(src = os.path.join(srcdir,track),dst = os.path.join(dstdir,track)))

