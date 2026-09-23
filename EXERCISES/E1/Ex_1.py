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
