import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_app = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_app):
            links.remove(url)

    return links 


def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.th/search?q=" + query)
    return response

def parse_results(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    if results:
        result = results[0]
        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            'text': result.find(css_identifier_text, first=True).text
        }
        return item
    else:
        return None


def google_search(query):
    try:
        response = get_results(query)
        result = parse_results(response)
    
        if result:
          return result
        else:
            print("I dont understand the question")
            return None
    except: 
        print("Sorry, I don't have information on this.")


while True:
    x = input("Search here: ")
    if x.lower() == 'exit':
        break
   
    result = google_search(x)

    if result:
        z = print(result['text'])
      
    else:
        print()
    print()