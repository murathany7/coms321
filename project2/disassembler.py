with open('file.machine') as f:
    for line in f:
        if line.startswith('10001011000'):
            Rm = int(line.split(' ')[1][11:15], 2)
            Rn = int(line.split(' ')[1][22:26], 2)
            Rd = int(line.split(' ')[1][27:31], 2)
            print(f'ADD X{Rd}, X{Rn}, X{Rm}')
        elif line.startswith('1001000100'):
            Rn = int(line.split(' ')[1][22:26], 2)
            Rd = int(line.split(' ')[1][27:31], 2)
            Imm = int(line.split(' ')[1][11:23], 2)
            print(f'ADDI X{Rd}, X{Rn}, #{Imm}')
        elif line.startswith('10001010000'):
            Rm = int(line.split(' ')[1][11:15], 2)
            Rn = int(line.split(' ')[1][22:26], 2)
            Rd = int(line.split(' ')[1][27:31], 2)
            print(f'AND X{Rd}, X{Rn}, X{Rm}')

