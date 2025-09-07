# Function: user_int_check
# Purpose: Validate that a user’s input can be converted to an integer
#          and falls within a specified inclusive range.
#
# Arguments:
#   input   - the raw user input (string)
#   minrng  - minimum acceptable integer value
#   maxrng  - maximum acceptable integer value
#
# Returns:
#   True if conversion succeeds and value ∈ [minrng, maxrng]
#   Otherwise prints an error message and returns None

def user_int_check(input, minrng, maxrng):
    try:
        # Attempt to convert the input to an integer
        valid_num = int(input)
        # Check if the integer lies within the allowed range
        validation = (valid_num >= minrng) and (valid_num <= maxrng)
        if validation:
            return True
        else:
            # Out-of-range error feedback
            print("The option you selected is not available, please try again")
    except (TypeError, ValueError):
        # Handles non-integer inputs gracefully
        print("\nYou must input a number, please try again")
    except Exception:
        # Catches any other unexpected errors
        print("The option you selected is not available, please try again")


