# Write your MySQL query statement below
SELECT tweet_id FROM tweets WHERE CHAR_LENGTH(content) > 15

# import pandas as pd

# def invalid_tweets(tweets: pd.DataFrame) -> pd.Data.Frame:
#     is_valid = tweets['content'].str.len() > 15
#     df = tweet[is_valid]
#     return df[['tweet_id']]