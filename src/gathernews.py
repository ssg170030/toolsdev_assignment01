# Description: Scrape and Summarize Animation articles on the Web
# find articles online about animation.
# websites that I found Cartoon Brew, NewYorker, and The Conversation


import nltk
from newspaper import Article



# url is a variable to store the article
url = 'https://www.cartoonbrew.com/business/everything-is-awesome-again-universal-and-lego-strike-exclusive-five-year-film-deal-190418.html'
#cartoon is also known as Cartoonbrew
cartoon = Article(url)


url = 'https://theconversation.com/tom-and-jerry-why-theyre-a-cat-and-mouse-double-act-for-the-ages-91762'
#con is also known as The Conversation
con = Article(url)


url = 'https://www.newyorker.com/magazine/2019/12/30/the-surprise-and-wonder-of-early-animation'
# new is also known as NewYorker
# varible to store the link
new = Article(url)


# download to get the article
cartoon.download()
con.download()
new.download()
#Then parse each article
cartoon.parse()
con.parse()
new.parse()

nltk.download('punkt')
cartoon.nlp()
con.nlp()
new.nlp()


#From Cartoon brew website
cartoon.title
# Get the authors who wrote the article
cartoon.authors
# get publish date
cartoon.publish_date
# finds the image and prints out a link to be shown on the Web
cartoon.top_image


#From Cartoon brew website
print(cartoon.title)
print(cartoon.authors) # Amid Amidi, Alex Dudok De Wit
print(cartoon.publish_date) #04-19-2018
print(cartoon.summary)



#From The Conversation
con.title
con.authors
con.publish_date

print(con.title)
print(con.authors) # Phillip Vaughan
print(con.publish_date) #03-14-2018
print(con.summary)

#From the NewYorker
new.title
new.authors
new.publish_date

print(new.title)
print(new.authors) #Richard Brod
print(new.publish_date) #12-30-2019
print(new.summary)

#unable to get funtion to work properly


def Articles(word):
    #number of words in each article
    art = 0

    for char in word:
        if char.lowercase() in "Article":
            art = art + 1
    return art
    userinput = input("Enter a word:")
    print(userinput)
    print(key(userinput))
