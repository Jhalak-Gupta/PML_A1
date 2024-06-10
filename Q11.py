n=int(input("Enter the number of terms:"))
fib_series=[0, 1]
for i in range(2, n):
    nt=fib_series[-1]+fib_series[-2]
    fib_series.append(nt)
print(fib_series)
