key = "key"

message = "Hello World"

letter_to_number_dictionary = {"a": 0,
                               "b": 1,
                               "c": 2,
                               "d": 3,
                               "e": 4,
                               "f": 5,
                               "g": 6,
                               "h": 7,
                               "i": 8,
                               "j": 9,
                               "k": 10,
                               "l": 11,
                               "m": 12,
                               "n": 13,
                               "o": 14,
                               "p": 15,
                               "q": 16,
                               "r": 17,
                               "s": 18,
                               "t": 19,
                               "u": 20,
                               "v": 21,
                               "w": 22,
                               "x": 23,
                               "y": 24,
                               "z": 25,
                               " ": 26} # Could use ord()


def get_key(val):
    for key, value in letter_to_number_dictionary.items():
        if val == value:
            return key

    return "key doesn't exist"

def l_to_num(letter):
    return ord(letter.lower()) - 97

output = ""
i = 0

for letter in message:
    output += get_key((l_to_num(letter) + l_to_num(key[i])) % 27)
    i += 1
    try:
        a = key[i]
    except:
        i = 0

print(output)



# for letter in key:
#     print(letter)