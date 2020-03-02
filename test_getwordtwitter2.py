
from getwordtwitter2 import get_all_tweets

def test_get_all_tweets():
    assert get_all_tweets('a','b') != []
