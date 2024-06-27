def get_password(n):
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                pairs.append(f"{i} {j}")
    result = ''.join(pairs)
    return result

n1 = 9
n2 = 11

result1 = get_password(n1)
result2 = get_password(n2)

print(f"{n1} - {result1}")
print(f"{n2} - {result2}")

for n in range(3, 21):
    print(f"{n} - {get_password(n)}")


