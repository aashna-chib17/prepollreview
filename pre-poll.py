import tweepy  # for twitter Api
import matplotlib.pyplot as plt  # for graph ploting
from textblob import TextBlob  # for tweet analysis

# consumer key and secret given by twitter with API
consumer_key = "8tcSQzvzZLRA0ltJZ3XE4siMy"
consumer_secret = "wyiLbp1hQ5gYzANlPnlpr1SHDsK9ry8OquO1U348kWJQCBkyEp"

# Access token and secret given by twitter with API
access_token = "3163679389-Cf4OiF6Qs2UFfeXg7ACwSkJMNEircIfUrhJXUKg"
access_secret = "7Eld3oQpXgCMA01SBoTGJBlsJLhLhnoJ7SryXn7irGHVX"

# login in tweeter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# getting all tweet
api = tweepy.API(auth)

public_tweets = api.search('BJP')  # search all the tweet related to BJP
bjp = 0
y = 0
for tweet in public_tweets:  # loop for analysis each and every tweet
    analysis = TextBlob(tweet.text)  # analysis
    bjp = analysis.sentiment.polarity + bjp  # find polarity - Polarity in sentiment analysis refers to identifying sentiment orientation (positive, neutral, and negative) in written or spoken language.
    y = analysis.sentiment.subjectivity + y  # find subjectivity - Subjective expressions are opinions that describe people's feelings towards a specific subject or topic

print("BJP")
print(f"Polarity of  all tweets is : {bjp}")
print(f"Subjectivity of all tweets is : {y}")
print("")

public_tweets = api.search('Congress')
congress = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    congress = analysis.sentiment.polarity + congress
    y = analysis.sentiment.subjectivity + y

print("Congress")
print(f"Polarity of  all tweets is : {congress}")
print(f"Subjectivity of all tweets is : {y}")
print("")

public_tweets = api.search('AAP')
aap = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    aap = analysis.sentiment.polarity + aap
    y = analysis.sentiment.subjectivity + y
print("AAP")
print(f"Polarity of all tweets is : {aap}")
print(f"Subjectivity of all tweets is : {y}")
print("")

public_tweets = api.search('SHIV SENA')
shiv_sena = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    shiv_sena = analysis.sentiment.polarity + shiv_sena
    y = analysis.sentiment.subjectivity + y

print("SHIV SENA")
print(f"Polarity of  all tweets is : {shiv_sena}")
print(f"Subjectivity of all tweets is : {y}")
print("")

public_tweets = api.search('NPP')
npp = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    npp = analysis.sentiment.polarity + npp
    y = analysis.sentiment.subjectivity + y
print("NPP")
print(f"Polarity of all tweets is : {npp}")
print(f"Subjectivity of all tweets is : {y}")
print("")

left = [1, 2, 3, 4, 5]  # list of number of parties

height = [bjp, congress, aap, shiv_sena, npp]  # list of parties

tick_label = ['BJP', 'CONGRESS', 'AAP', 'SHIV SENA', 'NPP']  # title label

plt.bar(left, height, tick_label=tick_label, width=0.5, color=['black', 'red'])  # plot graph

plt.xlabel('Political parties')  # label
plt.ylabel('Polarity')  # label

plt.title('My bar chart!')  # chart title

plt.show()  # show

public_tweets = api.search('Narendra Modi')
a = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    a = analysis.sentiment.polarity + a
    y = analysis.sentiment.subjectivity + y

print("Narendra Modi")
print(f"Polarity of  all tweets is : {a}")
print(f"Subjectivity of all tweets is : {y}")
print("")

public_tweets = api.search('Rahul Gandhi')
t = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    t = analysis.sentiment.polarity + t
    y = analysis.sentiment.subjectivity + y

print("Rahul Gandhi")
print(f"Polarity of  all tweets is : {t}")
print(f"Subjectivity of all tweets is : {y}")
print("")

public_tweets = api.search('Arvind Kejriwal')
h = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    h = analysis.sentiment.polarity + h
    y = analysis.sentiment.subjectivity + y
print("Arvind Kejriwal")
print(f"Polarity of all tweets is : {h}")
print(f"Subjectivity of all tweets is : {y}")
print("")

public_tweets = api.search('Lalu Prasad Yadav')
c = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    c = analysis.sentiment.polarity + c
    y = analysis.sentiment.subjectivity + y

print("Lalu Prasad Yadav")
print(f"Polarity of  all tweets is : {c}")
print(f"Subjectivity of all tweets is : {y}")
print("")

public_tweets = api.search('Akhilesh yadav')
d = 0
y = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    d = analysis.sentiment.polarity + d
    y = analysis.sentiment.subjectivity + y
print("Akhilesh yadav")
print(f"Polarity of all tweets is : {d}")
print(f"Subjectivity of all tweets is : {y}")
print("")

left = [1, 2, 3, 4, 5]

height = [a, t, h, c, d]

tick_label = ['Narendra Modi', 'Rahul Gandhi', 'Arvind Kejriwal', 'Lalu Prashad Yadav', 'Akhilesh yadav']

plt.bar(left, height, tick_label=tick_label, width=0.5, color=['black', 'red'])

plt.xlabel('Types of TV shows')
plt.ylabel('Polarity')

plt.title('My bar chart!')

plt.show()