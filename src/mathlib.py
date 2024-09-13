# TO convert decimal to binary
def dec_to_bin(number):
    result = ""
    q = int(number)

    # Convert base 10 to base 2 by division-remainder
    while q != 0 and q != 1:
        # get the remainder
        r = q % 2
        # include the remainder on the result
        result = result + str(r)
        # get the next number to be divided
        q = int(q / 2)

    # include the quotient on the result
    result = result + str(q)
    # reverse the result to get the converted number
    result_in_binary = result[::-1]

    return int(result_in_binary)


# TO convert decimal to hexadecimal
def dec_to_hex(number):
    # Creating dictionary
    switch = {
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
    }

    result = ""
    q = int(number)

    # Convert base 10 to base 16 by division-remainder
    while q >= 16:
        # get the remainder
        r = q % 16
        # convert if it's bigger than 10
        r = switch.get(r, r)
        # include the remainder on the result
        result = result + str(r)
        # get the next number to be divided
        q = int(q / 16)

    # convert the last quotient
    q = switch.get(q, q)
    # include the quotient on the result
    result = result + str(q)
    # reverse the result to get the converted number
    result_in_hex = result[::-1]

    return result_in_hex


# TO convert binary to decimal
def bin_to_dec(number):
    inverted = str(number)[::-1]
    count = result_in_dec = 0

    # Formula
    for i in inverted:
        result_in_dec += int(i) * 2 ** count
        count += 1

    return result_in_dec
