# smartprix_Interview_coding_questions
There were two questions in smartprix interviews: 1) Keystrokes and 2) Smart Assembly Language.
Unfortunately, I was unable to clear all the test cases. I have been able to come up with partial solution for both the problems,
looking for some help in sorting out the corner cases and few implementations.

1) Keystrokes
Operations::
'#' means add following characters in newline.
'@' simulates the behavior of the Caps Lock.
'^' move cursor up to insert the following character. If already on first line, then nothing needs to be done.
'?' move cursor down to insert the following character/operation. If already on last line, then nothing needs to be done.
'>' moves cursor right to one column to insert the following characters/operations. If already on the end column of the row,
    then nothing needs to be done.
'<' moves cursor left to one column to insert the following characters/operations. If already on the start column of the row, 
    then nothing needs to be done.
'/' same as left shift with few exceptions. 1) deletes the character while moving left. 2) If row is empty, then deletes the row
    and starts at the end of above row. If at first row, which turns out to be empty then nothing needs to be done.
'alphanumeric characters' inserts at the current position of the cursor.    

eg:
input: asd#fgh@qe^^@fy?t
output: asfyd
        fght
        QE

2) Smart Assembly Language
Operations:
'SET a 1' -> declares variable 'a' and initializes it to 1.
'ECHO a' -> outputs value of a to the console.
'ADD a 1 a' -> adds 1 to the a and store it in a.
'LABEL 100' -> creates a label for the following code so that it can be called using 'GOTO 100'. It is kind of like a loop.
'GOTO 100' -> moves the execution of the code to the line following 'LABEL 100'.
'EXIT' -> exits the operations. If in loop, exits the loop, else the execution of code.
'IF a 5' -> starts a if block with if condition checking 'a' equals to 5 or not. There may be one or more following statements(inside if-block) to be executed
             if condition is true.
'END' -> ends if block.
'CONTINUE' -> same as 'continue' in higher programming language. 
