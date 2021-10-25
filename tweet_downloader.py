#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(
        screen_name=screen_name, 
        count=200, 
        include_rts=False,
        exclude_replies=True
    )

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    # print(new_tweets)
    # #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(
            screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f"...{len(alltweets)} tweets downloaded so far")

    # alltweets
    # text = tweet._json["full_text"]
    # transform the tweepy tweets into a 2D array that will populate the csv
    # outtweets = [[tweet.id_str, tweet.created_at, tweet.text]
    #              for tweet in alltweets]
    # csvFile = open('result.csv', 'a')

    # # Use csv writer
    # csvWriter = csv.writer(csvFile)
    # for tweet in alltweets:
    #     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    #     print(tweet.created_at, tweet.text)

    # csvFile.close()
    print("exporting tweets")
    with open("tweets.csv", 'wt', encoding="utf8") as output:
        writer = csv.writer(output)
        writer.writerow(
            ['id', 'screen_name', 'created_at', 'retweeted', 'text']
        )
        writer.writerows([
            tweet.id_str,
            tweet.user.screen_name,
            tweet.created_at,
            tweet.retweeted,
            tweet.text] for tweet in alltweets
        )

    # with open('output_file_name', 'w', newline='', encoding='utf-8') as csv_file:
    #     writer = csv.writer(csv_file)
    #     for tweet in alltweets:
    #         writer.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    #         print(tweet.created_at, tweet.text)
# df = pd.DataFrame(outtweets)
# df.to_csv('output.csv')
# #write the csv
# with open(f'new_{screen_name}_tweets.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(["id","created_at","text"])
#     writer.writerows(outtweets)


pass


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("djkhaled")
