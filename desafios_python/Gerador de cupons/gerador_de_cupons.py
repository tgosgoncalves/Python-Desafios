base = 'www.homeflix.com'
cupon = 'signup/cupon'
discount = 50
amount = 4

for num in range(amount):
    print(f'{base}/{cupon}/{discount}/{num}')

print(f'{amount} coupons created')