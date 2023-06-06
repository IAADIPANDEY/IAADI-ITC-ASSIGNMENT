a = input()
# creating list containing all unique a;phabets and whitespace 
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t','u','v','w','x','y','z',' ']
# creating an empty list to append unique alphabets from given string 
c = []

for i in a.lower():# used lowercase for not getting capital and small alphabets as different unique alphabets
    if i not in c:
        c.append(i)

if sorted(b)==sorted(c):# using sort operator to arranging bot list in same order
    print('yes')
else:
    print("no")

