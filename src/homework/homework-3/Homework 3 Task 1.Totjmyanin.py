user_function = None


def curry_explicit(function, arity):
    global user_function
    user_function = function

    def get_args(args):
        if len(args) == arity:
            return function(*args)

        def curry(x):
            return get_args([*args, x])

        return curry

    return get_args([])


def uncurry_explicit(function, arity):
    def get_args(args):
        if len(args) == arity:
            return user_function(*args)

        def uncurry(*x):
            arguments = []
            for i in range(len(x)):
                arguments.append(x[i])
            return get_args(arguments)

        return uncurry

    return get_args([])


input_user_function = eval(input("Enter your python function: "))
input_user_arity = int(input("Enter your arity: "))

f = curry_explicit(print, 10)


curried_function = curry_explicit(input_user_function, input_user_arity)
print("Successful!")
