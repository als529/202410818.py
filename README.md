def get_radius(prompt):
    r = float(input(prompt))
    return r

def get_circle_area(radius):
    area = radius * radius * 3.14
    return area

prompt = '넓이를 구하고자 하는 원의 반지름은? '
radius = get_radius(prompt);
print('반지름', radius, '인 원의 넓이 =', end=' ');
area = get_circle_area(radius);
print('3.14 x', radius, 'x', radius, '=', area);
