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
if __name__ == "__main__":
     bna_news = newspaper.build("http://www.beforesandafters.com", memoize_articles =False)
     for article in bna_news.articles:
         extract = extract_article(article)
         print(extract + "\n")
     #print("Hello!")
