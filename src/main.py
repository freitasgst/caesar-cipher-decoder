import sys
from mathlib import bin_to_dec


# TO __init__
def __init__():
    # TO read the cipher
    with open('./cipher.txt') as file:
        lines = [line.split()[0] for line in file]

    send_message(lines)


# TO send message in binary to be coverted in decimals
def send_message(message):
    decimals = [bin_to_dec(bin) for bin in message]
    ajust(decimals)


# TO decipher
def ajust(decimals):
    cipher = int(input('>> '))
    ajusted_decimals = [(number - cipher) for number in decimals]
    decipher(ajusted_decimals)


def decipher(ajusted_decimals):
    answer = "".join([chr(letter) for letter in ajusted_decimals])
    print(answer)


__init__()

sys.exit()
