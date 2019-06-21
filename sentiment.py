from collections import tweepy
from collections import textblob
import matplotlib.pyplot as plt

accessKey = '832439082659770369-HuJC0xeXS5ZQAf0MOQCcjJk8PhKq8wl'
accessSecret ='c2esmijqjiMa6dDl3A1160soG7GFlNLAZkQb9PMw7Mjm9'
consumerKey = 'pDXSUr1z4ZjHiOYuPEbp4STY9'
consumerSecret = 'uRisLgAjCbOJ6KbvCxgqAfOSCUnif1LafuN8Grxgsye2P7AGju'

authentication=tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)

authentication.set_access_token(accessKey,accessSecret)

api=tweepy.API(authentication)

keyword=input('enter keyword')
numberOfTweets=int(input('enter no.of tweets'))

tweets=tweepy.Cursor(api.search, q=keyword, lang='en').items(numberOfTweets)

positive=negative=neutral=polarity=0

def calculatePercentage(a,b):
    return 100*float(a)/float(b)

for tweet in tweets:
    print(tweet.text)
    myAnalysis=textblob.TextBlob(tweet.text)
    polarity += myAnalysis.sentiment.polarity
    if myAnalysis.sentiment.polarity==0:
        neutral+=1
    elif myAnalysis.sentiment.polarity >0.00:
        positive+=1
    elif myAnalysis.sentiment.polarity < 0.00:
        negative+=1

positive=calculatePercentage(positive,numberOfTweets)
negative=calculatePercentage(negative,numberOfTweets)
neutral=calculatePercentage(neutral,numberOfTweets)

positive=format(positive,'-2f')
negative=format(negative,'-2f')
neutral=format(neutral,'-2f')

print('-------------------------------------------------------------')
if polarity>0:
    print("positive","\n")
elif polarity <0:
    print("negative","\n")
elif polarity ==0:
    print("neutral","\n")
    
labels=['Positive['+str(positive)+'%]','Negative['+str(negative)+'%]','Neutral['+str(neutral)+'%]']
sizes=[positive,negative,neutral]
color=['green','yellow','red']
patches,text=plt.pie(sizes,colors=color,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title('how people are reacting on'+keyword+'by analysing'+str(numberOfTweets)+'Tweets')
plt.axis('equal')
plt.tight_layout()
plt.show()

