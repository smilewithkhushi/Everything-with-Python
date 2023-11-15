
'''
LINKEDIN LEARNING COURSE - ADVANCED PYTHON
Ques : Ask a user to enter any string, phrase or word and test for the pallindrome. (for a phrase, whitespaces are not considered for a pallindrome test)
'''
#optimized approach
import re

def is_pallindrome(phrase):
	forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
	backwards= forwards[::-1]
	return forwards==backwards


#check whether the input value is a pallindrome or not
k=0
while (k<10):
	flag=0
	s=input("enter any alphabet for pallindrome test: ")
	end=len(s)//2
	j=-1
	for i in range(0, end):
		if s[i]==s[j]:
			flag+=1
		else:
			flag=0
		j-=1
	
	#output section
	if flag==0:
		print("-> false: not a pallindrome \n")
	else:
		print(" -> true: it is pallindrome \n")
	k+=1
	


