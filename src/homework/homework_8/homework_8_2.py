import re
import string


def encode(dna):
    pattern = "^[A-Za-z]*$"
    if not bool(re.match(pattern, dna)):
        raise ValueError("Your dna string must be only letters")
    function_re = lambda m: f'{m[0][0]}{l if (l := len(m[0])) >= 1 else ""}'
    output = re.sub(r"(\w)\1*", function_re, dna)
    return output


def is_valid(dna):
    letters = string.ascii_letters
    output = True
    for i in range(len(dna) - 1):
        if dna[i] in letters and dna[i + 1] in letters:
            output = False
    if dna[-1] in letters:
        output = False
    if dna[0] in string.digits:
        output = False
    return output


def decode(dna):
    pattern = "^[A-Za-z0-9]*$"
    if not bool(re.match(pattern, dna)):
        raise ValueError("Your dna string must be only letters and digits")
    if not is_valid(dna):
        raise ValueError(
            "You entered invalid dna string. Your string should not contain two letters in a row, as well as the last character should be a digit"
        )

    chars = filter(lambda char: char in string.ascii_letters, dna)
    counts = filter(lambda digit: digit in string.digits, dna)

    output = list(map(lambda char, count: char * int(count), chars, counts))
    return "".join(output)


def main():
    dna = input("Enter your DNA: ").lower()
    choice = input("Enter your choice:\n 1) Encode\n 2) Decode\n")
    if choice == "1":
        try:
            print(encode(dna))
        except ValueError as error:
            print(error)
    elif choice == "2":
        try:
            print(decode(dna))
        except ValueError as error:
            print(error)
    else:
        print("You entered wrong choice")


if __name__ == "__main__":
    main()
