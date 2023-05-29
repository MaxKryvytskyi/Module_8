

n = 10

def series(n, s=4):
    result = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n >= 2:
        result += 1/s
        result += series(n-1, s+3)
    return result

def series_sum(n):
    text = series(n)
    return "{:.2f}".format(text)
print(series_sum(n))
