                    #{key : value}
class_professors = {'Cart_253_A':'Pippin Bar',
                    'Cart_211':'Brad Todd',
                    'Cart_214':'Joanna Berzowska', 
                    'Cart_215':'Jonathan Lessard'}
# print(type(class_professors))

specialList = {17: [1.6, 2.45], 42: [11.6, 19.4], 101: [0.123, 4.89]}
# print(type(specialList))
# print(specialList[17])

# print(class_professors['Cart_253_A'])

# print(specialList.keys())
# for key in specialList.keys():
#     print(specialList[key]) #print the values associated with that key, no the key

# print(specialList.values())
# for value in specialList.values():
#     print(value)
# print(specialList.items())
# for item in specialList.items():
#     print(type(item[1]))

# for item in specialList:
#     print(item)
#     print(specialList[item])


###Dictionaries can contain lists and other dictionaries
# shopping = {
#             'vegetables': [{'spinach':['green','blue']}, 'carrots','broccoli','lettuce'],
#             'fruit': ['canteloupe', 'banananas'],
#              'bakery': ['bagels', 'rye bread'],
#             }
# print(shopping['vegetables'][0]['spinach'][0])
# print(shopping['vegetables'][1])

# print("Vegetable items on your list:")
# for item in shopping['vegetables']:
#     print("* " + item)

###Adding key/value pairs to a dictionary
shopping_rev = {
            'vegetables': {"green":["spinach","broccoli","lettuce"],"orange":["carrots"]},
            'fruit': ['canteloupe', 'banananas'],
             'bakery': ['bagels', 'rye bread'],
            }
shopping_rev["cleaning_items"] = ["dish-soap", "sponges"]
shopping_rev['cleaning_items'].append('bleach')
print(shopping_rev)

###Dictionary keys are unique - to add, values need to be in a list. cannot add something to a key that only has one value in it. 


