shopping_bag = {}  # 장바구니

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    quantity = int(input('수량은? '))
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} {quantity}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')

# 검색 기능 추가
print('[검색]')
search_item = input('장바구니에서 확인하고자 하는 상품은? ')
if search_item in shopping_bag:
    print(f'{search_item}은(는) {shopping_bag[search_item]}개 담겨 있습니다.')
else:
    print(f'장바구니에 {search_item} 상품이 없습니다.')
