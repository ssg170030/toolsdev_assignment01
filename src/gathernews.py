def  articles(word):
	count = 0
	
	for char in word:
		if char.lower() in'aeiou':
		    count = count + 1
	return count


keyinput = keyinput("Enter a word:")
print(keyinput)
print(articles(keyinput))