
pal = input("is this a palindrome? : ")

pal1 = pal.lower()

s = pal1.replace(" ","").replace(".", "").replace(",","")
m =[]

for i in s:
    m.insert(0, i)

x = "".join(m)

if x == s:
    print("true")
else:
    print("false")

