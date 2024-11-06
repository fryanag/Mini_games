# 3. Looping 

# for statement 
# index data dimulai dari 0
i = 0
for i in range(10):
    i + 1 
    print(i)

for baris in range(5):
  for kolom in range(5):
      print("*", end="")
print()
print("===========")


 # while iteration -> need conditions
baris2 = 0
tengah = 5
kolom2 = 0
while baris2 < 5 :
        if(baris2 % 2 == 1):
            while kolom2 < 5:
                if(kolom2 == int(round(tengah/2))):
                     print("*",end="")
                else:
                    print("*",end="")
                kolom2 += 1
else:
    while kolom2 < 5:
        print("*",end="")
        kolom2 += 1
print()
baris2 += 1