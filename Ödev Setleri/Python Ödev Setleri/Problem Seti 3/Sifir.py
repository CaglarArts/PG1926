liste1 = []
liste2 = []
for i in range(7):
    sayi = int(input(str(i+1)+". Sayı = "))
    if sayi == 0:
        liste1.append(sayi)
    else:
        liste2.append(sayi)
print(liste1+liste2)
