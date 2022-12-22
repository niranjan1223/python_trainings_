def mutate_string(string, pos, character):
    string_output = [i for i in string]
    string_output[pos] = character
    return "".join(i for i in string_output)


