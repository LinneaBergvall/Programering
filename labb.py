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

tal = int(input("Skriv ett tal: "))

while tal != secret_number:
    if tal > secret_number:
        försök += 1
        print("Haha! Du är fast i min loop!")
    else:
        försök += 1
        print("Haha! Du är fast i min loop!")
    tal = int(input("Skriv ett tal igen: "))
print(secret_number, "Bra jobbat. Du är inte fast längre!")
print("Du har fösökt", försök, "gånger. Hur dålig får man vara.")
