# while iteration -> need conditions

baris2 = 0
tengah = 5
while baris2 < 5:
    kolom2 = 0
    if(baris2 % 2 == 1):
        while kolom2 < 5:
            if (kolom2 == int(round(tengah/2))):
                print("*",end="")
            else:
                print(" ",end="")
            kolom2 += 1
    else:
        while kolom2 < 5:
            print("*",end="")
            kolom2 += 1
    print()
    baris2 += 1

    #trial

    baris2 = 0
tengah = 5
while baris2 < 5:
    kolom2 = 0
    if(baris2 % 2 == 1):
        while kolom2 < 5:
            if (kolom2 == int(round(tengah/2))):
                print("*",end="")
            else:
                print(" ",end="")
            kolom2 += 1
    else:
        while kolom2 < 5:
            print("*",end="")
            kolom2 += 1
    print()
    baris2 += 1