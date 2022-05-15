# 5 Mini Test

To challenge improving myself I completed the five mini test in Python. 

## Questions

1. Code a function called `first_div_16` 
  - ACCEPT two positive integers, n1 and n2, as inputs 
  - RETURN the first number in range(n1,n2) that is divisible by 16. 
  - HOWEVER, if no number in the range is divisible by 16 RETURN 0

2. Code a function called `halve_to_2` 
  - ACCEPT one numeric input. 
  - If the number <= 0, RETURN -1. 
  - If the number > 0, divide that integer over-and-over by 2 until it becomes smaller than 2. 
  - RETURN that smaller-than-2 number, e.g. input of 4 Will yield 1 (4->2->1), 5 yields 1.25 (5->2.5->1.25) etc.
 
3. Code a function called `string_expansion`
  - ACCEPT a non-empty string as input
  - RETURN a string that contains every other character, 2n+2 times, where n is the original index of the letter. e.g. Input of “Hello” should result in "HHlllllloooooooooo". Input of “ROBErt” should result in "RRBBBBBBrrrrrrrrrr".

4. Code a function called `item_count_from_index`.
  - ACCEPT two inputs, a list and an integer-index
  - RETURN a count (number) of how many times the item at that index appears in the list.
  - However, if the integer-index is out of bounds for the list RETURN the empty string (“”) (e.g. list of 3 items, index of 5 is out of bounds)

5. Code a function called `length_times_largest`.
  - ACCEPT a list as input
  - RETURN the length of the list times the largest integer (not float) in the list.
  - However, if the list does not contain an integer, RETURN the empty string (“”).

### Solutions


For each question, I created a file to solve the questions.

1. I used a while loop to solve the first question. To accept only positive integers, I set for the while loop the condition that the number must be greater than 0. While the condition is true, I used a for loop to iterate through the numbers in the range(n1,n2). Depending on the input, the function will return either the number divisible by 16 or return 0. 

2. I only accepted a numeric as input with the data type keyword' int'. Furthermore, I used the If-clause to check if n1 is smaller or equal to 0, and if it is true, the function returns -1. While n1 is greater or equal to 2, n1 will divide by 2 over and over until n1 is smaller than 2. After that, the function will return the number n1.

3. I only accept a non-empty string as input with the while loop. While the input is not empty, the function will assign the variable `new_string` to an empty string and a variable `n` to 0 (the index of the string). As long the variable `n` is smaller than the length of the input, the new string will contain every other character 2n+2 times. In the end, the output is the string `new_string`.

4. For this solution, I used the keyword `split()` to create a list by entering elements separated by space. To check if the input for the index is not an integer (ValueError) or out of bounds (IndexError), I used the command `try...except`. If the input is correct, it should return the quantity of the item at that index, and if not, it should return the string '""'.

5. Like solution 4, I also used the `split()` keyword to create a list of the input. I solved the question by using the `try...except` command. The while loop will iterate through the list, and If one of the items in the list is an integer, the function will append the integer into a new list. If the item is not an integer, the function will go to the next item from the list. After the list has been checked, the function will search for the highest number, `max`, and multiply it with the length of the list. The function return either the number or an empty string '""'.


### Dependencies

This python project does not have any external libraries. However, starting this program will only require a Python 3 version.

### Installing

The latest version of python can be installed on the website: https://www.python.org/downloads/.

### Executing program

Executing this python project requires only running the file on the python platform. Then, the user needs to rerun the file to repeat the project.

## Authors

Gianluca Cannone - https://github.com/gicanon

## License

Copyright (c) [2022] [Gianluca Cannone]

Permission is hereby granted, free of charge, to any person obtaining a copy of the project without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project, and to permit persons to whom the project is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of this project.

THE PROJECT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE PROJECT OR THE USE OR OTHER DEALINGS IN THE PROJECT.
