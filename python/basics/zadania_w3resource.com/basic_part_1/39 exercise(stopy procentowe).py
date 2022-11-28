# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
# Napisz program w języku Python, aby obliczyć przyszłą wartość określonej kwoty głównej, stopy procentowej i liczby lat

# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def futureValue(amt, int, years):
    totalAmt = amt
    a = 1
    while a <= years: 
        totalAmt =totalAmt + (totalAmt * (int  / 100))
        a += 1
    
    print(round(totalAmt, 2))

futureValue(10000, 3.5, 7)

# w3resource

amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))