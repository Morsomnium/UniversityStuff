def profit(amount, days):
    a = amount
    for i in range (days):
        amount += amount / 100
    amount -= a
    return amount
