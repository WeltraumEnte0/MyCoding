# Liste von Transaktionen
transactions = [
    {"type": "purchase", "amount": 1551, "date": "2002-12-12"},
    {"type": "sale", "amount": 8001, "date": "2024-01-14"},
]

# Werte für die erste Transaktion extrahieren
transaction_type = transactions[0]["type"]
transaction_amount = transactions[0]["amount"]
transaction_date = transactions[0]["date"]

# Funktion zum Extrahieren von Werten für einen bestimmten Schlüssel in allen Transaktionen
def transdic(my_key):
    amount_values = [transaction[my_key] for transaction in transactions]
    return amount_values

# Funktion aufrufen, um alle Beträge zu extrahieren
print(transdic("amount"))

# Funktion zum Summieren der Beträge für einen bestimmten Transaktionstyp
def sum_up(my_type):
    amount_values = [transaction["amount"] for transaction in transactions if transaction["type"] == my_type]
    return sum(amount_values)

# Einkommen und Ausgaben berechnen
income = sum_up("purchase")
expenses = sum_up("sale")
print("Einkommen = ", income)
print("Ausgaben = ", expenses)

# Entscheidung, ob mehr Geld eingenommen oder ausgegeben wurde
if income > expenses:
    print("Du hast mehr Geld eingenommen.")
else:
    print("Du hast Geld verloren.")

# Aufgabe: Funktion zum Finden aller Transaktionen mit einem bestimmten Schlüssel-Wert-Paar
def find_all(my_key, my_value):
    values = [transaction for transaction in transactions if transaction[my_key] == my_value]
    return values

# Funktion aufrufen, um alle Transaktionen mit dem Datum "2024-01-14" zu finden
my_transactions = find_all("date", "2024-01-14")
print(my_transactions)
print(len(my_transactions))

# Funktion zum Überprüfen des Datumsformats
import re

def is_valid_date_format(date_string):
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')	
    return bool(date_pattern.match(date_string))

# Einzelnes Datum aus den gefundenen Transaktionen extrahieren und das Datum überprüfen
my_date = my_transactions[0]["date"]
print(my_transactions[0]['date'])
print(type(my_date))
print(is_valid_date_format(my_date))
