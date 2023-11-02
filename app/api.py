from app import models
import re
import requests
import os
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

Article = models.Article
Source = models.Source

all_keys = os.getenv('NEWS_API_KEYS').split(',')

api_key = random.choice(all_keys)
country_based_headlines = os.getenv('COUTRY_BASED_HEADLINES')
country_base_headlines_category = os.getenv('COUTRY_BASED_HEADLINES_CATEGORIES')
source_headlines = os.getenv('TOP_HEADLINES_FROM_SOURCE')
all_sources = os.getenv('GET_ALL_SOURCES')
global_search = os.getenv('GLOBAL_SEARCH')

def get_all_articles(url):
    response = requests.get(url)
    response.raise_for_status()
    headlines_response = response.json()
    
    headlines = []

    if headlines_response["articles"]:
        for item in list(headlines_response["articles"]):
            if item["source"] and item["author"] and item["title"] and item["description"] and item["url"] and item["urlToImage"] and item["publishedAt"] and item["content"]:
                regex = "([0-9]+)"
                result = re.split(regex, item["publishedAt"])
                date = result[5]+result[4]+result[3]+result[2]+result[1]
                
                headlines.append(Article(item["source"]["name"], item["author"], item["title"], item["description"], item["url"], item["urlToImage"], date, item["content"]))

        
    return headlines


def get_headlines(country):
    headlines_url = country_based_headlines.format(country, api_key)
    return get_all_articles(headlines_url)                   


def get_source_headlines(source):
    headlines_url = source_headlines.format(source, api_key)
    return get_all_articles(headlines_url)


def get_category_headlines(courtry, category):
    headlines_url = country_base_headlines_category.format(courtry, category, api_key)
    return get_all_articles(headlines_url)


def get_sources():
    sources_url = all_sources.format(api_key)
    response = requests.get(sources_url)
    response.raise_for_status()
    sources_response =response.json()

    sources = []

    if sources_response["sources"]:
        for source in sources_response["sources"]:
            if source["id"] and source["name"] and source["url"]:
                sources.append(Source(source["id"], source["name"], source["url"]))


    return sources
