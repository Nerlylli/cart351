# var_a = 200
# var_b = 200

#inputs
var_a = int(input("Enter another integer a:")) #if the number can be both a full number or a decimal, the coding would be float(input("")), because float numbers can also be full numbers
var_b = int(input("Enter another integer b:"))

#simple if
if var_b > var_a:
    print("b is greater than a")
#else if
elif var_a > var_b:
    print("a is greater than b")
else:
    print ("a equals b")



