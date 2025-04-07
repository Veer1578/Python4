amount = int(input("Enter the amount to be withdrawn "))

#Calculating the number of notes for different denominations
notes1 = amount//100
notes2 = (amount%100)//50
notes3 = ((amount%100)%50)//10

print(f"The amount of 100 rupees notes are {notes1}")
print(f"The amount of 50 rupees notes are {notes2}")
print(f"The amount of 10 rupees notes are {notes3}")