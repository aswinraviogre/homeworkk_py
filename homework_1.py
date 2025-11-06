import random

rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3.0
sugar_qty = 2.5
oil_qty = 1.8

rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

final_total = rice_total + sugar_total + oil_total

print("Rice total:", rice_total)
print("Sugar total:", sugar_total)
print("Oil total:", oil_total)
print("Total bill (float):", final_total)

total_int = int(final_total)
print("Total bill (integer):", total_int)

total_str = str(final_total)
print("Total bill (string):", total_str)

delivery_charge = random.randint(5, 10)
final_bill = final_total + delivery_charge
print("Delivery charge:", delivery_charge)
print("Final bill including delivery:", final_bill)
