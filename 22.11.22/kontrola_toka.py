# vozilo_u_pokretu = True
# brzina = 60

# if vozilo_u_pokretu == True:
#     print("vozilo se krece")
#     print("Proverite i brzinu")
#     if brzina > 50:
#         print("Prekoracena")
#     if brzina <= 50:
#         print("brzina je ok")

# proizvod = "duks"
# cena = 3000

# komanda = int(input("Unesite komandu:  "))


# if komanda == 1:
#     print("Prikazi proizvode")
#     print("Proizvod:  ", proizvod, "Cena: ", cena)
# if komanda == 2:
#     print("Kupovina")
#     stanje = int(input("Unesite stanje na racunu:  "))
#     if stanje >= cena:
#         print("Uspesna kupovina!")
#     if stanje < cena:
#         print("Neuspesna kupovina")
# if komanda == 3:
#     print("Izlaz")

broj = 5

if broj > 0:
    print("Broj je veci od nule")
else:
    print("Broj je nula")


cities = ["Berlin", "Paris", "Moscow"]
for e in range(len(cities)):
    cities[e]=cities[e]+"2"