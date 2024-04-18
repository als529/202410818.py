def read_single_digit(digit):
    if digit == '0':
        return '영'
    elif digit == '1':
        return '일'
    elif digit == '2':
        return '이'
    elif digit == '3':
        return '삼'
    elif digit == '4':
        return '사'
    elif digit == '5':
        return '오'
    elif digit == '6':
        return '육'
    elif digit == '7':
        return '칠'
    elif digit == '8':
        return '팔'
    elif digit == '9':
        return '구'

def read_number(number):
    result = ''
    result = result + read_single_digit(number[0]) + read_single_digit(number[1]) + read_single_digit(number[2])
    return result

number = input("세 자리수 이하의 10진 정수를 입력하세요: ")
korean_number = read_number(number)
print(korean_number)

