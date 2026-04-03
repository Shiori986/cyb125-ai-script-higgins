# cyb125-ai-script-higgins
This is a sample script that was created by AI

# CYB126-ai-script-higgins

## Purpose 
This project is a script created for CYB 125.

Its purpose is to bring up a terminal and ask the user where their file location is that they want to generate a hash. If the 
location if is valid, the user should be able to generate an md5 hash, a sha1, sha256, and a sha512 hash. If the file location
is not valid, the user will find out when the system does not generate a hash but an error. 

## Language
This project was written in Pytthon.

## Tools Used
•	GitHub – Used for version control, storing the script, and tracking changes.
•	AI Tools Used – Used for debugging, clarifying Python behavior, and improving code readability.
•	Editor Used – Python-friendly code editor (such as VS Code, PyCharm, or IDLE) for writing and testing the script.

## How This Works – Step by Step (1, 2, 3)
1.	User Input The program asks the user for two things:
o	A file path
o	A hashing algorithm (md5, sha1, sha256, sha512)
2.	Hashing Process The script calls hash_file(), which:
o	Checks if the file exists
o	Creates a hashing object using the chosen algorithm
o	Reads the file in binary mode in 4096 byte chunks
o	Updates the hash with each chunk until the file is fully processed
3.	Output Once hashing is complete, the program prints the final hexadecimal hash value. If anything goes wrong (bad path, unsupported algorithm, permission issues), the script prints an error message instead of crashing.

## Security Review
This script was reviewed for the following concerns:

•	Unsafe output The script only prints a hash value or an error message. No sensitive data is exposed.
•	Dangerous commands No system level commands, shell execution, or destructive operations are used.
•	Hard coded secrets The script contains no passwords, API keys, or sensitive information.
•	File risks The script only reads files, never writes or modifies them. It also checks file existence before opening, reducing the chance of unexpected behavior.
Overall, the script is safe, minimal, and follows good practices for file handling and hashing.

## Improvements Made 

Change 1: The most important changes I made was just refining the comments so that they made sense. My thought process was that some programmer should be able to look at portions of my AI generated code and understand what it does. The original comments that Copilot had were sort of confusing so I had to make some adjustments.  As for improvement number 2, I did not really see where I could improve on, so no other improvements were made at this time. 

## What I Learned

•	How to use Python’s hashlib library to generate secure hash values.
•	Why reading files in chunks is important for performance and memory safety.
•	How to validate user input and handle exceptions cleanly.
•	The importance of checking file existence before opening it.
•	How to structure a Python script with a clear separation between functions and the main execution block.
•	How hashing algorithms differ and why some (like MD5) are outdated for security purposes but still useful for integrity checks.

