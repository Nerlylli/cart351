# Task 1: Add parentheses to the Python statement below so that it prints
# out the number 7.

print((10 + 4) / 2)

#------------------------------------------------------------------------

# Task 2: Change the operator in the statement below so that it displays
# "True" instead of "False."

print(14 < 15)

#------------------------------------------------------------------------

# Task 3: Change the variable assignment below so that the print statement
# displays "54." (Don't change the print statement!)

a_num_variable = 54
print(a_num_variable)

#------------------------------------------------------------------------

# Task 4: Three variables are assigned below, all with different types.
# Replace the word "None" inside the parentheses of type() in the print
# statement below so that it prints "".

x = 14
y = 17.4
z = "today is a fine day for sailing!"
if x > y :
	print(type(z))
else:
	print("")

#------------------------------------------------------------------------
# Task 5: Inside the call to "print" below, write an expression that evaluates
# to the sum of the lengths of the two string variables defined below
# (first_line and second_line). Use the len() function.

first_line = "It was the best of times."
second_line = "It was the worst of times."
text = first_line + second_line
print(len(text))

#------------------------------------------------------------------------
# Task 6: Inside the call to "print" below, write an expression that evaluates
# to the position of the word "window" in the string defined in the variable
# called "aStringSentence." Use the .find() method.

aStringSentence = "Did the cat jump out the window yesterday?"
x = aStringSentence.find("window")
print(x)

#------------------------------------------------------------------------
# Task 7: Modify the print statement below so that it prints out the contents
# of the variable "partLy", but with all white space removed from
# the beginning and end of the string. Use the .strip() method.

partLy = "     someone who has spent too much time    \n"
x = partLy.strip("\t, \n")
print(x)

#------------------------------------------------------------------------
# Task 8: Using the previously defined "partLy" variable, write an
# expression inside the "print" function below that evaluates to the content of
# the string, with all whitespace removed, and with all letters converted to
# uppercase. Use the .upper() method.

y = partLy.strip().upper()
print(y) 

#------------------------------------------------------------------------

# Task 9: Modify the value assigned to variable "offset" below so that
# the following "print" statement displays the letter "p".

offset = 1
print("apple"[offset])

#------------------------------------------------------------------------

# Task 10: Modify the values assigned to variables "start" and "end"
# below so that the following "print" statement displays the word "jump".

start = 12
end = 16
aStringSentenceAgain = "Did the cat jump out the window yesterday?"
print(aStringSentenceAgain[start:end])

#------------------------------------------------------------------------

# Task 11: Modify the statement below so that it displays the number 100.
# Do this using the int() function (hint: you need to use it twice).

print(int("19") + int("81"))
#------------------------------------------------------------------------

# Task 12: Modify the code below to include a condition to print the statement  
# 'test_var is less than 200' for the current value of test_var. 
# Do not change the intial code, rather add to it
test_var = 90
if test_var > 200:	
	print("test_var is greater than 200!")
else:
	print("test_var is less than 200")
#------------------------------------------------------------------------

# Task 13: Modify the if statement below to print the statement
# 'the condition test passed'. Do not change the values of the varaibles.
test_var_three = 400
test_var_two = 800
if test_var_three > 200 and test_var_two > 400:	
	print("the condition test passed")
else:
	print("the condition test not passed")
#------------------------------------------------------------------------

# Task 14: A variable "greek" is defined below. The value of this variable
# is of type list. Change the expression below the variable definition so
# that it prints "alpha" (instead of "beta").

greek = ["alpha", "beta", "gamma", "delta", "epsilon"]
print(greek[0])

