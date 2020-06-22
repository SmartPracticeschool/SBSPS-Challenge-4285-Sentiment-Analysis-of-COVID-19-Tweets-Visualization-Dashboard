# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:05:37 2020

@author: jaswa
"""
def comment_analyzer(url):
    import tweepy
    from textblob import TextBlob    
    consumer_key = 'rvtYVvwPtVcL68AZeo4lNSJit'
    consumer_secret = 'yJQrdQWYO1bu6rUQhecQk5QEGF8ujR3un8zxG9Ff4ZvCftk4xr'
    access_key = '1182899917943001088-1BuCJzSgnfFvmYyR2pNqq50L04jK6n'
    access_secret ='CZvLcPFGnllMPxfnapFjcEhCTRpw1WYfYuUAyO0Qbv71R'
    
    
    def update_urls(tweet, api, urls):
        tweet_id = tweet.id
        user_name = tweet.user.screen_name
        max_id = None
        replies = tweepy.Cursor(api.search, q='to:{}'.format(user_name),
                                    since_id=tweet_id, max_id=max_id, tweet_mode='extended',lang='en').items()

        id_list = []
        for reply in replies:
            if(reply.in_reply_to_status_id == tweet_id):
                id_list.append(reply.id)
                print(len(id_list))
                #urls.append(get_twitter_url(user_name, reply.id))
                #try:
                 #   for reply_to_reply in update_urls(reply, api, urls):
                  #      pass
                #except Exception:
                 #   pass
            #max_id = reply.id
        return id_list
    
    def get_api():
        auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api
    
    def get_tweet(url):
        tweet_id = url.split('/')[-1]
        api = get_api()
        tweet = api.get_status(tweet_id)
        return tweet
    
    def get_tweet_frm_id(ids,api):
        tweets = api.statuses_lookup(ids)
        l = []
        for tweet in tweets:
            l.append([tweet.id,tweet.text])
        return l
    
  
    
    api = get_api()
    tweet = get_tweet(url)
    urls = [url]
    tweets=[]
    comments = update_urls(tweet, api, urls)
    for i in range((len(comments)//100)+1):
        ids = comments[i*100:(i+1)*100]
        val = get_tweet_frm_id(ids,api)
        tweets.extend(val)
        
    analysis = {'positive':0,'negative':0}
    
    for i in tweets:
        a = TextBlob(i[1])
        b = a.sentiment.polarity
        if(b>0):
            analysis['positive'] +=1
        if(b<0):
            analysis['negative'] +=1
            
  
    return analysis
    
if __name__ == '__main__':
    url = 'https://twitter.com/narendramodi/status/1273855790827188225'
    comments = comment_analyzer(url)
    
    
    #a = TextBlob('I am happy')
    #b = a.sentiment