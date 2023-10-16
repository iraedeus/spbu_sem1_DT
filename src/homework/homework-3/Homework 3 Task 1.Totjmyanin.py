def curry_explicit(function, arity):
    """
    Turning a function from several parameters into a function from one parameter that returns a function from the other parameters:
    function(a,b) --> function(a)(b)
    """
    if arity < 0:
        raise ValueError("Wrong arity. The arity must be greater than or equal to one")
    if arity == 0:
        return function

    def get_args(args):
        if len(args) == arity:
            return function(*args)

        def curry(x):
            return get_args([*args, x])

        curry.__name__ = function.__name__
        curry.__doc__ = function.__doc__
        return curry

    return get_args([])


def uncurry_explicit(function, arity):
    """
    Performs the reverse actions of the curry_explicit function:
    function(a)(b) --> function(a,b)
    """

    def get_args(*args):
        if arity != len(args):
            raise ValueError(
                "Wrong arity. The arity must be similar with count of arguments"
            )

        nonlocal function
        for arg in args:
            function = function(arg)
        return function

    get_args.__name__ = function.__name__
    get_args.__doc__ = function.__doc__
    return get_args


if __name__ == "__main__":
    input_user_function = eval(input("Enter your python function: "))
    input_user_arity = int(input("Enter your arity: "))

    curried_function = curry_explicit(input_user_function, input_user_arity)
    uncurried_function = uncurry_explicit(curried_function, input_user_arity)
    print("Successful!")
