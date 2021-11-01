"""Write a program to perform linear encoding.
"""


def encode(string_input):

    # empty input string => empty encoding
    if len(string_input) == 0:
        return ""

    # build a list of encodings for each run
    encoded_runs = []
    run_ch = None
    for ch in string_input:

        # if new run => create a new counter + update run character
        if run_ch != ch:

            # if we were previously building a run, update the list of encoded runs
            if run_ch is not None:
                encoded_runs.append(f"{counter}{run_ch}")

            # initialize counter and run character for new run
            counter = 1
            run_ch = ch

        # otherwise same run => update counter
        else:
            counter += 1

    # update the latest run
    encoded_runs.append(f"{counter}{run_ch}")

    # return a joined string of encoded runs
    return "".join(encoded_runs)


if __name__ == "__main__":
    test_cases = [
        ("", ""),
        ("a", "1a"),
        ("aaaa", "4a"),
        ("abab", "1a1b1a1b"),
        ("aaabbb", "3a3b"),
        ("aabbbbbaaacccc", "2a5b3a4c"),
    ]
    for (input_string, encoded_string) in test_cases:
        found_string = encode(input_string)
        assert encoded_string == found_string,\
            f"input_string={input_string}, desired={encoded_string}, found={found_string}"

