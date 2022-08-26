import sys

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Error: Wrong arguments")
    print("Format: python cipher-key-detecter.py {original_text} {encrypted_text}")
elif len(sys.argv[1]) != len(sys.argv[2]):
    print("Error: Input strings should be the same length.")
else:
    print("=== Cipher Key Detecter ===")
    print()
    print("Make sure to reorganize the the key you get.")
    print("Ex. brainfuckmy => fuckmybrain")
    print()
    first_letter = ord("a")
    last_letter = ord("z")
    number_of_letters = 26

    original_list = list(sys.argv[1])
    encrypted_list = list(sys.argv[2])
    output = ""

    for (original, encrypted) in zip(original_list, encrypted_list):
        original_unicode = ord(original.lower())

        if first_letter <= original_unicode or original_unicode >= last_letter:
            original_code = ord(original.lower()) - first_letter
            encrypted_code = ord(encrypted.lower()) - first_letter

            value = encrypted_code - original_code
            if value < 0:
                value += number_of_letters

            output += chr(value + first_letter)

        else:
            continue

    key_length = len(output)
    key = ""

    for letter in list(output):
        count = output.count(key)
        if count == 1:
            break
        else:
            key += letter

    print("Key:", key[:-1])
