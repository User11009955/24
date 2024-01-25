first = float(input())
second = float(input())
mark = input()
match mark:
    case '-':
        print(first - second)
    case '+':
        print(first + second)
    case '*':
        print(first * second)
    case '/':
        if second != 0:
            print(first / second)
        else:
            print('888888')
    case default:
        print('888888')


