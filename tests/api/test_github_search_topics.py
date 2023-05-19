import requests
import pytest

def test_search_topics(fixture_git_hub_api_client):
    """
    This ...
    """
    topic_name = 'SQL'
    topics_list = fixture_git_hub_api_client.search_topics(topic_name, 100)
    assert len(topics_list)>99
    
def test_search_topics_negative(fixture_git_hub_api_client):
    """
    This ...
    """
    topic_name = 'asdasdasddsfdsfsdf'
    topics_list = fixture_git_hub_api_client.search_topics(topic_name, 100)
    assert len(topics_list) == 0
    
def test_search_topics_specific(fixture_git_hub_api_client):
    """
    This ...
    """
    topic_name = 'fastapi-crud-app'
    topics_list = fixture_git_hub_api_client.search_topics(topic_name, 100)
    assert len(topics_list) == 1