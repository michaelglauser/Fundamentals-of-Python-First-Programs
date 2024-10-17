Enter an input statement, using the input function at the shell prompt. When the prompt asks you for input, enter a number. Then attempt to add 1 to that number, observe the results, and explain what happened.

# Enter input statement
variable_1 = input("Enter an input: ")

# Add one to that number input 
variable_2 = variable_1 + 1

# Display the result
print(variable_2)


Enter an input: 
5
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    variable_2 = variable_1 + 1
TypeError: can only concatenate str (not "int") to str


** Process exited - Return Code: 1 **
Press Enter to exit terminal



This causes an error because you can't add a number to a string.