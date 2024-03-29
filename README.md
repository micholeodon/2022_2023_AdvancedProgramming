# Advanced Programming (NCU, Cognitive Science)


  * Python Online Cheatsheet: https://www.pythoncheatsheet.org/

  * Python Printable Cheatsheet: https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf

### MEETING nr 4 (28.04.2023)

**Exercise 1. Parrot**. The program allows you to enter some text and then it writes it to a `parrot.txt` file (created if needed).

Operation scheme:

1. The program asks for some input text,
    
1. The program prints the text on the screen,
    
1. The program writes the text to a `parrot.txt` file, which should be placed inside the script's directory.	


**Exercise 2. Movies**

The program that saves user data into a CSV file - https://en.wikipedia.org/wiki/Comma-separated_values

1. Program asks for a number of data records user want to enter (positive integer; number of rows in the file),
1. Next user inputs: movie name, 
1. Next user inputs: numerical value from 1.0 to 10.0,
1. Two requests above are repeated as many times as the number of rows,
1. All the data is saved in `movies.csv`, 
1. At the end, the content of the file is displayed on the screen.
1. Example content:

```
No.,Title,Rating
1,Inception,8.3
2,Room,2.9
3,Matrix,7.6
4,Pianist,8.3
5,Dune,7.7
6,Paterson,7.1
```
Notice the header!


**Exercise 3. Learning Time!**

Write a program that helps with studying.

The user can prepare his own set of questions and correct answers in a text file. Each text file can contain questions from different disciplines.
For each questions there should be only one correct answer.

Program should:

1. Ask user to input the name of the file to be loaded,
1. Load selected file,
1. Ask user how many questions to ask,
1. Ask **randomly** chosen question from the file,
1. Ask user to give an answer,
1. Check whether the answer is correct. 
1. If correct: add 1 point to the total score, 
1. If incorrect: show correct answer. No points are added.
1. After asking the specified number of questions the summary should be displayed. 
The summary should contain: number of asked questions, number of correct answers, percent of correct answers and (optionally) show questions that were answered incorrectly.


**Exercise 4. DecisionTree Class**

Write a program that can load data from a CSV file (e.g., iris dataset - https://gist.github.com/netj/8836201) and perform a decision tree classification. Functions and variables related to decision tree should be enapsulated within a separate class. 


### MEETING nr 2 (31.03.2023)

**Exercise 1. Calculator**. The program allows you to enter two real numbers and perform four operations: `+`, `-`, `*`, `/`, corresponding to addition, subtraction, multiplication, and division. The program calculates four results of all the operations performed on the two numbers specified by the user and displays them.

Operation scheme:

1. The program asks for the first number,
    
1. The program asks for the second number,
    
1. The program shows what operations it will perform,
    
1. The program calculates four results,
    
1. The program display each result.
    
1. Important! Program should detect division by zero and inform politely the user about this fact.
	
	

**Exercise 2. Find x**. The program is to find the solution of the equation `ax + b = c`. The parameters `a`, `b`, `c` are given by the user. Let the program run as follows:

1. First, it will display the text "ax + b = c".

2. Then it will ask the user to specify the real numbers a, b, c.

3. It will display the equation "ax + b = c" with the substituted numerical values.

4. The program calculates the value of x.

5. Will display the result.



