# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
curr_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    curr_month = curr_month + 1
    # if curr_month == 1:  # addition for the start month
    #     payment_temp = payment + extra_payment_start_month
    if (curr_month < (9*12+1)) & (curr_month > (5*12)):  # addition for the 5th to 9th year
        payment_temp = payment + extra_payment
        # print(curr_month/12)
    else:
        payment_temp = payment

    principal = principal * (1+rate/12) - payment_temp
    total_paid = total_paid + payment_temp
    print(curr_month, total_paid, principal)

total_paid = total_paid + extra_payment_end_month  # addition for the end month
print('Total paid', total_paid)
print('Months', curr_month)

