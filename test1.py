def decimal_to_bin(n):
    n = str(float(n))
    n = n.split('.')
    while(int(n[0]) >= 0):
        if int(n[1]) == 0:
            n = bin(int(n[0]))
            return n
        else: 
            whole_bin = bin(int(n[0]))

            fract = "0." + n[1]
            fract_float = float(fract)

            fract_bin = ""
            while True:
                fract_float *= 2

                fract_split = str(fract_float).split(".")
                if fract_float == 1.00:
                    fract_bin += "1"
                    break
                else:
                    fract_bin += fract_split[0]
                    fract_float = float("0." + fract_split[1])

                if len(fract_bin) == 20:
                    break
            return whole_bin + "." + fract_bin
    return "This calculator currently doesn't negative decimals"

def decimal_to_octal(n):
    n = str(float(n))
    n = n.split('.')
    while(int(n[0]) >= 0):
        if int(n[1]) == 0:
            n = oct(int(n[0]))
            return n
        else: 
            whole_bin = oct(int(n[0]))

            fract = "0." + n[1]
            fract_float = float(fract)

            fract_bin = ""
            while True:
                fract_float *= 8

                fract_split = str(fract_float).split(".")
                if int(fract_split[0]) in range(1,7+1) and int(fract_split[1]) == 0:
                    fract_bin += fract_split[0]
                    break
                else:
                    fract_bin += fract_split[0]
                    fract_float = float("0." + fract_split[1])

                if len(fract_bin) == 20:
                    break
            return whole_bin + "." + fract_bin
    return "This calculator currently doesn't negative decimals"

def decimal_to_hex(n):
    n = str(float(n))
    n = n.split('.')
    dict_hex = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
    while(int(n[0]) >= 0):
        if int(n[1]) == 0:
            n = hex(int(n[0]))
            return n
        else: 
            whole_bin = hex(int(n[0]))

            fract = "0." + n[1]
            fract_float = float(fract)

            fract_bin = ""
            while True:
                fract_float *= 16

                fract_split = str(fract_float).split(".")
                if int(fract_split[0]) in range(1,15+1) and int(fract_split[1]) == 0:
                    fract_bin += fract_split[0]
                    break
                elif int(fract_split[0]) in dict_hex:
                    fract_bin += dict_hex[int(fract_split[0])]
                    fract_float = float("0." + fract_split[1])
                else:
                    fract_bin += fract_split[0]
                    fract_float = float("0." + fract_split[1])

                if len(fract_bin) == 20:
                    break
            n = whole_bin[2:] + "." + fract_bin
            n = n.upper()
            n = "0x" + n
            return n
    return "This calculator currently doesn't negative decimals"    

while True:
    print("=========================================================")
    print("Simple Number System Converter")
    print("=========================================================")
    print("1. Decimal to binary")
    print("2. Decimal to octal")
    print("3. Decimal to hexadecimal")
    print("4. Exit")
    choice = input("Enter your choice (1-3): ")

    match choice:
        case '1':
            print("\n#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb#")
            try:    
                n = float(input("Enter decimal number (Positive Decimals Only): "))
                bin_hasil = decimal_to_bin(n)
                print(f"Decimal-to-binary: {bin_hasil}")   
            except ValueError:
                print("Please enter a valid input!")
            print("#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb#\n")
        case '2':
            print("\n#ooooooooooooooooooooooooooooooooooooooooooooooooooooooo#")
            try:
                n = float(input("Enter decimal number (Positive Decimals Only): "))
                oct_hasil = decimal_to_octal(n)
                print(f"Decimal-to-octal: {oct_hasil}")
            except ValueError:
                print("Please enter a valid input!")
            print("#oooooooooooooooooooooooooooooooooooooooooooooooooooooooo#\n")
        case '3':
            print("\n#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#")
            try:
                n = float(input("Enter decimal number (Positive Decimals Only): "))
                hex_hasil = decimal_to_hex(n)
                print(f"Decimal-to-hexadecimal: {hex_hasil}")
            except ValueError:
                print("Please enter a valid input!")
            print("#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#\n")
        case '4':
            print("Thank you for using this calculator")
            break
        case _:
            print("Please enter a valid Input!")