a=int(input("Başlangıç Sayısını Giriniz:"))
b=int(input("Bitiş Sayısını Giriniz:"))
for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
