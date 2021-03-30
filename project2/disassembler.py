with open('file.machine') as f:
    for line in f:
        if line.startswith('10001011000'):
            Rm = int(line.split(' ')[1][11:16], 2)
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            print(f'ADD X{Rd}, X{Rn}, X{Rm}')
        elif line.startswith('1001000100'):
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            Imm = int(line.split(' ')[1][10:22], 2)
            print(f'ADDI X{Rd}, X{Rn}, #{Imm}')
        elif line.startswith('10001010000'):
            Rm = int(line.split(' ')[1][11:16], 2)
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            print(f'AND X{Rd}, X{Rn}, X{Rm}')
        elif line.startswith('1001001000'):
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            Imm = int(line.split(' ')[1][10:22], 2)
            print(f'ADDI X{Rd}, X{Rn}, #{Imm}')
        elif line.startswith('000101'):
            br_addr = int(line.split(' ')[1][6:32], 2)
            print(f'B {br_addr}')
        # TODO B.cond
        elif line.startswith('100101'):
            br_addr = int(line.split(' ')[1][6:32], 2)
            print(f'B {br_addr}')
        # TODO BR
        elif line.startswith('10110101'):
            br_addr = int(line.split(' ')[1][8:28])
            Rt = int(line.split(' ')[1][27:32], 2)
            print(f'CBNZ {br_addr}, X{Rt}')
        elif line.startswith('10110100'):
            br_addr = int(line.split(' ')[1][8:28])
            Rt = int(line.split(' ')[1][27:32], 2)
            print(f'CBZ {br_addr}, X{Rt}')
        elif line.startswith('11001010000'):
            Rm = int(line.split(' ')[1][11:16], 2)
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            print(f'EOR X{Rd}, X{Rn}, X{Rm}')
        elif line.startswith('1101001000'):
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            Imm = int(line.split(' ')[1][10:22], 2)
            print(f'EORI X{Rd}, X{Rn}, #{Imm}')
        elif line.startswith('11111000010'):
            Rn = int(line.split(' ')[1][22:27], 2)
            Rt = int(line.split(' ')[1][27:32], 2)
            dt_addr = int(line.split(' ')[1][11:20])
            print(f'LDUR X{Rn}, [X{Rd}, #{dt_addr}]')
        # TODO LSL
        # TODO LSR
        elif line.startswith('10101010000'):
            Rm = int(line.split(' ')[1][11:16], 2)
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            print(f'ORR X{Rd}, X{Rn}, X{Rm}')
        elif line.startswith('1011001000'):
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            Imm = int(line.split(' ')[1][10:22], 2)
            print(f'ORRI X{Rd}, X{Rn}, #{Imm}')
        elif line.startswith('11111000000'):
            Rn = int(line.split(' ')[1][22:27], 2)
            Rt = int(line.split(' ')[1][27:32], 2)
            dt_addr = int(line.split(' ')[1][11:20])
            print(f'STUR X{Rn}, [X{Rd}, #{dt_addr}]')
        elif line.startswith('11001011000'):
            Rm = int(line.split(' ')[1][11:16], 2)
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            print(f'SUB X{Rd}, X{Rn}, X{Rm}')
        elif line.startswith('1101000100'):
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            Imm = int(line.split(' ')[1][10:22], 2)
            print(f'SUBI X{Rd}, X{Rn}, #{Imm}')
        # TODO SUBIS
        elif line.startswith('10011011000'):
            Rm = int(line.split(' ')[1][11:16], 2)
            Rn = int(line.split(' ')[1][22:27], 2)
            Rd = int(line.split(' ')[1][27:32], 2)
            print(f'MUL X{Rd}, X{Rn}, X{Rm}')


