#  to find tax 

grossincome = int(input('enter total income'))
standarddeduction = 10000 #this is the direct deduction
dependentdeduction = 3000
int(input('enter no.of dependent')) #standard deduction

taxableincome = grossincome-standarddeduction-dependentdeduction

print(taxableincome*0.2)