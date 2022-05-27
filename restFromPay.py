
nom = input().split(',')
cena = float(input())
reszta = []

while cena != 0:
    for i in reversed(nom):
        if float(i) > cena:
            pass
        else:
            reszta.append(float(i))
            cena = round(cena - float(i), 2) 
            break
        
print(len(reszta), reszta)