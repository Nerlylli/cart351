print("Task 21: Loops, part 2")
print("Expected output:")
print("  Artichokes")
print("  Aubergines")
print("  Carrots")
print("  Fiddleheads")
print("  Turnips")
print("  Radishes")

# Task 21: Write a "for" loop below that prints out each item in the list "vegetables" (defined above), but with the first letter of each item capitalized.
# (The list should contain the item that you added to the list in task 17.)

vegetables = ["aubergines", "carrots", "turnips", "fiddleheads", "artichokes"]
vegetables.sort()
vegetables.append("radishes")

for vegetable in vegetables:
    print(vegetable.capitalize())

#------------------------------------------------------------------------
# print("Task 22: Split and join")
# print("Expected output:")
# print("  25")
# print("  9-18-25")

# Task 22: Modify the variable "separator" below so that the first print  statement displays "25". Modify the variable "glue" so that the second print statement displays "9-18-25".


separator = "9/18/"
glue = "9/18/"
parts = "9/18/25".split(separator)
print(parts[-1])
print(glue.join(parts))

#------------------------------------------------------------------------

print("Task 23: All together now")
print("Expected output: alpha, beta, gamma, delta, epsilon, zeta, eta, theta")

# Task 23: Make three changes on the Python code below, as follows:
# (1) replace [] with an expression that evaluates to a list with two items, "eta" and  "theta" (using the .split() method). 
# (2) Replace the word "pass" with a Python statement, so that the "for" loop has the effect of adding two new items to the list "greek" - recall it was defined above - but we redefine it below:). (Use the .append() method.) 
# (3) Change the value of the variable "glue" so that the desired output is displayed.

greek = ["alpha", "beta", "gamma", "delta", "epsilon","zeta"]
new_letters = "eta theta"
new_letters_list = new_letters.split()

for letter_name in new_letters_list:
	greek.append(letter_name)
 
glue = ","
print(glue.join(greek))