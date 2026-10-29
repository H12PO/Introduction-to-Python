from lesson_1 import *



if __name__ == "__main__":
    interest_rate()
    res = total_amount(50 , 210000)
    print (f'Total amount = {res[0]}, Total blocks = {res[1]} ')

    print(f"Final year = {final_year(res[1])}" )
    res = monthly_payment()
    print(f'Monthly payment = {res[0]:.2f}, Principal = {res[1]:.2f}, Interest = {res[2]:.2f}')