def investment(initial_amount, month_amount, inv_percent, years):
    for i in range (years*12):
        if i == 0:
            initial_amount += initial_amount * (inv_percent/100/12)
        else:
            initial_amount += (initial_amount + month_amount) * (inv_percent/100/12)
    return initial_amount
print(investment(5000, 200, 15, 1))
