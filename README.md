# Destiny 2 Community Sentiment Analysis

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages7.alphacoders.com%2F112%2Fthumb-1920-1126860.jpg&f=1&nofb=1" width="500">

## Business Problem

Destiny 2 has been successful in its ability to create a story that entices gamers. Now that the story is coming to a close in the next year, the idea of a new game is brought up. In order to gather a sense of the community's sentiment around Destiny 2, Bungie wants to analyze the twitter hype surrrounding Destiny 2. **The Goal**: Deliver a classification model to the stakeholder (Bungie) that can predict the sentiment of tweets involving Destiny 2. These predictions can bring light to the community's thoughts on Destiny 2. 

## Data Understanding

This dataset including 6.3k non-retweets within a seven day range from 11/16/2021 - 11/23/21. The Dawning event, which is a holiday event within Destiny was currently being held. 
This event made it easy to gather an understanding of the community's current wishes as a character returns during this event that is treated as a santa figure. Player's tweeted wishlists to this character that include information on their in game desires, whether it be a specific item or content rework/glitch fixes. 

## Data Preparation

The id of the user, text, language, time created, amount of favorites and amount of retweets were all included in the scrape of tweets. For this project only the text was used in the sentiment analysis. The text itself was ran through a SentimentIntensityAnalyzer to create a target variable and after it was cleaned of special characters, punctuation, stopwords and uppercase letters. Once this process was finished, the words were vectorized with a CountVectorizer.

## Feature Engineering

After running the text through a SentimentIntensityAnalyzer, the top occuring words in each category of negative and positive were accounted for in each tweet. This created two new columns, 'positive_word_count' and 'negative_word_count', that helped the models accuracy of classification of positive or negative

## Results

### Sentiment Analyzer Scores
Using the three scores obtained by the SentimentIntensityAnalyzer - positive, negative, and neutral - the tweets were overwhelmingly neutral. So the focus was steered to the positive and negative scores producing a nearly even split of positive and negative tweets.

### Metric
Accuracy takes into consideration both false positives and false negatives. This metric proved useful as we want to know both negative sentiment and positive sentiment.

### Model
This analysis used natural language processing so the prior processing had the greatest effect on the model's performance. Due to this A simple logistic regression model was used for classification. This model scored 79% accurate and a mean cross-val score of 78%. 

## Conclusion

Due to the abundance of neutral tweets, there is no recommendation to release a new game. Although, there is time for that sentiment to change so moving forward this model could be used to monitor the Destiny community's future sentiment, monitoring bugs/glitches. 

## Future Research

* Scraping different platforms such as Destiny forums, Reddit, and even Twitch chats to gather the Destiny community's sentiment.
* Scraping Reddit for players who flaunt their extreme success in order to identify possible fraudulent gameplay.

## Repository Structure


