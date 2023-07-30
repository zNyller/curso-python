shop_cart = []
cart_value = cheap = above_1000 = 0
most_cheap = ''

while True:
    product = input("Insira um produto: ")
    price = int(input("Valor: R$"))

    shop_cart.append(product)

    if price > 1000:
        above_1000 += 1

    if len(shop_cart) <= 1 or price < cheap:
        cheap = price
        most_cheap = product

    cart_value += price

    next = input("Deseja continuar? [s/n] ")

    if next == 'n':
        break

print(f"Carrinho: {shop_cart}")
print(f"Total dos produtos: R${cart_value}")
print(f"Temos {above_1000} produto(s) custando mais de R$1.000,00")
print(f"O produto mais barato foi {most_cheap}, custando R${cheap}")
