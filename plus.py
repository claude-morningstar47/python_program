def to_hex(num):
    if num == 0:
        return '0'

    hex_digits = '0123456789abcdef'

    if num < 0:
        num = (1 << 32) + num

    hex_str = ''
    while num > 0:
        hex_str = hex_digits[num & 15] + hex_str
        num >>= 4
    return hex_str


to_hex(77)
assert to_hex(26) == '1a'
assert to_hex(-1) == 'ffffffff'
assert to_hex(0) == '0'

# je n'arrive pas a utiliser GPT
