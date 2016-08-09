######## Download chosen speech sound clips from Voxforge ######## 

from bs4 import BeautifulSoup,urllib, os, from shutil import copyfile

url_index = 'http://www.repository.voxforge1.org/downloads/'

r = urllib.urlopen(url_index).read()
soup = BeautifulSoup(r,'html.parser')

# chosen dialects
dialects = ['bg','de','el','es','fa','fr','it','tr','uk']
url_dialects = [x.string for x in soup.find_all('a') if x.string[:-1] in dialects]

# url with compressed wav files
url_downloadables = 'Trunk/Audio/Main/16kHz_16bit/'

#download tgz files
for d in url_dialects:
    url = url_index + d + url_downloadables
	r = urllib.urlopen(url).read()
	soup = BeautifulSoup(r,'html.parser')
	for link in soup.find_all('a'):
	    f = link.get('href')
	    if f[-3:] == 'tgz':
	        testfile = urllib.URLopener()
	        testfile.retrieve(url + f,f)

##################################################################
# downloaded tgz files were manually decompressed in 'female' dir
# the belofolder script copy-pastes included wavs to a common 
# 'all_female' dir, adding 'female_' in filename

pardir = "female"
folders = os.listdir(pardir)

for f in folders:
    srcdir = os.path.join(pardir,f,'wav')
    tracks = [x for x in os.listdir(srcdir) if x[-3:] == 'wav']
    for track in tracks:
        src = os.path.join(srcdir,track)
        dst = os.path.join(os.curdir,'female_all','female_' + track[:-4] + '_' + f[:3] + track[-4:])
        copyfile(src,dst)

# same as above for male

pardir = "male"
folders = os.listdir(pardir)[1:]

for f in folders:
    srcdir = os.path.join(pardir,f,'wav')
    tracks = [x for x in os.listdir(srcdir) if x[-3:] == 'wav']
    for track in tracks:
        src = os.path.join(srcdir,track)
        if track[:2] in os.listdir(os.path.join(os.curdir,'male_all')):
            dst = os.path.join(os.curdir,'male_all',track[:2],'male_' + track[:-4] + '_' + f[:3] + track[-4:])
        else:
            dst = os.path.join(os.curdir,'male_all','male_' + track[:-4] + '_' + f[:3] + track[-4:])
        copyfile(src,dst)
