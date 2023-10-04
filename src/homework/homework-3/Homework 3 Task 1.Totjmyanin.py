user_function = None


def curry_explicit(function, arity):
    """
    Turning a function from several parameters into a function from one parameter that returns a function from the other parameters:
    function(a,b) --> function(a)(b)
    """
    if arity == 0:
        return function()
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
    """
    Performs the reverse actions of the curry_explicit function:
    function(a)(b) --> function(a,b)
    """

    def get_args(args):
        if len(args) == arity:
            return user_function(*args)

        def uncurry(*x):
            arguments = [item for item in x]
            return get_args(arguments)

        return uncurry

    return get_args([])


if __name__ == "__main__":
    input_user_function = eval(input("Enter your python function: "))
    input_user_arity = int(input("Enter your arity: "))

    curried_function = curry_explicit(input_user_function, input_user_arity)
    print("Successful!")
