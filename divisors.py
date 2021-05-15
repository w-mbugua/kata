def divisors(integer):
    arr = []
    for n in range(2, integer):
        if integer % n == 0:
            print(n)
            arr.append(n)
    if len(arr) == 0:
        return f'{integer} is prime'
    return arr

print(divisors(13))