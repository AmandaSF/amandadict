score = open("scores.txt")
restaurant = {}

for line in score:
    line = line.strip()
    score_list = line.split(":")

    restaurant[score_list[0]] = score_list[1]

sorted_list = sorted(restaurant)
for item in sorted_list:


print sorted_list

#print sorted(restaurant) 
print " "
#print sorted(restaurant[0], "is rated at",restaurant[1]+".")
#print "%s: %d" % (tup[0], tup[1])
