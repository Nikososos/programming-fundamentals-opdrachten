# Maak een lijst van studenten geordend in tuples met naam en cijfer
studenten = [("David", 7.7), ("Lisa", 9.6), ("Ezra", 4.5), ("Wouter", 5.6)]

# Gebruik een for loop om de naam en cijfer van studenten netjes uit te printen

print("Studenten en hun cijfers: ")
for naam, cijfer in studenten:
    print(f"{naam} - {cijfer}")

# Bereken de gemiddelde score van alle studenten

lijst_leerlingen, lijst_score = zip(*studenten)
gemiddelde_score = sum(lijst_score) / len(lijst_leerlingen)

print(f"De gemiddelde score van alle studenten is {gemiddelde_score}")

# Geef weer wie het hoogste cijfer heeft gehaald

hoogste_cijfer = max(studenten, key=lambda x: x[1])
hoogste_cijfer_naam, hoogste_cijfer_score = hoogste_cijfer

print(f"De beste student is {hoogste_cijfer_naam} met een {hoogste_cijfer_score}")
