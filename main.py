input_string = input("Enter text   ") 
family_list = input_string.split(" ")
for n, name in enumerate(family_list): 
    if len(name) == 4:
        family_list[n] = '****';

# g1 = [i.replace("'", " ") for i in family_list]
# g1 = [x.strip('[') for x in family_list]
# g1 = family_list[1:-1].split('","')
family_list = [item.replace("'", "") for item in family_list]
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 
        
        
# print (family_list)    

print(listToString(family_list))  
    # print(name)


#The quick brown fox jumps over the lazy dog
