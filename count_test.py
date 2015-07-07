
my_file = open("test.txt")
dict_value = {}
for line in my_file:
    line = line.strip()
    my_data = line.split(" ")
    
    #print my_data
    for word in my_data:
        key = word

        if word not in dict_value.keys():
            dict_value[word] = 1
        else:
            dict_value[word] += 1
        print dict_value

for tup in dict_value.items():
    print "%s: %d" % (tup[0], tup[1])