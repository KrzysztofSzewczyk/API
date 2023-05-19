import requests
import pytest

def test_search_repo_positive(fixture_git_hub_api_client):
    """
    This ...
    """
    repo_name = 'python'
    
    repos_list = fixture_git_hub_api_client.search_repo(repo_name, 100)
    
    #print(repos_list)
    
    
    assert len(repos_list)>99
    
    #prepare existing repo name
    #repo_name ='python'
    #search for repo name
    #repo_list = api_github_client.search_repo(repo_n
    # ame)
def test_search_repo_negative(fixture_git_hub_api_client):
    """
    This ...
    """
    repo_name = '213sdfasd'
    
    repos_list = fixture_git_hub_api_client.search_repo(repo_name)
    
    #print(repos_list)
    
    assert len(repos_list)==0
    
    #prepare existing repo name
    #repo_name ='python'
    #search for repo name
    #repo_list = api_github_client.search_repo(repo_n
    # ame)