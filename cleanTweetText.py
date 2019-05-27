#!/usr/bin/python
#encoding: utf-8
'''
Created on Dec 8, 2015

@author: abdullateef
'''
'''
    This code process tweets text to remove @ # !  URLs and remove new line and no arabic words from text.
    row[0].isdigit() is to make sure that the line begin with tweet id
    the line structure in the file as follow:
        row[0] tweet.id_str ,
        row[1] tweet.author.screen_name,
        row[2] tweet.text
'''

import csv
import re

def extractLocations(fileName):
#     resultFolder="D:/SNA/content/tweetsOnly/cleaned/"
#     sourceFolder="D:/SNA/content/tweetsOnly/origin/"
     
    resultFolder="D:/Research/stock_prediction/cleaned_tweets/"
    sourceFolder="D:/Research/stock_prediction/dayByday/"
     
#     resultFolder="D:/SNA/content/retweetGraphTweets/cleaned/"
#     sourceFolder="D:/SNA/content/retweetGraphTweets/"
    result_file = open(resultFolder +"locations.csv", "w+")
#     result_file = open(resultFolder +fileName +"_re_tweets_cleaned.txt", "w+")
   
    try:
        reader = csv.reader(open(sourceFolder +fileName +".csv", 'rU'), delimiter = ',' ,lineterminator='\n')
#         reader = csv.reader(open(sourceFolder +fileName +"_tweets.csv", 'rU'), delimiter = ',' ,lineterminator='\n')
#         reader = csv.reader(open(sourceFolder +fileName +"_re_tweets.csv", 'rU'), delimiter = ',' ,lineterminator='\n')
        for row in reader:
            if( not row):
                continue
            else:
                if(row[0].isdigit()):
                    try:
                        line =row[4]
                        if (line !=""):
                            result_file.write(line+'\n')
                
                    except:
                        continue 
                else:
                    continue
               
    finally:
        pass
    
    print "extract locations for " + fileName +" done"
def cleanTweets(fileName):
#     resultFolder="D:/SNA/content/tweetsOnly/cleaned/"
#     sourceFolder="D:/SNA/content/tweetsOnly/origin/"
     
    resultFolder="D:/Research/stock_prediction/cleaned_tweets/"
    sourceFolder="D:/Research/stock_prediction/dayByday/"
     
#     resultFolder="D:/SNA/content/retweetGraphTweets/cleaned/"
#     sourceFolder="D:/SNA/content/retweetGraphTweets/"
    result_file = open(resultFolder +fileName +"_tweets_cleaned.txt", "w+")
#     result_file = open(resultFolder +fileName +"_re_tweets_cleaned.txt", "w+")
   
    try:
        reader = csv.reader(open(sourceFolder +fileName +".csv", 'rU'), delimiter = ',' ,lineterminator='\n')
#         reader = csv.reader(open(sourceFolder +fileName +"_tweets.csv", 'rU'), delimiter = ',' ,lineterminator='\n')
#         reader = csv.reader(open(sourceFolder +fileName +"_re_tweets.csv", 'rU'), delimiter = ',' ,lineterminator='\n')
        for row in reader:
            if( not row):
                continue
            else:
                if(row[0].isdigit()):
                    try:
                        line =' '.join(re.sub("(@[a-zA-Z0-9]+)|(#)|(!)|(\w+:\/\/\S+)|(\n)|([a-zA-Z]+)"," ",row[2]).split())
                        result_file.write(line+'\n')
                    except:
                        continue 
                else:
                    continue
               
    finally:
        pass
    
    print "cleaning tweets for " + fileName +" done"

print "Start cleaning tweets process"

def cleanTweetsbyLocation(fileName,locationfilename):
#     resultFolder="D:/SNA/content/tweetsOnly/cleaned/"
#     sourceFolder="D:/SNA/content/tweetsOnly/origin/"
     
    resultFolder="D:/Research/stock_prediction/cleaned_tweets/"
    sourceFolder="D:/Research/stock_prediction/dayByday/"
    
    locationsfile="D:/Research/stock_prediction/"
#     resultFolder="D:/SNA/content/retweetGraphTweets/cleaned/"
#     sourceFolder="D:/SNA/content/retweetGraphTweets/"
    result_file = open(resultFolder +fileName +"_"+locationfilename+"_tweets_cleaned.txt", "w+")
#     result_file = open(resultFolder +fileName +"_re_tweets_cleaned.txt", "w+")
   
    try:
        reader = csv.reader(open(sourceFolder +fileName +".csv", 'rU'), delimiter = ',' ,lineterminator='\n')
#         reader = csv.reader(open(sourceFolder +fileName +"_tweets.csv", 'rU'), delimiter = ',' ,lineterminator='\n')
#         reader = csv.reader(open(sourceFolder +fileName +"_re_tweets.csv", 'rU'), delimiter = ',' ,lineterminator='\n')
        for row in reader:
            if( not row):
                continue
            else:
                if(row[0].isdigit()):
                    try:
                        
                        reader1 = csv.reader(open(locationsfile+locationfilename+".csv", 'rU'), delimiter = ',', lineterminator='\n')
                        for row1 in reader1:
                            
                            if (row1[0] in row[4]):
                                line =' '.join(re.sub("(@[a-zA-Z0-9]+)|(#)|(!)|(\w+:\/\/\S+)|(\n)|([a-zA-Z]+)"," ",row[2]).split())
#                                 print line
                                result_file.write(line+'\n')
                                break
                    except:
                        continue 
                else:
                    continue
               
    finally:
        pass
    
    print "cleaning tweets for " + fileName +" done"

print "Start cleaning tweets process"


for i in range(4,46):
#     splitFiles("Financial_DS_12_3","Financial_DS","2016-03-"+str(i))
    if (i<10):
        cleanTweets("Financial_DS_2016-03-0"+str(i))
#         cleanTweetsbyLocation("Financial_DS_2016-03-0"+str(i),"sa_locations")
#         extractLocations("Financial_DS_2016-03-0"+str(i))
        print "2016-03-0"+str(i)
    else:
        if (i<32):
            cleanTweets("Financial_DS_2016-03-"+str(i))
#         cleanTweetsbyLocation("Financial_DS_2016-03-"+str(i),"sa_locations")
#         extractLocations("Financial_DS_2016-03-"+str(i))
            print "2016-03-"+str(i)
        else:
            if (i<41):
                cleanTweets("Financial_DS_2016-04-0"+str(i-31))
                print "2016-04-0"+str(i-31)
            else:
                cleanTweets("Financial_DS_2016-04-"+str(i-31))
                print "2016-04-"+str(i-31)    




# cleanTweets("Morsi_replies")
# cleanTweets("seesi_replies")
# cleanTweets("Hizb_alnoor_replies")
# cleanTweets("Haram_replies")
# cleanTweets("Estish-had_Sadam_Hussain_replies")
# cleanTweets("Al_Entofadah_replies")
# cleanTweets("Tdafo3Mena_replies")
# cleanTweets("3ashoraa_replies")
# cleanTweets("Ahlam_Sa6beh_Da3iah_islamiah_replies")


print "End of cleaning tweets process"