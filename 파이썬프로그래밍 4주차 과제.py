def get_discount_rate():
    dr = int(input('할인율은? '))
    return dr

def get_price(product):
    price = int(input(product + ' 상품의 할인된 가격은? '))
    return price

def get_fixed_price(product, dr, price):
    real_price = price / ((100 - dr) / 100)
    print(product, '상품의 정가는', real_price, '원')

discount_rate = get_discount_rate()

product_A_price = get_price('A')
get_fixed_price('A', discount_rate, product_A_price)

product_B_price = get_price('B')
get_fixed_price('B', discount_rate, product_B_price)
