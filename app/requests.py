import urllib.request, json
from .models import News


api_key = None
base_url = None

def configure_request(app):
    global api_key , base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    get_news_url = base_url.format(category,api_key)

    mydata = []

    with urllib.request.urlopen(get_news_url) as url:
        highlights = url.read()
    
        newhighlights = json.loads(highlights)
        articles = newhighlights['articles']

        for article in articles:
            id = article['source']['id']
            name = article['source']['name']
            author = article['author']
            title = article['title']
            description = article['description']
            url = article['url']
            urltoimage = article['urlToImage']
            publishedat = article['publishedAt']

            mydata.append(News(id,name,author,title,description,url,urltoimage,publishedat))

    
    return mydata
