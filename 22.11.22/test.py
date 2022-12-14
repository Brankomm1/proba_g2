pozicija_automobila = 0
pozicija_cilja = 10

pozicija_automobila += 2
print(pozicija_automobila== pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila== pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila== pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila== pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila== pozicija_cilja)




for ime in ["marko", "milos", "marija", "ana", "pera"]:
    print("Hello", ime)

print("Prva sledeca linija....")

for broj in [1,2,3,4,5]:
    print("Ovo je broj: ", broj)




for broj in range(5, 10, 3):
    print("Stampanje broja: ", broj)


for broj in range(100, 0, -1):
    print("Prikaz", broj)


pozicija_automobila = 0
pozicija_cilja = 10

for kretanje in range(5):
    pozicija_automobila +=2
    print(pozicija_automobila == pozicija_cilja)


startDate = 2010
endDate = 2015

for godina in range(startDate, endDate):
    print("Godina:", godina)

for _ in range(50):
    print("*", end="")

print()

print("1\t2\t3\t")
print("*******************")



# zeljeni_broj = int(input("Zeljeni broj : "))

# for brojac in range(1, zeljeni_broj +1):
#     print(brojac*1, end="\t")
#     print(brojac*2, end="\t")
#     print(brojac*3, end="\n")


for x in range(5):
    for y in range(3):
        print("ovo je x:", x,"Ovo je y", y)




print()

for x in range(6):
    for y in range(6):
        print("*", end="")
    print()


for x in range(6):
    for y in range(6):
            print("*" if x == y else "#", end="")
    print()


#simbol = "*" if x == y else "#"




for x in range(10):
    for y in range(10):
        if x== 0 or x== 9 or y==0 or y==9:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()

import random
sekunde = 10

# while sekunde > 0:
#     print(sekunde)
#     sekunde -=1

baterija = 90

while baterija >0:
    print("Mozes koristiti tel:", baterija,"%")
    baterija -= random.randint(5,20)

print("Baterija je prazna")


for broj in range(11):
    if broj ==2:
        continue
    print(broj)

print()

for x in range(1,7):
    for y in range(5):
        print("#", end=" ")
    print()

print()


for x in range(10):
    for y in range(10):
        if y>x:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()



automobil = 0
cilj = 100
gorivo = 120
while automobil < cilj:
    print("Voznja u toku", automobil,"km:")
    automobil +=10
    gorivo -=5
    if gorivo == 0:
        break
else:
    print("stigli ste")




osoba = ["Sofija", 20, "plava", True]
print(osoba)

print(osoba[0])
print("Godine: ",osoba[1])



automobili=["Opel","Mercedes","Audi"]
print(automobili[1])

for x in range(5,10,2):
    print(x)

print()



kurs = "python"


for x in range(len(kurs)):
    print("Na poziciji: ",x , kurs [x])

ustanova = "IT Academy"

for index in range(len(ustanova)):
    print(ustanova[index])


print()

primer = "zadatak1"

for x in range(len(primer)):
    print(primer[x])

broj_karaktera = len(primer)
index = 0

while index < len(primer):
    print(primer[index])
    index +=1


korisnicko_ime = "admin"
uneto_ime = input("Unesi ime: ")

if korisnicko_ime == uneto_ime.lower():
    print("Dobrodosli")
else:
    print("Pogresni podaci")