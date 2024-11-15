text=input("Enter the long text:")

print(text)  #We print the text

words=text.split() #Converting the string to a list of words


word_frequency={}  #Creating a dictionary to count the frequency of each word

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
        print(word)
    else:                              #Here we go through each word and count their occurence
        word_frequency[word] = 1
        print(word)  


#Printing words and their frquencies
print("\n word_frequency:\n")
for word, frequency in word_frequency.items():
    print(f"(word):{frequency}")
