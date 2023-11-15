#Assignment 27.09.2022

""" Ques 4 : Write a function that takes a sentence as an input parameter and replaces the first letter of every work with the corresponding uppercase letter and rest of the letters in the word
by corresponding letters in lowercase without using built-in function """

print()
print("Ques 4 : Write a function that takes a sentence as an input parameter and replaces the first letter of every work with the corresponding uppercase letter and rest of the letters in the word by corresponding letters in lowercase without using built-in function \n ")

def str_conversion(a):
    lst=a.split(" ")
    new_lst=[]
    for word in lst:
        word_lst=[i for i in word]
        if (word_lst[0]>=chr(97) and word_lst[0]<=chr(122)):
            ordAt0=ord(word_lst[0])
            word_lst[0]=chr(ordAt0-32)
        new_word="".join(word_lst)
        new_lst.append(new_word)
    new_line=" ".join(new_lst)  
    return new_line

a=input("Enter the string : ")
result=str_conversion(a)
print("-> The new string is : ",result)

""" Ques 3 : Write a fucntion that takes a sentence as an input parameter and displays the number of words in the sentence """

print()
print("Ques 3 : Write a function that takes a sentence as an input parameter and displays the number of words in the sentence \n")

def word_count(a):
    lst=a.split(" ")
    count=len(lst)
    return count

a=input("Enter the sentence : ")
result=word_count(a)
print("The words in the sentence are : ", result)


'''
Ques 2: WAF that takes two strings and returns True if they are anagrams and False otherwise. A pair of strings is anagrams if the letters
in one word can be arranged to form the second one.


def anagram_check(a,b):
    print("-")




a=input("Enter String 1 : ")
b=input("Enter String 2 : ")
print(a,b)
result=anagram_check(a,b)
if (result==1):
    print(a, " and ", b , " are anagrams! ")
else:
    print(a, " and ", b , " are not anagrams! ")

'''


'''
Ques 1 : WAP that takes a string as a parameter and returns a string with every
successive repetiitve character replaced with a star (*).


def replace_str(s):
    new=[]
    for i in range(0,len(s)):
        flag=0
        new.append(s[i])
        
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                flag+=1
                if (flag>0):
                    new.append("*")

                
        print("flag=",flag)
        print("updated=", new)
    
    new_str="".join(new)
    print("new string : ", new_str)
    return new_str         

    
s=input("Enter the string : ")
result=replace_str(s)
print("-> The replaced string is : ", result)
'''
