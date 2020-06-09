
#Description: Scrape and Summarize articles
 	#find artices online about animtaion.
#pip install nltk 
#pip install newspaper3k
import nltk 
from newspaper import Article
#Get the article from Cartoon Brew
#url is the variable for the article
url = 'https://www.cartoonbrew.com/sponsored-by-enoben/the-callipeg-app-offers-an-intuitive-new-way-to-do-2d-animation-on-an-ipad-190845.html'
article = Article(url)

#Do some NLP
article.download()
article.parse()
#nltk.download('punkt')
article.nlp()


#Get the authors
article.authors

#get publis datpye
article.publish_date

article.top_image

#article text
#


#print(article.summary)
