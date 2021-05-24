# Programming Project 2
## Contributors njtucker@iastate.edu jpowell1@iastate.edu kstrozin@iastate.edu murathan@iastate.edu
For this project, the disassembling part was fairly simple. First, the program opens the .machine file if it exists and reads in 4 bytes at a time, or 32 bits. Then, it converts that line into a 32 length string of 1s and 0s for parsing. Now that we have this string, we can easily extract the opcode through an admiteddly large if-elif chain to check the first bits against known opcodes. Once you have the opcode found it's very easy to extract Rn, Rt, Rm, Branch offsets, etc.

## Run instructions
This is as easy as running `./build.sh` followed by `./run.sh` with the name of the .machine file as a command line arg in run.sh. It will generate a new .legv8asm file with the same name as the .machine file but with .machine removed.

## How on earth do we keep track of branch names?
With a separate list, of course! We keep a list of dictionary values of a line number and a corresponding name for that value, starting at 1, then 2, etc. The line number is easy to keep track of through the current instruction number plus the offset. If we've seen a target with this value before, we don't add it to the list. If it's new, we add it to the list. Then it's as easy as inserting the branch names into the final instructions based on the key of the dictionary, as we've been keeping track. ez pz

## Any known issues or bugs?
So far, the *only* known bug is that, sometimes, the branch target/procedure name is inserted in a line or two north or south of the expected line. It is able to keep track of how many there are no issue, what the names should be, and everything, but when it comes time to add them to the list, it gets just a line or two off *sometimes*. 
