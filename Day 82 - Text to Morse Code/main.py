from morse import morse, alphabet

def encode(data):
    morse_text = ''
    for char in data:
        if char == " ":
            morse_text += "/"
        for index, letter in enumerate(alphabet):
            if char.upper() == letter:
                morse_text += morse[index]
                continue
        morse_text += " "
    return morse_text.strip()


def decode(data):
    result = ''
    letters = data.split(' ')
    for letter in letters:
        if letter == "/":
            result += " "
        for index, char in enumerate(morse):
            if letter == char:
                result += alphabet[index]
    return result

if __name__ == "__main__":
    text = input("Type sentence you want to convert to Morse Code > ")
    print(f"\nYour message in Morse Code:\n\n{encode(text)}")