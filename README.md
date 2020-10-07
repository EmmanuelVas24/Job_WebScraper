This program is a web-scraper that retrieves job descriptions and requirements from indeed, glassdoor, careerbuilder, and dice. The program maintains a list of common words, and common pairs that appear together frequently. Each word (and pair), is then classified into either 'skill','requirement', or 'other'. 
The main program is "Jobcount0611.py".

"dictionary.txt" contains a python dictionary, where the key is the job number, and the value is a list, where each line of the job requirement is an element.

"pairs.txt" contains the most common pairs of words. Each pair has a tag indicating whether it is a skill or requirement. The average distance between the words and the frequency of occurence is also shown.
