txt = "The best things in life are free!"
print( "ORIGN: " + txt )

y = input("Enter a word or 'free':")

if y in txt:
  print("Yes, '" + y + "' is present.")
else:
  print("No, '" + y + "' is not what I expect.")

if y not in txt:
  print("The word '" + y + "' is not present in the ORIGN.")
