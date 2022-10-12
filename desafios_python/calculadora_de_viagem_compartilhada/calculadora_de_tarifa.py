ride_type = 'Black'
creditos = 4

ride_price = 0
final_price = 0

if ride_type == 'DooberX':
    ride_price = 20.5

elif ride_type == 'Black':
    ride_price = 37.9

else:
    ride_price = 18.7

print('Ride price:')
print(ride_price)

if creditos > 0:
    final_price = ride_price - creditos

print('Ride price:')
print(ride_price)



