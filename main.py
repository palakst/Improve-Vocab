#imported pandas to read the dataset
import pandas as pd

from plyer import notification
import time
"""
vocabulary dataset source was https://www.admitkard.com/blog/2019/12/26/50-new-english-words-with-meaning-and-sentences/
word and meanings were converted into a csv file
"""

vocabulary=pd.read_csv('vocab.csv')
word=vocabulary.iloc[:,0]
meaning=vocabulary.iloc[:,1]


for i in range(150):
    notification.notify(title=word[i], message=meaning[i], app_name="Learn new words!!!", timeout=10, ticker="Word of the Hour")
    time.sleep(3600)