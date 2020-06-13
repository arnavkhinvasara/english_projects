import math

#obtaining user input
writing=input("Please enter a piece of writing to look for spelling errors:")

#getting list of all words in dictionary
with open("Allwords.txt") as allwords:
    words = allwords.readlines()
    aw = []
    for word in words:
        if word!="\n":
            aw.append(word)
    aw2 = []
for element in aw:
    aw2.append("".join(map(str, element[:len(element)-1])))

#getting list of all words in user-answer
list_writing = list(writing)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for char in list_writing:
    if char.isspace()==False:
        str_char = "".join(map(str, char))
        if str_char not in letters:
            list_writing.remove(char)
writing2 = "".join(map(str, list_writing))
            
the_words = []
for item in writing2.split(" "):
    the_words.append(item)

#obtaining list of all misspelled words in user-answer
wrong_words = []
for word in the_words:
    new_word = word.lower()
    if new_word not in aw2:
        wrong_words.append(new_word)

#printing misspelled word(s) if any   
if len(wrong_words) > 1:     
    print("\nThese are the words that are misspelled:")
elif len(wrong_words)==1:
    print("\nThis is the word that is misspelled:")
else:
    print("\nYou have not misspelled any words.")
        
for wrong_word in wrong_words:
    print(wrong_word)

#function to compare similar letters
def Charcompare (x, y):
    count2 = 0
    for the_car in x:
        if the_car in y:
            count2+=1
    if len(x)>=len(y):
        if count2>=len(x) - 1:
            return True
    else:
        if count2==len(x):
            return True

#function to figure out if a word has many repeating letters
def Repeater (x):
    repeat_counter = []
    for char in x:
        if x.count(char)>1:
            repeat_counter.append(char)
    if len(repeat_counter)>2:
        return True
    return False

#function to compare similar letters in similar areas
def Ordercompare (x, y):
    list_x = list(x)
    list_y = list(y)
    index_finder = []
    count = 0
    for char in list_y:
        if char in list_x:
            if list_x.count(char)>1:
                for thing in list_x:
                    if thing==char:
                        index_finder.append(list_x.index(thing))
            else:
                index_finder.append(list_x.index(char))
   
            if len(index_finder)>1:
                for character in index_finder:
                    if int(character)==list_y.index(char) or int(character)==list_y.index(char) + 1 or int(character)==list_y.index(char) - 1:
                        count+=1
                        break                  
            else:
                if int(index_finder[0])==list_y.index(char) or int(index_finder[0])==list_y.index(char) + 1 or int(index_finder[0])==list_y.index(char) - 1:
                    count+=1

            index_finder.clear()

    if Repeater(y):
        if count>=len(list_y):
            return True
    else:
        if count>=len(list_y) - 1:
            return True

#function to figure out distance between 2 coordinates
def distance(x, y, a, b):
    return math.sqrt(pow(x - a, 2) + pow(y - b, 2))

#function to find distance between 2 letters
def checker(x, y):
    keyboard_row4 = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", ""]
    keyboard_row3 = ["", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", ""] 
    keyboard_row2 = ["", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "", "", ""] 
    keyboard_row1 = ["", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "", "", ""]  
    if y in keyboard_row1:
        y_ycoordinate = 1
        y_xcoordinate = keyboard_row1.index(y) + 1
    elif y in keyboard_row2:
        y_ycoordinate = 2
        y_xcoordinate = keyboard_row2.index(y) + 1
    elif y in keyboard_row3:
        y_ycoordinate = 3
        y_xcoordinate = keyboard_row3.index(y) + 1
    else:
        y_ycoordinate = 4
        y_xcoordinate = keyboard_row4.index(y) + 1
    if x in keyboard_row1:
        x_ycoordinate = 1
        x_xcoordinate = keyboard_row1.index(x) + 1
    elif x in keyboard_row2:
        x_ycoordinate = 2
        x_xcoordinate = keyboard_row2.index(x) + 1
    elif x in keyboard_row3:
        x_ycoordinate = 3
        x_xcoordinate = keyboard_row3.index(x) + 1
    else:
        x_ycoordinate = 4
        x_xcoordinate = keyboard_row4.index(x) + 1
    if distance(y_ycoordinate, y_xcoordinate, x_ycoordinate, x_xcoordinate)<=math.sqrt(2):
        return True

#function to determine whether all characters from right word are in wrong word
def checker2(x, y):
    counter3 = 0
    for char in y:
        if char in x:
            counter3+=1
    if counter3==len(y):
        return True
     
#function to determine whether a letter in a right word is near a corresponding letter in the misspelled word
def near_or_not (x, y):
    not_in_list = []
    list_x2 = list(x)
    counter2 = 0
    for char in y:
        if char not in x:
            not_in_list.append(char)
            index_wanted = list(y).index(char)
            if index_wanted==0:
                if checker(char, list_x2[index_wanted]) or checker(char, list_x2[index_wanted + 1]):
                    counter2+=1
            elif index_wanted==len(x) - 1:
                if checker(char, list_x2[index_wanted]) or checker(char, list_x2[index_wanted - 1]):
                    counter2+=1
            else:
                if checker(char, list_x2[index_wanted - 1]) or checker(char, list_x2[index_wanted - 1]) or checker(char, list_x2[index_wanted - 1]):
                    counter2+=1
    if checker2(x, y):
        return True
    if counter2==len(not_in_list):
        return True

#function to determine whether lettes are the same and in exact same place
def exact(x, y):
    countness = 0
    for char in y:
        if char in x:
            if list(y).index(char)==list(x).index(char) or len(y)!=len(x):
                countness+=1
    if countness>=len(y) - 1:
        return True

#function to determine whether an extra letter should have been misstyped
def spec_diff(x, y):
    len_x = len(x)
    len_y = len(y)
    listx = list(x)
    listy = list(y)
    if len_x==len_y + 1:
        if checker(listx[len_x - 1], listy[len_y - 1]):
            return True
        else:
            return False
    elif len_x!=len_y + 1:
        return True

#printing most similar word(s) of each misspelled word
related_words = []
for wrong_word_wanted in wrong_words:
    lower_wrongy = len(wrong_word_wanted) - 2
    higher_wrongy = len(wrong_word_wanted) + 1
    for elementistic in aw2:
        len_elementistic = len(elementistic)
        if len_elementistic>lower_wrongy and len_elementistic<higher_wrongy:
            if Charcompare(wrong_word_wanted, elementistic):
                if Ordercompare(wrong_word_wanted, elementistic):
                    if near_or_not(wrong_word_wanted, elementistic):
                        if exact(wrong_word_wanted, elementistic):
                            if spec_diff(wrong_word_wanted, elementistic):
                                related_words.append(elementistic)
    print("\nFor word " + wrong_word_wanted + ", did you mean: ", end = " " )
    for word in related_words:
        if related_words.index(word)!=len(related_words) - 1:
            print(word+" OR",end=" ")
        else: 
            print(word)
    related_words.clear()