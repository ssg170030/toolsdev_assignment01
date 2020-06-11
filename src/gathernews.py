# Description: Scrape and Summarize articles
# find articles online about animation.
# Get the article from Cartoon Brew


import nltk
from newspaper import Article

url = 'https://www.the-flying-animator.com/pixilation.html'
flying = Article(url)


url = 'https://theconversation.com/tom-and-jerry-why-theyre-a-cat-and-mouse-double-act-for-the-ages-91762'
con = Article(url)


# print(info.text)
# url is a variable to store the article
url = 'https://www.cartoonbrew.com/business/everything-is-awesome-again-universal-and-lego-strike-exclusive-five-year-film-deal-190418.html'

article = Article(url)

# download to get the article
article.download()
con.download()
flying.download()

article.parse()
con.parse()
flying.parse()

nltk.download('punkt')
article.nlp()
con.nlp()
flying.nlp()

article.html
# Get the authors who wrote the article
article.authors
# get publish date
article.publish_date
# finds the image and prints out a link to be shown on the Web
article.top_image







# collect the text

# prints out the output to be shown in the code when gathernews.py is called upon


print(article.authors)
print(article.publish_date)
print(article.summary)

con.authors
con.publish_date

print(con.authors)
print(con.publish_date)
print(con.summary)

flying.authurs

print(flying.authors)

