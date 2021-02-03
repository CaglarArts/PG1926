a = 0
b = input("Liste Girin:")
print(list(b.split(",")))
for i in list(b.split(",")):
    if int(i) % 2 != 0 and int(i) > a:
        a = int(i)