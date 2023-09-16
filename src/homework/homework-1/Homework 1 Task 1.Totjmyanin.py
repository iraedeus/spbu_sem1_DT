def find_answer(x):
    square_of_x = x*x
    return (square_of_x + x)*(square_of_x + 1) + 1


if __name__ == '__main__':
    print('If you want exit, please press Enter')
    while True:
        try:
            input_from_user = float(input('Calculating x^4+x^3+x^2+x+1, enter x: ').replace(',', '.'))
            if input_from_user == '':
                break
        except ValueError:
            print('This is not a number, please try again')
            continue
        print(f'{input_from_user}^4+{input_from_user}^3+{input_from_user}^2+{input_from_user}+1 = {find_answer(input_from_user)}')