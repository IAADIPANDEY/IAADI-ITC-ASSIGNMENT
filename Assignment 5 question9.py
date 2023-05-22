#using split operator to split list of words
word_list = input("Enter a list of words (separated by spaces): ").split()

#using for loop and get operator to get the number of repeated strings
word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1

print("Word count:")
for word, count in word_count.items():
    print(word, "occurs", count, "times")
