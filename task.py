# 1.Write a Python program to calculate the total number of Vowels and Count of each individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited"

#Initializing the input string
str="Guvi Geeks Network Private Limited"

# Storing the list of  vowels in the variable
vowels=["a","e","i","o","u"]

# Initializing the variable to count the total number of vowels
vc=0

# Looping through the each character in the string
for i in str:
    #This condition checks if current character is a vowel(i.e., if it exists in the 'vowels' list)
    if i in vowels:
        #If the character is vowel increases the vowel count by 1
        vc+=1
#Printing total number of vowels
print(f"Total vowel count is {vc}" )
#Printing the count of each individual vowel
print("Count of a is",str.count("a"))
print("Count of e is",str.count("e"))
print("Count of i is",str.count("i"))
print("Count of o is",str.count("o"))
print("Count of u is",str.count("u"))




# 2.Create a Pyramid of NUmbers from 1 to 20 using For loop

# Defining the no of rows for the pattern
rows=20

# Looping through each row from 0 to row-1
for i in range(0,rows):
    #This loop is for the spaces before the numbers in each row
    #The number of  spaces decreases with subsequent row 
    for j in range(0,rows-i-1):
        #This statement prints the space for required no of spaces
        print(end=" ")

#This loop prints the numbers in each row
#Prints the numbers from 1 to current row number(i+1)
    for j in range(0,i+1):
        #Prints the number followed by space
        print(j+1,end=" ")
    #This statement is to  move to the next line after printing each row
    print()



# 3.Write a program that takes a string and returns a new string with all the vowels removed

# Defining the input string
str="Guvi Geek"

#Storing the list of vowels in a variable
vowels=["a","e","i","o","u"]

# Converting the string to lowe case
str.lower()

# Looping through each character in the string
for i in str:
    # Checks if the current character is vowel(i.e., if it exists in the 'vowels' list)
    if i in vowels:
        #If the character is vowel, that is removed from the string
        str=str.replace(i,"")
#This statement prints the modified string after removing the vowels
print(str)


# 4.Write a program that takes a string and returns the number of unique characters in it

# Defining  the input string
str="Guvi Geek"

#Intialising the count of non-unique characters
nuc=0

#Intialising the count of unique characters
uc=0

# Looping through each character in the string
for i in str:
    #This condition checks the count of current character in the string is greater than 1
    #It means the character is not unique
    if str.count(i)>1:
        #If the character is not unique the count of non-unique characters is increased by 1
        nuc=nuc+1
        #Printing the messsage indicating it is a non-unique character
        print("Not unique character",i)
    else:
        #If the character is unique, the count of unique characters is increased by 1
        uc=uc+1
        #Printing the messsage indicating it is a unique character
        print("Unique character",i)
#Printing the count of unique characters
print(f"Unique characters:{uc}")
   

# 5. Write a program that takes a string and returns True if it is a plindrome, Flase otherwise
# Defining the input string
str="radar"

# Reversing the input string
revstr=str[::-1]

# This condition checks if the original string is equal to its reversed string
if str==revstr:
    # If the original string is equal to its reverse string, it is a palindrome
    print(f"True:The given string {str} is a palindrome")
else:
    # If the original string is not equal to its reverse string, it is not  a palindrome
    print(f"False:The given string {str} is not palindrome")




# 6. Write a program that takes two strings and returns the longest common substring between them

# Defining the input strings 
str1="my name is radha"
str2="my name is jyothi"


# Initialising the empty lists to store words from the each string and common words
l1=[]
l2=[]
common=[]

# To create a string from the list of common words initialising the empty string
lcs=""

# Splitting the strings into lists of words
l1=str1.split(" ")
l2=str2.split(" ")

# Loopin through each word in the first list
for i in range(len(l1)):
    # Looping through each word in the second list
    for j in range(len(l2)):
        #Checks if the current word in the first list is equal to second list
        if l1[i]==l2[j]:
            # If the words match appending in to the 'common' list
            common.append(l1[i])

# Printing the list of common words           
print(f"The longest common substring is {common}")
# Joinong the words from the 'common' list into a single string using lcs as separator
# lcs is an empty string, so the words will be concatenated without a separator
print(lcs.join(common))







# 7.Write a program that takes a string and returns the most frequent character in it

# Defining the input string
str="hello"

# Initialising an empty dictionary to store characters frequency
d=dict()

# Initialising a variable to keep track of the maximum frequency
c=0

# Looping through each character in the string
for i in str:

    # Checks if the character 'i' is already in the dictionary 'd'
    if i in d:
        # If the character is already in the dictionary, increment its count by 1
        d[i]=d[i]+1
        # Printing  the updated count for the character
        print(d[i])
    else:
        # If the character is not in the dictionary, add it with a count of 1
        d[i]=1

# Finding  the character with the maximum frequency
c=max(d,key=d.get)

# Printing  the character(s) with the highest frequency
print("most frequent characters in it:", c)





# 8.Write a program that takes a string and returns True if it is an anagram of another string,False otherwise

# Defining the input strings
str1="heart"
str2="earth"

# Sorting the input strings
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)

# Checjs if the sorted strings are equal
if sorted_str1==sorted_str2:
    # If sorted strings are equal they are anagrams
    print(f"True:The given strings {str1},{str2} are anagrams")
else:
    # If sorted strings are not equal they are not anagrams
    print(f"Flase:The given strings {str1},{str2} are not anagrams")




# 9.Write a program that takes a string and returns the number of words in it
#Method 1

# Defining the unput string
str="my name is Sushma"

# Splitting the string into list of words
li=str.split()

# Counting the words in the list by using len() function
count=len(li)

# Printing the count of words
print(f"The number words are {count}")


#Method 2

# Defining the input string
str="my name is Sushma"

# Initialising the count varaiable to count the words
count=1

# Looping through each character in the string
for i in str:
    # This condition checks if the current character is a space character(" ")
    if i==" ":
     
     # If the current characer is space, the  words count is incremented by 1 
     count=count+1
# Pinting the number of words in the string
print(f"The Number of words are {count}")