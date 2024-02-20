# Password-Generator
A password generator application using python
Imports the random module: Provides functions for generating randomness.
Defines character sets:
lower: Lowercase letters for increased readability.
upper: Uppercase letters for enhanced strength.
number: Numbers for wider character variety.
symbols: Symbols for maximum complexity (optional).
Creates the string: Combines all character sets based on user input.
Gets password length and validates: Prompts the user to enter the desired password length, ensuring it's a positive integer.
Generates random password:
random.sample(string, length) takes a random sample of length characters from the string.
"".join(password) concatenates the list of characters into a string.
Prints the password: Displays the generated password to the user.
