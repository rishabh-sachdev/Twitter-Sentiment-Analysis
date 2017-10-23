this is very simple and rough version of our project... 

1. I've extracted around 20k+ tweets from using tweepy. They are saved in twitDB1.csv file in the data folder.
2. saved the text of those tweets in the tweetText.csv file
3. pre_processed.py then pre_processes them (removing all @,links etc). saved in pre_processed.csv
4. Then classify.py does 2 things  --
    a. remove all non english words from the tweets(yes there is still a lot of garbage in them) using nltk's wordnet module
    b. classifies them as tweets related to punctuality, cleanliness etc(just 2 sections till now...we could add more like food)
5.Finally sentiment_analysis.py simply predicts the tweet as positive or negative. So I've printed the % of tweets in each section (cleanliness/punctua..) as + or -

this is just a very rough idea...and many predictions are wrong. However I guess from here on we could do some sort of meaningful analysis like trends in feedback etc. and prepare a project report by plotting some graphs and that sort of shit.


I've used this playlist by sentdex to learn nltk.
https://www.youtube.com/watch?v=FLZvOKSCkxY&index=1&list=ac


please give ur suggestions and/or feedback
