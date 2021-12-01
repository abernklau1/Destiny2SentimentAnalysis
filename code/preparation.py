from sklearn.feature_extraction.text import CountVectorizer
from nltk import sent_tokenize
from nltk import word_tokenize
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from textblob import TextBlob



def top_n_gram(corpus,ngram_range,n=None):

    #Vectorize corpus
    vec = CountVectorizer(ngram_range=ngram_range, stop_words='english', max_df=1.0, min_df=0.01).fit(corpus)

    #creates bag of words and finds the sums of words
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    
    #creates a list of words and their frequencies
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)

    return words_freq[:n], bag_of_words


def top_n_gram_test(corpus, trained_corpus, ngram_range,n=None):

    #Vectorize corpus
    vec = CountVectorizer(ngram_range=ngram_range, stop_words='english', max_df=1.0, min_df=0.01).fit(trained_corpus)

    #Create bag of words and the sums
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 

    #Create a list of words and their frequencies
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n], bag_of_words

#Function to clean tweets of urls, punctuation and uppercase letters
def clean_tweets(dataframe):

    #Lambda function to remove urls from tweets providing links
    remove_url = lambda tweet: re.sub(r'http\S+', '', tweet)

    #Lambda function to remove punctuation from tweets
    remove_punct = lambda tweet: re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+://\S+)"," ", tweet)

    #Remove urls and punctuation from text column
    dataframe["clean_text"] = dataframe.text.map(remove_url).map(remove_punct)

    #Reduce text to lowercase format
    dataframe["clean_text"] = dataframe.clean_text.str.lower()

    return dataframe

#Calculating Negative, Positive 
def create_sentiment_neu(dataframe):
    df_probs = pd.DataFrame()

    #create dataframe of subjectivity and subjectivity polarity of tweets
    df_probs[['polarity', 'subjectivity']] = dataframe['clean_text'].apply(lambda text: pd.Series(TextBlob(text).sentiment))

    #Scores each tweet based on the subjectivity polarity
    for index, row in dataframe['text'].iteritems():

        #Provides negative, neutral, positive and compound scores for the tweet in that row
        score = SentimentIntensityAnalyzer().polarity_scores(row)

        #extracts negative and positive scores
        neg = score['neg']
        pos = score['pos']
        neu = score['neu']
        
        #creates binary values based on which sentiment score is higher 
        if neg > pos and neg > neu:
            df_probs.loc[index, 'sentiment'] = 0
        elif pos > neg and pos > neu:
            df_probs.loc[index, 'sentiment'] = 1
        elif neu > neg and neu > pos:
            df_probs.loc[index, 'sentiment'] = 2
            
    return df_probs

def create_sentiment(dataframe):
    df_probs = pd.DataFrame()

    #create dataframe of subjectivity and subjectivity polarity of tweets
    df_probs[['polarity', 'subjectivity']] = dataframe['clean_text'].apply(lambda text: pd.Series(TextBlob(text).sentiment))

    #Scores each tweet based on the subjectivity polarity
    for index, row in dataframe['text'].iteritems():

        #Provides negative, neutral, positive and compound scores for the tweet in that row
        score = SentimentIntensityAnalyzer().polarity_scores(row)

        #extracts negative and positive scores
        neg = score['neg']
        pos = score['pos']
        
        #creates binary values based on which sentiment score is higher 
        if neg > pos:
            df_probs.loc[index, 'sentiment'] = 0
        elif pos > neg:
            df_probs.loc[index, 'sentiment'] = 1
        else:
            df_probs.loc[index, 'sentiment'] = 0
            
    return df_probs

#Creates a dataframe of the neutral tweets and matches their sentiment values
def create_neu_df(dataframe, dataframe_probs):

    #Grabs text from original dataframe 
    dataframe.reset_index(drop=True, inplace=True)
    df_pos = dataframe[['text']].copy(deep=True)

    #Grabs sentiment values from probs dataframe
    dataframe_probs.reset_index(drop=True, inplace=True)
    df_pos['sentiment'] = dataframe_probs['sentiment'].copy(deep=True)

    #Creates dataframe of only positive sentiment tweets
    df_pos = df_pos[df_pos['sentiment'] == 2]
    
    return df_pos

#Creates a dataframe of the positive tweets and matches their sentiment values
def create_pos_df(dataframe, dataframe_probs):

    #Grabs text from original dataframe 
    dataframe.reset_index(drop=True, inplace=True)
    df_pos = dataframe[['text']].copy(deep=True)

    #Grabs sentiment values from probs dataframe
    dataframe_probs.reset_index(drop=True, inplace=True)
    df_pos['sentiment'] = dataframe_probs['sentiment'].copy(deep=True)

    #Creates dataframe of only positive sentiment tweets
    df_pos = df_pos[df_pos['sentiment'] == 1]
    
    return df_pos

#Creates a dataframe of the negative tweets and matches their sentiment values
def create_neg_df(dataframe, dataframe_probs):

    #Grabs text from original dataframe 
    dataframe.reset_index(drop=True, inplace=True)
    df_neg = dataframe[['text']].copy(deep=True)

    #Grabs sentiment values from probs dataframe
    dataframe_probs.reset_index(drop=True, inplace=True)
    df_neg['sentiment'] = dataframe_probs['sentiment'].copy(deep=True)

    #Creates dataframe of only positive sentiment tweets
    df_neg = df_neg[df_neg['sentiment'] == 0]
    
    return df_neg

def create_neu_df(dataframe, dataframe_probs):

    #Grabs text from original dataframe 
    dataframe.reset_index(drop=True, inplace=True)
    df_neu = dataframe[['text']].copy(deep=True)

    #Grabs sentiment values from probs dataframe
    dataframe_probs.reset_index(drop=True, inplace=True)
    df_neu['sentiment'] = dataframe_probs['sentiment'].copy(deep=True)

    #Creates dataframe of only positive sentiment tweets
    df_pos = df_neu[df_neu['sentiment'] == 2]
    
    return df_pos

def create_features(text, top_words):
    features = {}
    wordcount = 0

    #Adds 1 to wordcount if word in tokenized text is within the top list of words
    for sentence in sent_tokenize(text):
        for word in word_tokenize(sentence):
            if word.lower() in top_words:
                wordcount += 1

    #adds wordcount to dictionary
    features["wordcount"] = wordcount

    return features['wordcount']