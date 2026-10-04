# fruits = ["oranges", "bananas", "melons","strawberries"]
# for el in fruits:
#     print(f"I love {el}")

# testString = "A wonderful sunshiny day"
# for ch in testString:
#     print(ch)

# newItems = []
# newItems.append("first")
# print(newItems[0])

### EXTEND(AnotherLisst)
# listA = ["red", "blue", "orange"]
# listB = ["sarah", "micheal", "kiara", "stephen"]
# # listA.extend(listB)
# # print(listA)

### +=
# listC = ['cats','dogs','parrots']
# listA +=listC
# print(listA)

###sort()
# listToSort = ['water','question','apples','wander']
# listToSort.sort()
# print(listToSort)

# listToSortBools = [True,True,False,True]
# listToSortBools.sort()
# print(listToSortBools)

# listToSortNums = [2.5,6,7,43,102.6,1,1.2,0.8]
# listToSortNums.sort()
# print(listToSortNums)

# el = listToSort.pop()
# print(f"item removed: {el}")
# print(f"rev list: {listToSort}")

###Finding Existence
# list_ex = ['stars', 23, 'stripes',"dots",62]
# ##1 
# if 'stars' in list_ex:
#     print('yay')
# if 'star' not in list_ex:
#     print('not in list')

##join()
# element_list = ["hydrogen", "helium", "lithium", "beryllium", "boron"]
# glue = ", and "
# single_str = glue.join(element_list)
# print(single_str)

###List slicing;  (list_name[start : end])
# aList = [1,2,3,4,5,'a','b','c','d','e'] 
# print(aList[0:5])
# # Get elements until from start until index 5 
# cList = aList[:5] #specify end and leave start blank
# print(cList)

# ##Get items at specified intervals - list_name[start : end : step]
# # Get every third element from the list, starting from index 1 to 8(exclusive)
# stepB = aList[1:8:3]
# print(stepB)

# print(aList[-2])

# qList = [1,2,3,4,5,'a','b','c','d','e'] 
# qList[0:2] = 'z'    ## replace [1,2] with single ['z']
# print(qList)

# rList = [1,2,3,4,5,'a','b','c','d','e'] 
# rList[0:2] = 'zz'   ## replace [1,2] with ['z','z'] - excluding 2 
# print(rList)

###READING FROM A TEXT TILE
# franken_1 = open("data/frankenstein.txt").read()
# print(franken_1)
