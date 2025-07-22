def get_valid_input(prompt, expected_type, min_value=None, max_value=None, allow_empty=False):
    while True:
        user_input = input(prompt)
        if not allow_empty and user_input.strip() == "":
            print("Input cannot be empty. Please try again.")
            continue
        if allow_empty and user_input.strip() == "":
            return None
        try:
            if expected_type == int:
                value = int(user_input)
            elif expected_type == float:
                value = float(user_input)
            elif expected_type == str:
                value = user_input
            else:
                print("Unsupported type specified.")
                continue
        except ValueError:
            print(f"Input must be of type {expected_type.__name__}. Please try again.")
            continue

        if (min_value is not None) and (value < min_value):
            print(f"Input must be at least {min_value}. Please try again.")
            continue
        if (max_value is not None) and (value > max_value):
            print(f"Input must be at most {max_value}. Please try again.")
            continue

        return value

# Example usage:
if __name__ == "__main__":
    age = get_valid_input("Enter your age: ", int, min_value=0)
    print(f"Your age is: {age}")
    score = get_valid_input("Enter your score (0-100): ", float, min_value=0, max_value=100)
    print(f"Your score is: {score}")
    name = get_valid_input("Enter your name: ", str, allow_empty=False)
    print(f"Hello, {name}!")
