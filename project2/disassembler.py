file = open('file.machine', 'rb')
found_bytes = file.read(4)
line_count = 1
branch_targets = []
procedure_name = f'procedure{line_count}'
while found_bytes:
    i = int.from_bytes(found_bytes, byteorder='big')
    instruction = '{:032b}'.format(i)
    if instruction.startswith('10001011000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        print(f'ADD X{Rd}, X{Rn}, X{Rm}')
    elif instruction.startswith('1001000100'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        print(f'ADDI X{Rd}, X{Rn}, #{Imm}')
    elif instruction.startswith('10001010000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        print(f'AND X{Rd}, X{Rn}, X{Rm}')
    elif instruction.startswith('1001001000'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        print(f'ADDI X{Rd}, X{Rn}, #{Imm}')
    elif instruction.startswith('000101'):
        br_addr = int(instruction[6:32], 2)
        print(f'B {br_addr}')
    # TODO B.cond
    elif instruction.startswith('100101'):
        br_addr = int(instruction[6:32], 2)
        print(f'B {br_addr}')
    elif instruction.startswith('11010110000'):
        Rn = int(instruction[22:27], 2)
        print(f'BR {Rn}')
    elif instruction.startswith('10110101'):
        br_addr = int(instruction[8:28])
        Rt = int(instruction[27:32], 2)
        print(f'CBNZ {br_addr}, X{Rt}')
    elif instruction.startswith('10110100'):
        br_addr = int(instruction[8:28])
        Rt = int(instruction[27:32], 2)
        print(f'CBZ {br_addr}, X{Rt}')
    elif instruction.startswith('11001010000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        print(f'EOR X{Rd}, X{Rn}, X{Rm}')
    elif instruction.startswith('1101001000'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        print(f'EORI X{Rd}, X{Rn}, #{Imm}')
    elif instruction.startswith('11111000010'):
        Rn = int(instruction[22:27], 2)
        Rt = int(instruction[27:32], 2)
        dt_addr = int(instruction[11:20])
        print(f'LDUR X{Rn}, [X{Rt}, #{dt_addr}]')
    # TODO LSL
    # TODO LSR
    elif instruction.startswith('10101010000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        print(f'ORR X{Rd}, X{Rn}, X{Rm}')
    elif instruction.startswith('1011001000'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        print(f'ORRI X{Rd}, X{Rn}, #{Imm}')
    elif instruction.startswith('11111000000'):
        Rn = int(instruction[22:27], 2)
        Rt = int(instruction[27:32], 2)
        dt_addr = int(instruction[11:20])
        print(f'STUR X{Rn}, [X{Rt}, #{dt_addr}]')
    elif instruction.startswith('11001011000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        print(f'SUB X{Rd}, X{Rn}, X{Rm}')
    elif instruction.startswith('1101000100'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        print(f'SUBI X{Rd}, X{Rn}, #{Imm}')
    elif instruction.startswith('1111000100'):
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        Imm = int(instruction[10:22], 2)
        print(f'SUBIS X{Rd}, X{Rn}, #{Imm}')
    elif instruction.startswith('10011011000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        print(f'MUL X{Rd}, X{Rn}, X{Rm}')
    elif instruction.startswith('11101011000'):
        Rm = int(instruction[11:16], 2)
        Rn = int(instruction[22:27], 2)
        Rd = int(instruction[27:32], 2)
        print(f'SUBS X{Rd}, X{Rn}, X{Rm}')
    elif instruction.startswith('11111111101'):
        print('PRNT')
    elif instruction.startswith('11111111100'):
        print('PRNL')
    elif instruction.startswith('11111111110'):
        print('DUMP')
    elif instruction.startswith('11111111111'):
        print('HALT')

    found_bytes = file.read(4)
    line_count += 1
