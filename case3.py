letter=input()
if(letter=='A' or letter=='a' or letter=='E' or letter=='e' or letter=='I' or letter=='i' or letter=='O' or letter=='o' or letter=='U' or letter=='u'):
	print("Vowel")
elif((letter>='a' and letter<='z') or (letter>='A' and letter<='Z')):
    print("Consonant")
else:
	print("invalid")
