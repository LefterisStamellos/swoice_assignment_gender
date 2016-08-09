# Swoice Task Assignment Pt.1: Gender of Voice  
The aim of this project is to implement a system capable of specifying a speaker's gender from his/her voice.  
In ipython it should work as follows:  
import predict_gender  
predict_gender.speaker_gender(yourFile)     (wav, mp3, ogg and flac formats have been tested)  
## Dataset
The system was trained using data from [www.voxforge.org](http://www.voxforge.org/).  
From the available speech clips, a selection of bulgarian, german, greek, spanish, farsi, french, italian, turkish and ukranian speakers
of both male and female gender was made. Speakers appear to be reciting passages from some script or another.   
The two sets are balanced (580 clips under the male category, same number for female).  
An equal loudness filter is applied and silence intervals longer than 0.1 second are removed.  
Resulting dataset can be found [here](https://www.dropbox.com/home/female_male_wav)
## Tools
Data scrapping: urlib, [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
Sound Processing: [SoX](http://sox.sourceforge.net/)  
Feature Extraction: [Essentia out-of-the-box extractors](http://essentia.upf.edu/documentation/extractors/)  
Data Curation: [pandas](http://pandas.pydata.org/)  
pandas DataFrame to arff (for experimenting with [Weka](http://www.cs.waikato.ac.nz/ml/weka/)): [pandas2arff](https://github.com/saurabhnagrecha/Pandas-to-ARFF)  
Feature Selection and System Building: [scikit-learn](http://scikit-learn.org/stable/)  
## Algorithms
Feature selection was made using ANOVA F-values of features. The 15 Best scoring were kept.  
Classifier was built using k Nearest Neighbors, with k=1 and Manhattan distance metric. Choice of algorithm was based simply
 on comparing accuracy rates (calculated with 10-fold cross validation) of different techniques.  
 Except from kNN, SVM (linear and rbf kernel), Random Forest, Decision Tree and Naïve Bayes based classifiers were tested. kNN scored highest with an accuracy rate calculated at about 89% with the 15 abovementioned features.  
## To do
 1) Extend dataset    
 The used dataset was built with spoken language diversity in mind. Additions could be: varying emotions, single phonems, 'extreme' cases (e.g. too low female, too high male)...  
 2) More features  
 Features used were Mel Frequency Cepstral Coefficients(MFCC), Gammatone Feature Cepstral Coefficients(GFCC) and the Fundamental Frequency using the YinFFT algorithm (PitchYinFFT). Those were chosen because they made the most sence among the available, given the used tool. Different libraries/extractors could give provide features.  
 .  
 .  
 .
 
