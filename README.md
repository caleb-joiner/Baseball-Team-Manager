# Baseball-Team-Manager
Python class project

Chapter 1: Intro to Python Programming
Chapter 2: How to Write Your First Programs

    Baseball Team Manager Case Study
    Calculate batting average
    - Create a program that displays a welcome message and calculates a player’s batting average.

    Specifications
    - The formula for calculating batting average is: average = hits / at_bats
    - The program should accept integer entries.
    - Assume the user will enter valid data.
    - The program should round the batting averages to a maximum of three decimal places.

Chapter 3: How to Code Control Statements

    Add a menu
    - Update the program so it allows the user to select options from a menu.

    Specifications
    - Assume the user will enter valid data.
    - Display an error message if the user chooses an invalid menu option.

Chapter 4: How to Define and Use Functions and Modules

    Use functions to organize the program
    - Update the program so it uses functions to organize the code so it’s easier to reuse and maintain.

    Specifications
    - Use a function to store the code that displays the menu.
    - Use a function to store the code that calculates the batting average.
    - Use a main function to store the rest of the code.
    - Assume the user will enter valid data.
    - If the user enters an invalid menu option, display an error message and display the menu again, so the user can clearly see the valid menu options.

Chapter 5: How to Test and Debug a Program

    Test and debug the program
    
    Specifications
    - Create a list of valid entries and the correct results for each set of entries. Then, make sure that the results are correct when you test with these entries.
    - Create a list of invalid entries. These should include entries that test the limits of the allowable values. Then, handle the invalid integers (such as negative integers and unreasonably large integers). In addition, make sure the user can’t enter data that doesn’t make sense (such as a player having more hits than at bats).
    - Don’t attempt to handle invalid entries that cause exceptions, such as the user entering a string like “x” for an integer value. You can do that after you read chapter 8.

Chapter 6: How to Work with Lists and Tuples

    Use a list to store the players
    - Update the program so that it allows you to store the players for the starting lineup. This should include the player’s name, position, at bats, and hits. In addition, the program should calculate the player’s batting average from at bats and hits.

    Specifications
    - Use a list of lists to store each player in the lineup.
    - Use a tuple to store all valid positions (C, 1B, 2B, etc).
    - Make sure that the user’s position entries are valid.

Chapter 7: How to Work with File I/O

    Use a file to save the data
    - Update the program so it reads the player data from a file when the program starts and writes the player data to a file anytime the data is changed.

    Specifications
    - Use a CSV file to store the lineup.
    - Store the functions for writing and reading the file of players in a separate module than the rest of the program.

Chapter 8: How to Handle Exceptions

    Handle exceptions
    - Thoroughly test the program and update it so it handles all exceptions that you encounter during testing.

    Specifications
    - Handle the exception that occurs if the program can’t find the data file.
    - Handle the exceptions that occur if the user enters a string where an integer is expected.
    - Handle the exception that occurs if the user enters zero for the number of at bats.

Chapter 9 and 10: How to Work with Numbers and How to Work with Strings

    Improve number and string formatting
    - Update the program to improve the formatting of the numbers and the strings.

    Specifications
    - Use the multiplication operator to make sure that horizontal separator lines use 64 characters.
    - Use spaces, not tabs, to align columns. This should give the program more control over how the columns are aligned.
    - Make sure the program always displays the batting average with 3 decimal places.
    - Display the positions by processing the tuple of valid positions.