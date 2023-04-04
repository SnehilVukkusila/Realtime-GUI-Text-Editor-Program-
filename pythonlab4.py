#read a paragraph from the user and count the number of words and the frequency and search for the specific word


str = input('enter the paragraph')
print(f'the entered parahgraph is {str}')
wordcount = len(str.split())
print(f'the total number of words is {wordcount}')

print(f'the upper case is {str.upper()}')

print(f'the lower case is {str.lower()}')

print(f'the title case is {str.title()}')

counts = {}
words = str.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for key in list(counts.keys()):
    print(key,":", counts[key])

searchword = input("enter the word to search:")
result = str.find(searchword)

if (result) != -1 :
    print(searchword + 'was found in the para')
else:
    print(searchword+ "was not found in string!!!!")
    

