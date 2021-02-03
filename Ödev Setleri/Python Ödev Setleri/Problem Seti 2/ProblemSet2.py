list0 = []
list1 = []
mail = input("E-posta Adresinizi Giriniz: ")

def dogrula(mail):
    global list0, list1
    result = True
    for i in mail:
        if i == "@":
            list0 = mail.split("@")
    for i in list0[1]:
        if i == ".":
            list1 = list0[1].split(".")
    for k in list0[0]:
        for i in list(range(32,45)) + list(range(46,48)) + list(range(58, 65)) + list(range(91,95)) + list(range(96,97)) + list(range(123,226)):
            if k == chr(i):
                result = False
    for k in list1[0] + list1[1] + list1[2]:
        for i in list(range(32,48)) + list(range(58, 65)) + list(range(91,97)) + list(range(123,226)):
            if k == chr(i):
                result = False
    return result

if dogrula(mail) == True:
    print("Mail Adresi Uygundur")
else:
    print("Mail Adresi Uygun Değildir")