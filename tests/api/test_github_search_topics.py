import requests
import pytest

def test_search_topics(fixture_git_hub_api_client):
    """
    This ...
    """
    topic_name = 'SQL'
    topics_list, response_code = fixture_git_hub_api_client.search_topics(topic_name, 100)
    assert len(topics_list)>99
    
def test_search_topics_negative(fixture_git_hub_api_client):
    """
    This ...
    """
    topic_name = 'asdasdasddsfdsfsdf'
    topics_list, response_code = fixture_git_hub_api_client.search_topics(topic_name, 100)
    assert len(topics_list) == 0
    
def test_search_topics_specific(fixture_git_hub_api_client):
    """
    This ...
    """
    topic_name = 'fastapi-crud-app'
    topics_list, response_code = fixture_git_hub_api_client.search_topics(topic_name, 100)
    assert len(topics_list) == 1
    
def test_search_topics_empty_name(fixture_git_hub_api_client):
    """
    This ...
    """
    topic_name = ''
    topics_list, response_code = fixture_git_hub_api_client.search_topics(topic_name, 100)
    
    assert response_code == 422 and len(topics_list) == 0