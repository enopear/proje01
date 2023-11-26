def fibonaccibasla(n):
    fib_serisi = [0, 1]

    while len(fib_serisi) < n:
        son_eleman = fib_serisi[-1] + fib_serisi[-2]
        fib_serisi.append(son_eleman)

    return fib_serisi[:n]


