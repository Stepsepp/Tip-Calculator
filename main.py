# Prindib tervituse kasutajale.
print("Hello")

# Küsib kasutajalt arve kogusummat ja teisendab sisendi ujukomaarvuks (float).
bill = float(input("What was the total bill? $"))

# Küsib kasutajalt, millist protsenti jootraha soovitakse jätta, ja teisendab sisendi täisarvuks (int).
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Küsib kasutajalt, mitme inimese vahel arvet jagada, ja teisendab sisendi täisarvuks (int).
people = int(input("How many people to split the bill? "))

# Arvutab jootraha protsendi arvuliselt.
tip_as_percent = tip / 100

# Arvutab jootraha kogusumma.
total_tip_amount = bill * tip_as_percent

# Lisab jootraha kogusumma arve kogusummale, et saada arve lõppsumma.
total_bill = bill + total_tip_amount

# Jagab arve lõppsumma inimeste arvu vahel, et leida ühe inimese makstav summa.
bill_per_person = total_bill / people

# Ümardab ühe inimese makstava summa kahe kümnendkoha täpsusega.
final_amount = round(bill_per_person, 2)

# Prindib lõppsumma, mida iga inimene peaks maksma.
print(f"Each person should pay: ${final_amount}")
