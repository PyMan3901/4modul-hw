while True:
    palindrome = str(input('Введите палиндром: ').lower())

    check_palindrome = palindrome[::-1]


    if palindrome == check_palindrome:
        print(f'Это палиндром')
        print(f'true')
    else:
        print(f'{palindrome} не является палиндромом')
        print(f'false')


