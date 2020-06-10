# Description: Scrape and Summarize articles
# find artices online about animtaion.
# Get the article from Cartoon Brew


import nltk
from newspaper import Article

#url is a variable to store the article
url = 'https://www.cartoonbrew.com/sponsored-by-enoben/the-callipeg-app-offers-an-intuitive-new-way-to-do-2d-animation-on-an-ipad-190845.html'
article = Article(url)

#download to get the article
article.download()

#<!DOCTYPE HTML><html itemscope itemscope itemtype = "https://www.cartoonbrew.com/sponsored-by-enoben/the-callipeg-app-offers-an-intuitive-new-way-to-do-2d-animation-on-an-ipad-190845.html"
article.parse()
nltk.download('punkt')
article.nlp()

article.html

# Get the authors who wrote the article
article.authors

# get publish date
article.publish_date

#finds the image and prints out a link to be shown on the Web
article.top_image

#collect the text
article.text

#article.summary

#prints out the output to be shown in the code when gathernews.py is called upon
print(article.publish_date)
print(article.top_image)
print(article.authors)

