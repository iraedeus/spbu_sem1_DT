def to_unicode_char(char):
    hex_unicode = hex(ord(char)).lstrip("0x").upper()
    return "U+" + hex_unicode.rjust(4, "0")


def to_utf16(char):
    decimal_char = ord(char)

    if decimal_char < 65535:
        binary_char = bin(decimal_char).lstrip("0b").rjust(16, "0")
        output = " ".join([binary_char[:8], binary_char[8:]])
    else:
        decimal_char -= 65536
        binary_char = bin(decimal_char).lstrip("0b").rjust(20, "0")

        higher_num = int(binary_char[:10], 2) + 55296
        lower_num = int(binary_char[10:], 2) + 56320

        higher_bits = bin(higher_num).lstrip("0b")
        lower_bits = bin(lower_num).lstrip("0b")

        output = " ".join(
            [higher_bits[:8], higher_bits[8:], lower_bits[:8], lower_bits[8:]]
        )

    return output


def main():
    chars = list(input("Enter your string: "))
    output = ""
    for char in chars:
        unicode_char = to_unicode_char(char)
        utf16 = to_utf16(char)

        output += f"{char}    {unicode_char}    {utf16}\n"

    print(output)


if __name__ == "__main__":
    main()
