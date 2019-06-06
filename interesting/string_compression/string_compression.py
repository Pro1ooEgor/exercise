def str_compression(string):
    char_repetition = 0
    current_char = ""
    result_string = ""
    for char in string:
        char_repetition = char_repetition + 1 if char == current_char else 1
        current_char = char
        result_string += f"" \
            f"{current_char if current_char not in result_string else ''}"
        if result_string[-1].isdigit():
            result_string = result_string.replace(
                result_string[-1], str(char_repetition))
        else:
            result_string += str(char_repetition) if char_repetition > 1 else ''

    return result_string


print(str_compression('adddbbbgg'))
