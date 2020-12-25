def find_p(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return find_p(n - 1) + find_p(n - 2) + find_p(n - 3)

print(find_p(4))
print(find_p(5))
print(find_p(35))
