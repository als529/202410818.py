def get_integer(prompt) :
    return int(input(prompt));
    
def exchange(prompt) :
    amount = get_integer(prompt);
    n500 = amount // 500
    amount %= 500

    n100 = amount // 100
    amount %= 100

    n50 = amount // 50
    amount %= 50

    n10 = amount // 10
    amount %= 10

    print('> 받을 500원 동전의 개수: ',n500)
    print('> 받을 100원 동전의 개수: ',n100)
    print('> 받을 50원 동전의 개수: ',n50)
    print('> 받을 10원 동전의 개수: ',n10)

exchange('동전으로 교환하고자 하는 금액은? :');
