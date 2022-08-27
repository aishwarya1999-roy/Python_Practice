# display count if it matches the pattern -> _at or _at_

def count_names(name_list):
    count1 = 0
    count2 = 0
    for i in name_list:
        if "at" in i:
            count2+=1
        if i.endswith("at") and i.find("at") == 1:
            count1+=1
    print("_at -> ",count1)
    print("%at% -> ",count2)
name_list = ['at', 'dats']
count_names(name_list)