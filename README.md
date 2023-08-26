# 30-Day Python Challenge

This repository contains a collection of tasks completed during the 30-day Python challenge. Each day's task is designed to reinforce and expand Python programming skills progressively.

## Day 0: Hello, World!

### Objective
In this challenge, we revisited some basic concepts to get started with the series. The challenge involved reading input, writing output, and using variables.

### Task
To complete this challenge:
- Read a line of input from stdin and save it to a variable.
- Print "Hello, World." on one line.
- Print the value of the variable on the next line.

**Input Format**: A single line of text denoting the variable.

**Output Format**: 
```
Hello, World.
<value of the variable>
```

### Example
**Input**
```
Welcome to 30 Days of Code!
```
**Output**
```
Hello, World.
Welcome to 30 Days of Code!
```

## Day 1: Data Types

### Objective
This challenge focuses on working with different data types.

### Task
You must:
- Declare variables of different types: int, double, and String.
- Read input and initialize the variables accordingly.
- Perform various operations involving these variables.

**Input Format**:
- The first line contains an int to be summed with an int variable.
- The second line contains a double to be summed with a float variable.
- The third line contains a string to be concatenated with another string.

**Output Format**:
- First line: Sum of integers.
- Second line: Sum of doubles (rounded to one decimal place).
- Third line: Concatenated strings.

### Example
**Input**
```
12
4.0
is the best place to learn and practice coding!
```
**Output**
```
16
8.0
HackerRank is the best place to learn and practice coding!
```

## Day 2: Operators

### Objective
This challenge involves working with arithmetic operators.

### Task
Given the cost of a meal, tip percent, and tax percent, calculate and print the total cost of the meal rounded to the nearest integer.

**Input Format**:
- The first line contains the cost of the meal (as a double).
- The second line contains the tip percentage (as an integer).
- The third line contains the tax percentage (as an integer).

**Output Format**: Total cost of the meal (rounded to the nearest integer).

### Example
**Input**
```
12.00
20
8
```
**Output**
```
15
```

## Day 3: Introduction to Conditional Statements

### Objective
This challenge introduces conditional statements.

### Task
Given an integer, perform different actions based on the value:
- If odd, print "Weird".
- If even and in the range of 2 to 5 (inclusive), print "Not Weird".
- If even and in the range of 6 to 20 (inclusive), print "Weird".
- If even and greater than 20, print "Not Weird".

**Input Format**: A single positive integer.

**Output Format**: Print corresponding message.

### Example
**Input**
```
3
```
**Output**
```
Weird
```

## Day 4: Classes vs Instances

### Objective
Learn the difference between a class and an instance.

### Task
Write a `Person` class with an age instance variable and a constructor. Handle negative age values and implement methods to:
- Increment age.
- Determine if a person is young, a teenager, or old.

**Input Format**:
- The first line contains an integer, T (number of test cases).
- The subsequent T lines each contain an integer representing a Person's age.

**Output Format**: Messages based on age classification.

### Example
**Input**
```
4
-1
10
16
18
```
**Output**
```
Age is not valid, setting age to 0.
You are young.
You are young.
You are a teenager.
You are a teenager.
You are old.
You are old.
You are old.
```

## Day 5: Loops

### Objective
This challenge focuses on loops in Python.

### Task
Print the multiples of a given integer up to 10.

**Input Format**: An integer.

**Output Format**: Multiples of the integer up to 10.

### Example
**Input**
```
2
```
**Output**
```
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
```
