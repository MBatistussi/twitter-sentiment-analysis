import oauth2 as oauth
import urllib2 as urllib


api_key = "YU0KmCt8JMhSml0EwurQDvUtv"
api_secret = "Iuu7zawVK2zmMJMeRgFGDl19LsqhkQs19MmKNUZSrCh7qk5oCq"
access_token_key = "825902122893971458-KMgjVVWqMibax6bDz8IwqOhzzQCQgnf"
access_token_secret = "wdfiGxkPBoRa6pWyhQE5FW2soUUAMeOCnuzKpVeSvIlGI"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
    token=oauth_token, http_method=http_method, http_url=url,
    parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response

def fetchsamples():
    url = "https://stream.twitter.com/1.1/statuses/sample.json"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print line.strip()

def create_dictionary(sentiment):
    afinn_file  = sentiment
    scores = {}
    for line in afinn_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    return scores

def create_west_coast_list(tweets):
    tweets_list = tweets
    list_of_tweets = []
    for line in tweets_list:
        tweet = json.loads(line)
        if tweet.has_key('location'):
            #Faz a mágica por aqui, pega ", CA" ", OR" ", WA" ", HI" e ", AK"
            #se for de um deles, segue em frente
            if tweet.has_key('text'):
                text = tweet['text']
                list_of_tweets.append[text]
    return list_of_tweets

def create_east_coast_list(tweets):
    tweets_list = tweets
    list_of_tweets = []
    for line in tweets_list:
        tweet = json.loads(line)
        if tweet.has_key('location'):
            #Faz a mágica por aqui, pega ", CA" ", OR" ", WA" ", HI" e ", AK"
            #se for de um deles, segue em frente
            if tweet.has_key('text'):
                text = tweet['text']
                list_of_tweets.append[text]
    return list_of_tweets

def create_south_list(tweets):
    tweets_list = tweets
    list_of_tweets = []
    for line in tweets_list:
        tweet = json.loads(line)
        if tweet.has_key('location'):
            #Faz a mágica por aqui, pega ", CA" ", OR" ", WA" ", HI" e ", AK"
            #se for de um deles, segue em frente
            if tweet.has_key('text'):
                text = tweet['text']
                list_of_tweets.append[text]
    return list_of_tweets

def create_midwest_list(tweets):
    tweets_list = tweets
    list_of_tweets = []
    for line in tweets_list:
        tweet = json.loads(line)
        if tweet.has_key('location'):
            #Faz a mágica por aqui, pega ", CA" ", OR" ", WA" ", HI" e ", AK"
            #se for de um deles, segue em frente
            if tweet.has_key('text'):
                text = tweet['text']
                list_of_tweets.append[text]
    return list_of_tweets

def create_rocky_mountains_list(tweets):
    tweets_list = tweets
    list_of_tweets = []
    for line in tweets_list:
        tweet = json.loads(line)
        if tweet.has_key('location'):
            #Faz a mágica por aqui, pega ", CA" ", OR" ", WA" ", HI" e ", AK"
            #se for de um deles, segue em frente
            if tweet.has_key('text'):
                text = tweet['text']
                list_of_tweets.append[text]
    return list_of_tweets

def calculate_scores(tweets, dictionary):
    for i in tweets:
        words_list = i.split()
        for i in words_list:
            if i in dictionary:
                score = score + dictionary[i]

        print score

if __name__ == '__main__':

    list_tweets = []
    scores_west_coast = []
    scores_east_coast = []
    scores_south = []
    scores_midwest = []
    scores_rocky_mountains = []

    fetchsamples()

    sent_file = open("AFINN-111.txt")
    tweet_file = open("three_minutes_tweets.json")

    dictionary = create_dictionary(sent_file)

    west_coast_tweets = create_west_coast_list(tweet_file)
    east_coast_tweets = create_east_coast_list(tweet_file)
    south_tweets = create_south_list(tweet_file)
    midwest_tweets = create_midwest_list(tweet_file)
    rocky_mountains_tweets = create_rocky_mountains_list(tweet_file)

    scores_west_coast = calculate_scores(west_coast_tweets, dictionary)
    scores_east_coast = calculate_scores(east_coast_tweets, dictionary)
    scores_south = calculate_scores(south_tweets, dictionary)
    scores_midwest = calculate_scores(midwest_tweets, dictionary)
    scores_rocky_mountains = calculate_scores(rocky_mountains_tweets, dictionary)
