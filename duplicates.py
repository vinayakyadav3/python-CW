"""

input:
list1= [1,5,10,20,40,80]
list2= [6,7,20,80,100]
list3= [3,4,15,20,30,70,80,120]

output:
[80,20]

"""

l1 = [1, 5, 10, 20, 40, 80]
l2 = [6, 7, 20, 80, 100]
l3 = [3, 4, 15, 20, 30, 70, 80, 120]

# typecast into a set
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

# join using intersection (it will put values in new variable, )
s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)

final_list = list(final_set)
print(final_list)

