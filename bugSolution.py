def function_with_error_handling(x):
    try:
        return x * (1 / x)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "Error: Input must be a number."