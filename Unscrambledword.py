mixed = input("Enter a scrambled country:")

with open("all_countries.txt") as temp:
    t = temp.readlines()
    t_list = []
    for i in t:
        t_list.append(i.strip())

country_list = []
for item in t_list:
    item = item.lower().replace(" ","")
    country_list.append(item)
    
#print(country_list)

def letter_dict(word):
    out = {}
    for char in word:
        if char in out.keys():
            out[char]+=1
        else:
            out[char]=1
    return out


def find_match(mixed,country_list):
    mixed_dict = letter_dict(mixed)
    for real_country in country_list:
        if mixed_dict==letter_dict(real_country):
            return real_country
        
print("Unscrambled: " + find_match(mixed,country_list))

