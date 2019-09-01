import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

#Set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

#Assign given names for input/output files.
inputFname = sys.argv[1]
outputFname = sys.argv[2]

#Where all words are stored.
dictionary = dict()
    
#Opens file and iterate trough every line.
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        line = line.strip()
        word = re.split('[\"\' \t,;.:-]', line)
        #Iterate through every word.
        for temp in word:
            if len(temp) > 0:
                if temp.lower() in dictionary:
                    currentValue = dictionary.get(temp.lower())
                    dictionary[temp.lower()] = currentValue + 1
                else:
                    dictionary[temp.lower()] = 1

#Writes the sorted dictionary the output file.
f = open(outputFname, "w+")
for key in sorted(dictionary.keys()) :
    f.write("%s %d\r\n" % (key, dictionary.get(key)))
f.close
