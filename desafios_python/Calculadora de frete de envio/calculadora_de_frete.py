internacional_shipping = True

total = 150
shipping_coast = 0

if internacional_shipping:
    shipping_coast += 15
    print('Internacional base cost applied')

if total <= 50:
    shipping_coast += 20

elif total <= 100:
    shipping_coast += 15

else:
    shipping_coast += 5

print(f"Shipping cost: {shipping_coast}")
