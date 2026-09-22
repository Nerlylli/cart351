def least_difference(x1,x2,x3): 
    diff1 = abs(x1 - x2)
    diff2 = abs(x1 - x3)
    diff3 = abs(x2 - x3)
    return min(diff1,diff2,diff3)

print(least_difference(1,2,3)) #HELP!!

#example 
def write_A_String(printVar):
    print(f"hello {printVar}")

write_A_String("Sabine")
write_A_String("Nerly")
write_A_String("Jack")



