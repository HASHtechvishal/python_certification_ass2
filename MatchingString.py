#Matching Specific String
# importing the re module
import re

# taking input from user
n = int(input())

# using user defined function
def check_replacement_required(match):
    
    # using if else statements to check
    st = str(match.group(0))
    if st == "||":
        return "or"
    elif st == "&&":
        return "and"

# using for loop to 
for i in range(n):
    
    # taking input from user and calling the function
    s = input()
    p = "(?<=[ ])[|]{2}(?=[ ])|(?<=[ ])[&]{2}(?=[ ])"
    print(re.sub(p, check_replacement_required, s))