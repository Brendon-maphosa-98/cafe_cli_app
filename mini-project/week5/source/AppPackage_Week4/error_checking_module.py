# function to error check user input across the app


def user_int_check(input, minrng, maxrng):
    try:
        valid_num = int(input)
        validation = valid_num >= minrng and valid_num <= maxrng
        if validation:
            return True
        else:
            print("The option you selected is not available, please try again")
    except TypeError:
        print("\nYou must input a number, please try again")

    except ValueError:
        print("\nYou must input a number, please try again")

    except Exception:
        print("The option you selected is not available, please try again")

