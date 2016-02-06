"""Hello my name is Marine,
This program is written in Python to calculate the cost of your meal with taxes and tips included. This program will prevent you the struggles and stress of haaving to calculate the right answer when you go out, so enjoy! :) """

print "Welcome to the taxes and tip calculator!"
meal=float(raw_input("What is the price before tax? "))
tax=float (raw_input ("What are the taxes? (in %) "))
tip=float (raw_input ("What do you want to tip? (in %) "))


meal= meal+ (tax/100)*meal
meal= meal+ ((tip/100)*meal)

print "The price you need to pay is: $%.6f." % meal
