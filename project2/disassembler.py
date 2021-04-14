import json

file = open('fib.legv8asm.machine', 'rb')
found_bytes = file.read(4)
line_count = 1
branch_targets = []
instructions = []

branch_conditionals = {0: 'EQ', 1: 'NE', 2: 'HS', 3: 'LO', 4: 'MI', 5: 'PL', 6: 'VS', 7: 'VC',
                       8: 'HI', 9: 'LS', 10: 'GE', 11: 'LT', 12: 'GT', 13: 'LE'}

while found_bytes:
    print(branch_targets)
    i = int.from_bytes(found_bytes, byteorder='big')
    instruction = '{:032b}'.format(i)
    if instruction.startswith('10001011000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        instructions.append(f'ADD X{Rd}, X{Rn}, X{Rm}')

    elif instruction.startswith('1001000100'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        instructions.append(f'ADDI X{Rd}, X{Rn}, #{Imm}')

    elif instruction.startswith('10001010000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        instructions.append(f'AND X{Rd}, X{Rn}, X{Rm}')

    elif instruction.startswith('1001001000'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        instructions.append(f'ADDI X{Rd}, X{Rn}, #{Imm}')

    elif instruction.startswith('01010100'):
        Rt = int(instruction[27:32], 2)
        br_addr = int(instruction[9:27], 2)

        if not any(branch.get(line_count + br_addr) for branch in branch_targets):
            print(f'FOUND A NEW BRANCH TARGET IN BR AT LINE {line_count} called {br_addr + line_count}')
            branch_targets.append({line_count + br_addr: f'$procedure{len(branch_targets) + 1}'})
        else:
            print(f'WE KNOW THIS BRANCH ALREADY, IT IS {[branch.get(line_count + br_addr) for branch in branch_targets]}')

        cond = branch_conditionals[Rt]
        instructions.append(f'BR {[b.get(line_count + br_addr) for b in branch_targets if b.keys() is line_count + br_addr]}')

    elif instruction.startswith('000101'):
        br_addr = int(instruction[6:32], 2)

        if not any(branch.get(line_count + br_addr) for branch in branch_targets):
            print(f'FOUND A NEW BRANCH TARGET IN B AT LINE {line_count} called {br_addr + line_count}')
            branch_targets.append({line_count + br_addr: f'$procedure{len(branch_targets) + 1}'})
        else:
            print(f'WE KNOW THIS BRANCH ALREADY, IT IS {[branch.get(line_count + br_addr) for branch in branch_targets]}')

        instructions.append(f'B {[b.get(line_count + br_addr) for b in branch_targets if b.keys() is line_count + br_addr]}')

    elif instruction.startswith('100101'):
        br_addr = int(instruction[6:32], 2)

        if not any(branch.get(line_count + br_addr) for branch in branch_targets):
            print(f'FOUND A NEW BRANCH TARGET IN BL AT LINE {line_count} called {br_addr + line_count}')
            branch_targets.append({line_count + br_addr: f'$procedure{len(branch_targets) + 1}'})
        else:
            print(f'WE KNOW THIS BRANCH ALREADY, IT IS {[branch.get(line_count + br_addr) for branch in branch_targets]}')

        instructions.append(f'BL {[b.get(line_count + br_addr) for b in branch_targets if b.keys() is line_count + br_addr]}')

    elif instruction.startswith('11010110000'):
        Rn = int(instruction[22:27], 2)
        # TODO not sure how to handle this, need to RTFM
        instructions.append(f'BR {Rn}')

    elif instruction.startswith('10110101'):
        br_addr = int(instruction[8:28])
        Rt = int(instruction[27:32], 2)

        if not any(branch.get(line_count + br_addr) for branch in branch_targets):
            print(f'FOUND A NEW BRANCH TARGET IN CBNZ AT LINE {line_count}')
            branch_targets.append({line_count + br_addr: f'$procedure{len(branch_targets) + 1}'})
        else:
            print(f'WE KNOW THIS BRANCH ALREADY, IT IS {[branch.get(line_count + br_addr) for branch in branch_targets]}')

        instructions.append(f'CBNZ {[b.get(line_count + br_addr) for b in branch_targets if b.keys() is line_count + br_addr]}')

    elif instruction.startswith('10110100'):
        br_addr = int(instruction[8:28])
        Rt = int(instruction[27:32], 2)

        if not any(branch.get(line_count + br_addr) for branch in branch_targets):
            print(f'FOUND A NEW BRANCH TARGET IN CBZ AT LINE {line_count}')
            branch_targets.append({line_count + br_addr: f'$procedure{len(branch_targets) + 1}'})
        else:
            print(f'WE KNOW THIS BRANCH ALREADY, IT IS {[branch.get(line_count + br_addr) for branch in branch_targets]}')

        instructions.append(f'CBZ {[b.get(line_count + br_addr) for b in branch_targets if b.keys() is line_count + br_addr]}')

    elif instruction.startswith('11001010000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        instructions.append(f'EOR X{Rd}, X{Rn}, X{Rm}')

    elif instruction.startswith('1101001000'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        instructions.append(f'EORI X{Rd}, X{Rn}, #{Imm}')

    elif instruction.startswith('11111000010'):
        Rn = int(instruction[22:27], 2)
        Rt = int(instruction[27:32], 2)
        dt_addr = int(instruction[11:20])
        instructions.append(f'LDUR X{Rn}, [X{Rt}, #{dt_addr}]')
    # TODO LSL
    # TODO LSR
    elif instruction.startswith('10101010000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        instructions.append(f'ORR X{Rd}, X{Rn}, X{Rm}')

    elif instruction.startswith('1011001000'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        instructions.append(f'ORRI X{Rd}, X{Rn}, #{Imm}')

    elif instruction.startswith('11111000000'):
        Rn = int(instruction[22:27], 2)
        Rt = int(instruction[27:32], 2)
        dt_addr = int(instruction[11:20])
        instructions.append(f'STUR X{Rn}, [X{Rt}, #{dt_addr}]')

    elif instruction.startswith('11001011000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        instructions.append(f'SUB X{Rd}, X{Rn}, X{Rm}')

    elif instruction.startswith('1101000100'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        instructions.append(f'SUBI X{Rd}, X{Rn}, #{Imm}')

    elif instruction.startswith('1111000100'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        instructions.append(f'SUBIS X{Rd}, X{Rn}, #{Imm}')

    elif instruction.startswith('10011011000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        instructions.append(f'MUL X{Rd}, X{Rn}, X{Rm}')

    elif instruction.startswith('11101011000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        instructions.append(f'SUBS X{Rd}, X{Rn}, X{Rm}')

    elif instruction.startswith('11111111101'):
        instructions.append('PRNT')

    elif instruction.startswith('11111111100'):
        instructions.append('PRNL')

    elif instruction.startswith('11111111110'):
        instructions.append('DUMP')

    elif instruction.startswith('11111111111'):
        instructions.append('HALT')

    found_bytes = file.read(4)
    line_count += 1


# print(*instructions, sep='\n')
