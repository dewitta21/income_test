#2) The original U.S. income tax of 1913 was quite simple. The schedule for this calculation is provided below. 
# Write a program that computes the income tax according to this schedule.

# 1 percent on the first $50,000.
# 2 percent on the amount over $50,000 up to $75,000.
# 3 percent on the amount over $75,000 up to $100,000.
# 4 percent on the amount over $100,000 up to $250,000.
# 5 percent on the amount over $250,000 up to $500,000.
# 6 percent on the amount over $500,000.


#define tax rates
RATE1 = 0.01
RATE2 = 0.02
RATE3 = 0.03
RATE4 = 0.04
RATE5 = 0.05
RATE6 = 0.06
tax = 0
income = float(input("Enter income: "))

#calculate tax rates with income
if income <= 50000:
   tax = RATE1 * income
elif income > 50000 and income <= 75000:
     tax = RATE2 * income
elif income > 75000 and income <= 100000:
     tax = RATE3 * income
elif income > 100000 and income <= 250000:
     tax = RATE4 * income
elif income > 250000 and income <= 500000:
     tax = RATE5 * income
elif income >= 500000:
     tax = RATE6 * income
else:
     print("Error")

print("The tax is $%.2f" % tax)

    
    
    
    
    
