def simulate_multiline(string):
    """Return simulated multiline input for given string."""
    counter = 0
    strings = string.split("\n")

    def simulated_input(*args):
        nonlocal counter
        if counter == len(strings):
            return ""
        value = strings[counter]
        counter += 1
        return value
    return simulated_input