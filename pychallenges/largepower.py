def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False