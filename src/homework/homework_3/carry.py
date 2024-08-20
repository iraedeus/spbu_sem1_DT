import functools


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

        functools.update_wrapper(curry, function)
        return curry

    return get_args([])


def uncurry_explicit(function, arity):
    """
    Performs the reverse actions of the curry_explicit function:
    function(a)(b) --> function(a,b)
    """

    def get_args(*args, user_function=function):
        if arity != len(args):
            raise ValueError(
                "Wrong arity. The arity must be similar with count of arguments"
            )
        for arg in args:
            user_function = user_function(arg)
        return user_function

    functools.update_wrapper(get_args, function)
    return get_args


if __name__ == "__main__":
    input_user_function = eval(input("Enter your python function: "))
    input_user_arity = int(input("Enter your arity: "))

    curried_function = curry_explicit(input_user_function, input_user_arity)
    uncurried_function = uncurry_explicit(curried_function, input_user_arity)

    print("Successful!")
