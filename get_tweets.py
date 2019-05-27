# -*- coding: utf-8 -*-

import tweepy
import sys
import re
import csv


datasetsFolder="e:/stock_datasets/"

def getTweets(searchQuery, sinceId, outputFile):
     
    # API and ACCESS KEYS
    API_KEY = "kRM78NvxjetH5lKWhKg8HnRkl"
    API_SECRET = "WYARVTbT7pvYQ804MQ8HMarkUnASCTglHswUFXlu1YrmbK1Dgtl"
     
    tweetsPerQry = 100
    
    last_id = -1L
    
    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
    
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    if (not api):
        print ("Can't Authenticate Bye!")
        sys.exit(-1)
    
    
    # search for large  umber of tweets
     
    tweetCount = 0
    print("Start downloading tweets")
    while True:
        try:
            if (last_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(last_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(last_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
             
#             tweets_for_csv = [[tweet.id_str,tweet.author.screen_name.encode('utf8'),
#                                tweet.author.id, tweet.text.encode("utf-8"),
#                                tweet.created_at,tweet.retweeted,
#                                tweet.user.location.encode('utf8')] for tweet in new_tweets]
#           
            tweets_for_csv = [[tweet.id_str,tweet.author.screen_name.encode('utf8'),
                              "\'"+' '.join(re.sub("(\n)"," ",tweet.text.encode("utf-8")).split())+"\'",
                                tweet.created_at,
                                tweet.user.location.encode('utf8')] for tweet in new_tweets]  

    #    #write to a new csv file from the array of tweets
    #    
            print "writing to {0}.csv".format(outputFile)
            
            with open(datasetsFolder + outputFile +".csv", 'a') as f:
                writer = csv.writer(f, delimiter = ',', lineterminator='\n')
                writer.writerows(tweets_for_csv)
    
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            pass
    

'''
 get_tweets(searchQuery ="# search key" , sinceId =None , outputFile = output file)
 
 sinceId = " the Id we want to get tweetes after it "
 
''' 

       




getTweets("سعر OR أسعار OR اسهم OR نقدي OR مالية OR سوق OR بورصة OR ارباح" , sinceId ="721413759995158533", outputFile ="Financial_DS_22_4")


          
      
    