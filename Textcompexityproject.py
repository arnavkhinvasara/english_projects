
while True:
    print("\nEnter a text file name with .txt at the end")
    answer = input()
    try:
        with open(answer) as potiontext:
            pt = potiontext.readlines()
        break
    except FileNotFoundError:
        print("\nYour text file needs to be in the same directory as the python file and/or needs to have .txt at the end")
                
scoloncounts = []
scolon = ";"
for line in pt:
    if scolon in line:
        scoloncounts.append(scolon)
scoloncount = len(scoloncounts)
        		 
charactercounts = []
for line in pt:
	for word in line.split():
		for letter in word:
			charactercounts.append(letter)
charcount = len(charactercounts)

scolonrating = 0
ratiocount1 = scoloncount/charcount
if ratiocount1 < .01:
	scolonrating = 1
elif ratiocount1 >=.01 and ratiocount1 <=.02:
	scolonrating = 2
else:
	scolonrating = 3

commacounts = []
comma = ","
for line in pt:
    if comma in line:
        commacounts.append(comma)
commacount = len(commacounts)

commarating = 0
ratiocount2 = commacount/charcount
if ratiocount2 < .05:
    commarating = 1
elif ratiocount2 >= .05 and ratiocount2 < .06:
    commarating = 2
else:
    commarating = 3


wordlist = []
for line in pt:
    for word in line.split():
        wordlist.append(word)
        
wordamount = len(wordlist)

sentenceamount = 0
period = "."
for line in pt:
    if period in line:
        sentenceamount+=line.count(".")

wpsrating = 0
wps = wordamount/sentenceamount
if wps < 10:
    wpsrating = 1
elif wps >= 10 and wps <= 15:
    wpsrating = 2
else:
    wpsrating = 3

cpwrating = 0
cpw = charcount/wordamount
if cpw < 3:
    cpwrating = 1
elif cpw >=3 and cpw <=4:
    cpwrating = 2
else:
    cpwrating = 3

totalrating = scolonrating + commarating + wpsrating + cpwrating
if totalrating <=5:
    print("There are " + str(round(wps)) + " words per sentence on average")
    print("There are " + str(round(cpw)) + " characters per word on average")
    print("The level of this text is simple and the text reached " + str(round(totalrating/12 * 100, 2)) + " percent complexity level")
elif totalrating == 6 or totalrating ==7:
    print("There are " + str(round(wps)) + " words per sentence on average")
    print("There are " + str(round(cpw)) + " characters per word on average")
    print("The level of this text is medium and the text reached " + str(round(totalrating/12 * 100, 2)) + " percent complexity level")
elif totalrating > 7:
    print("There are " + str(round(wps)) + " words per sentence on average")
    print("There are " + str(round(cpw)) + " characters per word on average")
    print("The level of this text is complex and the text reached " + str(round(totalrating/12 * 100, 2)) + " percent complexity level")

