"""
© https://sudipghimire.com.np

Function Exercises
"""

"""
1. Write a python function to find the largest out of 3 numbers
You should use comparison operator to find out the maximum of 3 numbers.
"""
# answer


"""
2. Write a python function that calculates the number of upper case characters, lower case characters
 and spaces in the string and returns them as a tuple.

for example

x = "A Quick Brown Fox Jumps Over The Lazy Dog."

Number of upper case characters: 9
Number of lower case characters: 14
Number of spaces: 8
"""


'''
3.
Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee
according to the customer's requirements.

The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user.
Please use the `make_coffee()` function below to prepare a coffee and serve it.

Followings are the ingredients for coffee:

Sugar: no. of spoons
beans: no. of spoons
milk: volume in ml.

The total volume of coffee should be 250ml. The maximum volume of milk can be only upto  150ml. greater than that
should give the error saying not acceptable.

Finally print the line describing the coffee you prepared along with  milk and water composition.

'''
# answer


"""
4.
Write a program to create a multiplication table of the given number.
The `mul_table()` function should have the following arguments:
- `number`: the number to print multiplication table of.
- `limit`: the number upto which multiples are printed which should have the default value of 10

Multiplication table for 13

| 13  X   1|    13|
| 13  X   2|    26|
| 13  X   3|    39|
| 13  X   4|    52|
| 13  X   5|    65|
| 13  X   6|    78|
| 13  X   7|    91|
| 13  X   8|   104|
| 13  X   9|   117|
| 13  X  10|   130|

"""
# Answer Here


"""
5.
Write a function that takes a string and checks whether the word is palindrome or not.

- A palindrome is a string that reads the same backward or forward.
- Examples: eve, dad, rotator

Your program should be able to ask user to enter the word and check whether it is palindrome or not.
The program should not end until user enters no.
The program should start with the
The output should show inside a box as shown below with text justified center.



Example Output:

=============================[ Palindrome Finder ]=============================
Enter a word: rotator

+-----------------------------------------------------------------------------+
|                   The word 'rotator' is a palindrome                        |
+-----------------------------------------------------------------------------+

The word 'rotator' is a palindrome word

Do you want to check again? [yes/no]: yes

Enter a word: dad

+-----------------------------------------------------------------------------+
|                     The word 'dad' is a palindrome                          |
+-----------------------------------------------------------------------------+


Do you want to check again? [yes/no]: no

=================================[ exiting now ]================================

"""


"""
6.
Write a function that accepts words that are separated by hyphen returns the alphabetically sorted words
separated by hyphen.

Hint:
- split the words using string.split() method
- sort the list
- join the list to a string with string.join() method
"""

word = "cat-apple-dog-ball-ears-goose-fish"
def sort_words(word: str):
    # change your function body here
    return word

word = sort_words(word)
print(word)
# "apple-ball-cat-dog-ears-fish-goose"



"""
7.
Write a function that accepts a number x
- if x is a multiple of 2, it should return the value y = x**2 + 2x + 3
- if x is a multiple of 3, it should return the value y = x**3 + 4x + 5
- if x is a multiple of both 2 and 3, it should return the value y = x**3 + 4x**2 + 5x + 6
- in other cases it should return negative value of the given number
"""
# answer


"""
8.
Write a function that accepts any number of arguments
find out the sum of all numbers by multiplying by 2 if it is odd and dividing by 2 if the number is even.

Example if arguments are (5,6,7,8)

the result should be 31 [ 5*2 + 6/2 + 7*2 + 8/2 ]
"""
# answer
