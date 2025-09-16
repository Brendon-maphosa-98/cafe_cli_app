# function to validate the users input when selecting menu options


def menu_choice_validator(
    user_input, options
):  # will intake the returned value from the function that takes the users choice.
    try:
        stringint = int(
            user_input
        )  # check that the user input can be turned into an int
        if (
            0 <= stringint <= len(options)
        ):  # check if the input the user gave can be turned into an integer and if that int is less than the length of the options available.
            return True
        return False
    except ValueError:
        return "NOT_A_NUMBER"
