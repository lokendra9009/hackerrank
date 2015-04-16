#bhargav has dream to study his MS is foreign country. So, He started his preparation for GRE. There are huge number of words that he has to prepare for. So, firs he wanted to group all synonyms and antonyms. As there are huge number of words that he has to group. So, he asked help to group all synonyms and antonyms of a word. it is called antonym if the first letter of a current number is 3 steps upper than reference then it is antonym if the first letter of the reference number is same as the current first letter of a word then it is synonym. and the length should be same for the antonym and synonym

#INPUT: first line should contain a word W. next line contains no of words N. next N lines consists of words that are to be grouped.

#OUTPUT print no of synonyms S followed by antonyms A.

#Sample Input (Plaintext Link)
#hasrfk
#4
#heyfgs
#jhajyrbf
#kayufs
#hetinf
#Sample Output (Plaintext Link)
#2 1

ref_word = str(input());
ref_word = ref_word.lower();
#refword_ascii = 
num_of_words = int(input());
antonyms = 0;
synonyms = 0;
n=0;
while (n<num_of_words):
	words = str(input());
	words = words.lower();
	if (ord(words[0])==ord(ref_word[0])):
		synonyms+=1;
	elif (ord(words[0])==(ord(ref_word[0])+3)):
		antonyms+=1;
	n+=1;
print (synonyms,antonyms)
