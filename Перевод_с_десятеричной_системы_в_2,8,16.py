num = int(input())

bin_num = bin(num)
oct_num = oct(num)
hex_num = hex(num)

print(bin_num[2:])
print(oct_num[2:])
print(hex_num[2:].upper())
