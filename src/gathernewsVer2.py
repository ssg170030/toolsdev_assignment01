import newspaper

def extract_article(article):
#"""Extract the title, authors(s0 and summary"""

    article.download()
    article.parse()
    article.nlp()
    result = article.title + " -  " + ", ".join(article.authors)
    result += "\n" + article.summary
    return result

#runing as a stand alone
#testing code works
def extract_articles(news_site, iscached=False):
    #Scans news site and extracts a list of content
    bna_news = newspaper.build(news_url, memoize_articles=iscached)
    for article in bna_news.articles:
        extract = extract_article(article)
        print(extract + "\n")
    # print("Hello!")


if __name__ == "__main__":
    news_sources = ["http://www.beforesandafters.com","https://www.cartoonbrew.com","https://www.fxguide.com/"]
    for news_irl in news_sources:
        extract_articles(news_url)