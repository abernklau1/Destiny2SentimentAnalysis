import tweepy
import csv
import time

# Authentication
def authenticate(consumer_key, consumer_secret, access_token, access_secret):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth)

def append_to_csv(tweets, fileName):

    #A counter variable
    counter = 0

    #Open OR create the target CSV file
    csvFile = open(fileName, "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    #Loop through each tweet
    for tweet in tweets:
        
        # variable created for each aspect since some of the keys might not exist for some tweets
        # So we will account for that

        # 1. ID
        id = tweet.id

        # 2. Time created
        created_at = tweet.created_at

        # 4. Language
        lang = tweet.lang

        # 5. Tweet metrics
        retweet_count = tweet.retweet_count
        like_count = tweet.favorite_count

        # 6. Tweet text
        text = tweet.text
        
        # Assemble all data in a list
        res = [id, created_at, lang, like_count, retweet_count, text]
        
        # Append the result to the CSV file
        csvWriter.writerow(res)
        counter += 1

    # When done, close the CSV file
    csvFile.close()

    # Print the number of tweets for this iteration
    print("# of Tweets added from this response: ", counter)


def scrape_and_place(api):

    #Ask for keyword with which to scrape.
    keyword = input('Please enter keyword or hastag to search: ')

    #Ask for number of tweets desired to scrape.
    tweet_num = int(input('Please enter how many tweets to analyze (If greater than 900, must be multiple of 900): '))

    #Ask for date at which access was requested as the scrape can only occur on tweets made within seven days prior to requested date.
    date_req = input('Please enter the date from which you request YYYY/MM/DD: ')
    date_req = date_req.split('/')

    j = 0

    #Only 900 tweets can be scraped every 15min so if desired amount is greater than 900 this will create a wait time to pull every 15 min.
    if tweet_num > 900:

        for i in range(0, tweet_num//900):
            if j == 7:
                break
            elif j != 7:
                tweets = tweepy.Cursor(api.search_tweets, q=keyword+' lang:en -filter:retweets', until=date_req[0] + '-' + date_req[1] + '-' + str((int(date_req[2]) - j))).items(900)
            j += 1
            append_to_csv(tweets, fileName='data.csv')
            time.sleep(900)

    elif tweet_num <= 900 & tweet_num > 0:
 
        tweets = tweepy.Cursor(api.search_tweets, q=keyword+' lang:en -filter:retweets', until=date_req[0] + '-' + date_req[1] + '-' + date_req[2]).items(tweet_num)
        append_to_csv(tweets, fileName='data.csv')
