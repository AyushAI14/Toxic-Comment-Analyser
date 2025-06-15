import os
os.environ['SSL_CERT_FILE'] = '/etc/ssl/certs/ca-certificates.crt'

import snscrape.modules.twitter as sntwitter


def get_twitter_replies(video_url, max_comments=100):
  tweet_id = video_url.split('/')[-1]
  query = f'conversation_id:{tweet_id}'
  replies=[]
  for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >=max_comments:
      break
    if tweet.inReplyToTweetId==int(tweet_id):
      replies.appeng(tweet.content)
  return replies

q = get_twitter_replies('https://x.com/IRIran_Military/status/1933590328017121748')
print(q)