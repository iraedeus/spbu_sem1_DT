from math import *


def request_to_user_action(object):
    if object == "vector":
        input_action_vector = input(
            "1) Find scalar product of vectors \n"
            "2) Find length of vector \n"
            "3) Find angle between vectors: \n"
        )
        return input_action_vector
    elif object == "matrix":
        input_action_matrix = input(
            "1) Find sum of matrices \n"
            "2) Find product of matrices \n"
            "3) Transpose a matrix: \n"
        )
        return input_action_matrix
    elif object == "choice":
        print(
            paint_text(
                "Enter the number to perform the action: \n"
                "1) Perform actions on vectors\n"
                "2) Perform actions on matrices\n"
                "3) Exit the program",
                "white",
            )
        )
    return None


def request_to_user_vector(sequence):
    if sequence == "first":
        return format_vector(
            input(
                "Enter your first vector in format: (x1,x2,x3....xn), xn is a number\n"
            )
        )
    elif sequence == "second":
        return format_vector(
            input(
                paint_text(
                    "Enter your second vector in format: (y1,y2,y3....yn), yn is a number\n",
                    "white",
                )
            )
        )


def request_to_user_matrix(sequence):
    if sequence == "first":
        return format_matrix(
            input(
                "Enter you first matrix in format: "
                "(x11,x12...x1n)-(x21,x22...x2n)...(...) x1n,x2n are numbers\n"
            )
        )
    elif sequence == "second":
        return format_matrix(
            input(
                paint_text(
                    "Enter you second matrix in format: (x11,x12...x1n)-(x21,x22...x2n)...(...) "
                    "x1n,x2n are numbers\n",
                    "white",
                )
            )
        )


def format_vector(vector):
    answer = vector.replace("(", "").replace(")", "")
    try:
        [int(k) for k in answer.split(",")]
    except ValueError:
        print(paint_text("Incorrect format", "red"))
        return []
    return [int(j) for j in answer.split(",")]


def format_matrix(matrix):
    str_matrix = matrix.split(sep="-")
    return [format_vector(i) for i in str_matrix]


def correctness_of_matrix_check(matrix):
    first_line_len = len(matrix[0])
    for j in matrix:
        if len(j) != first_line_len:
            print(paint_text("You entered incorrect matrix", "red"))
            return False
    return True


def check_vectors_dimensions(vector_1, vector_2):
    if len(vector_2) != len(vector_1):
        print(paint_text("Dimensions of your vectors are not similar", "red"))
        return False
    return True


def find_scalar_product(vector_1, vector_2):
    if not check_vectors_dimensions(vector_1, vector_2):
        return []
    return sum(vector_1[j] * vector_2[j] for j in range(len(vector_1)))


def find_length_of_vector(vector):
    return sum(coordinates_of_vector**2 for coordinates_of_vector in vector) ** 0.5


def find_angle_between_vectors(vector_1, vector_2):
    if not check_vectors_dimensions(vector_1, vector_2):
        return []
    return (
        acos(
            find_scalar_product(vector_1, vector_2)
            / (find_length_of_vector(vector_1) * find_length_of_vector(vector_2))
        )
        * 180
        / pi
    )


def find_sum_of_matrices(matrix_1, matrix_2):
    if not correctness_of_matrix_check(matrix_1) or not correctness_of_matrix_check(
        matrix_2
    ):
        return []
    if (len(matrix_1[0]) != len(matrix_2[0])) or (len(matrix_1) != len(matrix_2)):
        print(paint_text("You cannot sum these matrices", "red"))
        return []
    return [
        [matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_2[0]))]
        for i in range(len(matrix_1))
    ]


def transpose_the_matrix(matrix):
    if not correctness_of_matrix_check(matrix):
        return []
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def find_product_of_matrices(matrix_1, matrix_2):
    if not correctness_of_matrix_check(matrix_1) or not correctness_of_matrix_check(
        matrix_2
    ):
        return []
    if len(matrix_1[0]) != len(matrix_2):
        print(paint_text("You cannot multiply this matrices", "red"))
        return []
    matrix_2 = transpose_the_matrix(matrix_2)
    return [[find_scalar_product(i, j) for j in matrix_2] for i in matrix_1]


def paint_text(text, color):
    if color == "red":
        return "\033[31m{}".format(text)
    elif color == "yellow":
        return "\033[33m{}".format(text)
    elif color == "white":
        return "\033[0m{}".format(text)
    return text


def paint_matrix(matrix):
    for i in matrix:
        print(i)


def action_with_vector():
    if action_from_user == "1":
        vector_1_input = request_to_user_vector("first")
        vector_2_input = request_to_user_vector("second")
        print(
            paint_text(
                "Scalar product of your vectors is: "
                + str(find_scalar_product(vector_1_input, vector_2_input)),
                "yellow",
            )
        )
    elif action_from_user == "2":
        vector_input = format_vector(
            input("Enter your vector in format: (x1,x2, 3....xn), xn is a number\n")
        )
        print(
            paint_text(
                "Length of your vector is: " + str(find_length_of_vector(vector_input)),
                "yellow",
            )
        )
    elif action_from_user == "3":
        vector_1_input = request_to_user_vector("first")
        vector_2_input = request_to_user_vector("second")
        print(
            paint_text(
                "Angle between your vectors is: "
                + str(find_angle_between_vectors(vector_1_input, vector_2_input)),
                "yellow",
            )
        )
    else:
        print(
            paint_text("You have chosen an incorrect action, please try again", "red")
        )


def action_with_matrices():
    if action_from_user == "1":
        matrix_1_input = request_to_user_matrix("first")
        matrix_2_input = request_to_user_matrix("second")

        print(paint_text("Sum of your matrices is: ", "yellow"))
        paint_matrix(find_sum_of_matrices(matrix_1_input, matrix_2_input))
    elif action_from_user == "2":
        matrix_1_input = request_to_user_matrix("first")
        matrix_2_input = request_to_user_matrix("second")

        print(paint_text("Product of your matrices is: ", "yellow"))
        paint_matrix(find_product_of_matrices(matrix_1_input, matrix_2_input))
    elif action_from_user == "3":
        matrix_input = format_matrix(
            input(
                "Enter you matrix in format:"
                "(x11,x12...x1n)-(x21,x22...x2n)...(...) x1n,x2n are numbers\n"
            )
        )
        print(paint_text("The transposed matrix: \n", "yellow"))
        paint_matrix(transpose_the_matrix(matrix_input))
    else:
        print(
            paint_text("You have chosen an incorrect action, please try again", "red")
        )


if __name__ == "__main__":
    print("MathHelper v1.1")
    while True:
        request_to_user_action("choice")
        action_from_user = input()

        if action_from_user == "1":
            action_from_user = request_to_user_action("vector")
            action_with_vector()

        elif action_from_user == "2":
            action_from_user = request_to_user_action("matrix")
            action_with_matrices()

        elif action_from_user == "3":
            break

        else:
            print(
                paint_text(
                    "You have chosen an incorrect action, please try again", "red"
                )
            )
