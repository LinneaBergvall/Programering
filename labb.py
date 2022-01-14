secret_number = 888

print(
"""
+================================+
| Välkommen till mitt spel!      |
| Skriv ett nummer och           |
| gissa vilket nummer jag        |
| har valt för dig.              |
| Så, vad är det hemliga nummret?|
+================================+
""")

försök = 0
#hur många försök du gjort

tal = int(input("Skriv ett tal: "))
#ber personen skriva in ett tal

while tal != secret_number:
    #så länge tal är skillt från sevret_number fortsätt
    if tal > secret_number:
        försök += 1
        print("Haha! Du är fast i min loop!")
        #är tal större än secert_number lägg till ett försök, skriv ut "Hahah du är fast i min loop" och fortsätt
    else:
        försök += 1
        print("Haha! Du är fast i min loop!")
        #är talet mindre fortsätt och skriv ut.
    tal = int(input("Skriv ett tal igen: "))
    #frågar igen
print(secret_number, "Bra jobbat. Du är inte fast längre!")
print("Du har fösökt", försök, "gånger. Hur dålig får man vara.")
#lyckas man träffa rätt så skriver den ut de två senaset print
