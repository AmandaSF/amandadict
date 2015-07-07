

my_file = open("test.txt")
dict_value = {}
for line in my_file:
    line = line.strip()
    my_data = line.split(" ")
    
    #print my_data
    for word in my_data:
        key = word
        value = 1
        dict_value[key] = value
        if word in dict_value.keys():
            dict_value[key] = value
        else:
            dict_value[key] =value + 1
        print dict_value

for tup in dict_value.items():
    print "%s: %d" % (tup[0], tup[1])

