#!/bin/bash
python3 disassembler.py $1
newfile=$(echo $1 | sed 's/\.machine//')
echo "You can find the disassembled values in $newfile"
