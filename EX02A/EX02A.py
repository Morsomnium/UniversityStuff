def profit(amount, days):
    a = amount
    for i in range (1, days):
        amount += amount / 100
    amount -= a
    return amount
