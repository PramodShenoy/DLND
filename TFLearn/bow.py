def bag_of_words(text):
    # TODO: Implement bag of words
    words=text.split(' ')
    bag={}
    count=[]
    for word in words:
       print word
       bag[word]=0
    keys=bag.keys()
    for key in keys:
    	count=0
    	for word in words:
    		if word==key:
    			count+=1
    	bag[key]=count

    return bag

test_text = 'the quick brown fox jumps over the lazy dog'

print(bag_of_words(test_text))