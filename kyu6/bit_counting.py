def count_bits(n):
    return sum(int(x) for x in bin(n) if x.isdigit())

print(count_bits(1234))

