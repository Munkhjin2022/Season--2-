#comment input
p = float(input("How much is the item? "))
d = float(input("Please enter the discount precintage "))

#process phase 
da = (p/100) * d
A = p - da

#output
print("The discount amount is ", da)
print ("The discounted price is ", A)