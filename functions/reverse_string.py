def reverse_string(txt):
    if len(txt) == 0:
        return txt
        # base case
    else:
        return reverse_string(txt[1:]) + txt[0]
        # recursive case

print(reverse_string("four"))  # Output: "olleh"


