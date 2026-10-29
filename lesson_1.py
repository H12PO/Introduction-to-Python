"""
Code du premier cours d'Introduction au Python
"""
from math import pow

##Exercice 2
def interest_rate():
    # principal = float(input("Principal: "))
    # time = int(input("Time: "))
    # rate = float(input("Rate: "))
    principal = 100
    time = 10
    rate = 5
    for i in range(1,time+1):
        amount = principal *(1+i*rate/100)
        compound = principal *pow((1+rate/100),i)
        print(f'year : {i} \n amount : {amount:.2f} \n compound : {compound:.2f}')



#exercice 3
def total_amount (start_reward, reward_interval):
    total = 0
    total_blocks = 0
    current_reward = start_reward*10**8
    reward_interval = reward_interval
    while current_reward >= 1:
        total += reward_interval * current_reward
        total_blocks += 210000
        current_reward /= 2
    total = total/(10**8)
    res = [total, total_blocks]
    return res


def final_year (total_blocks):
    final_year = 2009 + (((((total_blocks)*10))/60)/24)/365
    return final_year


def monthly_rate(rt):
    mrt = pow(1+rt,1.0/12)-1
    return mrt


def monthly_payment():
    rate = monthly_rate(float(input('Annual interest rate (%) :')) / 100)
    amount = float(input('Amount:'))
    maturity = int(input('Maturity :'))
    i = int(input('Payment number :'))
    n = maturity*12
    monthlyPayment = (amount*((1+rate)**n)*rate)/((1+rate)**n-1)
    principal = monthlyPayment/((1+rate)**(n-i+1))
    interest = monthlyPayment - principal
    return monthlyPayment, principal, interest

