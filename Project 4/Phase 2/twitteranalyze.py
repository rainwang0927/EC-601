# install the libraries, use tweepy to gather the tweet data
import tweepy
# We will use the nltk and regex libraries to help us in this process.
import re

from telegram.ext import Updater, MessageHandler, Filters
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from datetime import datetime, timedelta
# We will use the nltk and regex libraries to help us in this process.
from nltk.tokenize import WordPunctTokenizer

# use your own Twitter API Keys
ACC_TOKEN = 'TOKEN'
ACC_SECRET = 'TOKEN'
CONS_KEY = 'TOKEN'
CONS_SECRET = 'TOKEN'

# Make a function called 'authentication' to connect to the API, with four parameters which are all of the keys.
def authentication(cons_key, cons_secret, acc_token, acc_secret):
    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(acc_token, acc_secret)
    api = tweepy.API(auth)
    return api

# we want to gather the tweets from the last 24 hours with maximum tweets of 50  
def search_tweets(keyword, total_tweets):
    today_datetime = datetime.today().now()
    yesterday_datetime = today_datetime - timedelta(days=1)
    today_date = today_datetime.strftime('%Y-%m-%d')
    yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')
# Connect to the Twitter API using a function we defined before.
    api = authentication(CONS_KEY,CONS_SECRET,ACC_TOKEN,ACC_SECRET)
    search_result = tweepy.Cursor(api.search, 
                                  q=keyword, 
                                  since=yesterday_date, 
                                  result_type='recent', 
                                  lang='en').items(total_tweets)
    return search_result

# We will use the nltk and regex libraries to help us in this process.
# Remove the username, links, numbers in every tweet
# Convert all of the characters into lower space, then remove every unnecessary space
def clean_tweets(tweet):
    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
    lower_case_tweet= number_removed.lower()
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()
    return clean_tweet

# Make a function called 'get_sentiment_score' which takes 'tweet' as the parameter, and returns the 'sentiment' score.
def get_sentiment_score(tweet):
    client = language.LanguageServiceClient()
    document = types\
               .Document(content=tweet,
                         type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
                      .analyze_sentiment(document=document)\
                      .document_sentiment\
                      .score
    return sentiment_score

# Calculate the average score and pass it to 'final_score' variable. Wrap all of the codes into 'analyze_tweets' function, with 'keyword' and 'total_tweets' as the parameters.
def analyze_tweets(keyword, total_tweets):
    score = 0
    tweets = search_tweets(keyword,total_tweets)
    for tweet in tweets:
        cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
        sentiment_score = get_sentiment_score(cleaned_tweet)
        score += sentiment_score
        print('Tweet: {}'.format(cleaned_tweet))
        print('Score: {}\n'.format(sentiment_score))
    final_score = round((score / float(total_tweets)),2)
    return final_score

# Wrap the codes into a function called 'send_the_result'.
def send_the_result(bot, update):
    keyword = update.message.text
    final_score = analyze_tweets(keyword, 50)
    if final_score <= -0.25:
        status = 'NEGATIVE ❌'
    elif final_score <= 0.25:
        status = 'NEUTRAL ='
    else:
        status = 'POSITIVE ✅'
        
 # Send the final_score and the status through Telegram Bot.       
    bot.send_message(chat_id=update.message.chat_id,
                     text='Average score for '
                           + str(keyword) 
                           + ' is ' 
                           + str(final_score) 
                           + ' ' 
                           + status)

# create another function called main to run our program.
def main():
    updater = Updater('Enter bot_Token', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, send_the_result))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
