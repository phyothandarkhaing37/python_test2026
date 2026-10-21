pizzas = ['margherita', 'pepperoni', 'hawaiian']
friend_pizzas = pizzas[:]

pizzas.append('bbq chicken')
friend_pizzas.append('veggie supreme')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")