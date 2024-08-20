from random import randint

BLOCK = " █"
SPACE = "  "


def create_list(size):
    if not (3 <= size <= 30):
        raise ValueError("Your size must be greater than 2 and less or equal than 30")
    list = []
    for i in range(size):
        new_list = [0] * size
        list.append(new_list)
    return list


def vertical_symmetry(sprite_list):
    size = len(sprite_list)
    for i in range(size):
        for j in range(size // 2, size):
            sprite_list[i][size - j - 1] = sprite_list[i][j]

    return sprite_list


def horizontal_symmetry(sprite_list):
    size = len(sprite_list)
    for i in range(size // 2):
        for j in range(size):
            sprite_list[size - i - 1][j] = sprite_list[i][j]

    return sprite_list


def paint_or_not(sprite, size, i, j):
    if (i + 1 < size and j + 1 < size) and (
        sprite[i][j + 1] == 1 or sprite[i + 1][j] == 1
    ):
        choice = randint(0, 100)
        if choice <= 80:
            sprite[i][j] = 1
    elif (i + 1 < size and j + 1 < size) and (
        sprite[i + 1][j + 1] == 1 or sprite[i + 1][j + 1] == 1
    ):
        choice = randint(0, 100)
        if choice <= 65:
            sprite[i][j] = 1
    else:
        choice = randint(0, 100)
        if choice <= 34:
            sprite[i][j] = 1


def generate_sprite(size: int):
    sprite = create_list(size)
    symmetry = randint(0, 1)

    if symmetry == 0:
        for i in range(size):
            for j in range(size // 2, size):
                paint_or_not(sprite, size, i, j)

        return vertical_symmetry(sprite)

    else:
        for i in range(size // 2):
            for j in range(size):
                paint_or_not(sprite, size, i, j)

        return horizontal_symmetry(sprite)


def print_sprite(sprite_list: list[list]):
    output = ""
    for i in range(len(sprite_list)):
        for j in range(len(sprite_list)):
            if sprite_list[i][j] == 0:
                output += SPACE
            elif sprite_list[i][j] == 1:
                output += BLOCK

            if j == len(sprite_list) - 1:
                output += "\n"

    print(output)


def main():
    try:
        input_user = int(input("Enter your size for sprites: "))
        while True:
            user_choice = input(
                "If you want next sprite press Enter, if you want exit enter Exit: "
            )
            if user_choice == "Exit":
                break
            try:
                sprite_list = generate_sprite(input_user)
                print_sprite(sprite_list)
            except ValueError as error:
                print(error)
                break
    except:
        print("You entered not integer")


if __name__ == "__main__":
    main()
