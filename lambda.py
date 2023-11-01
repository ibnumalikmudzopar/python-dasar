# lambda adalah fungsi yang pemakaiannya tidak harus didefinisakan
""""contoh lambda"""
def suqare_sum(x, y):
    return x ** 2 + y ** 2


lambda x, y: x ** 2 + y ** 2

# lambda args : expression


greeting = lambda name: print(f"Hello, {name}")

greeting("Ibnu Malik")
greeting("Ibn")

# lambda biasanya digunakan pada map filter dan reduce()

bilangan = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
filtered_result = map(lambda x: x * x, bilangan)
print(list(filtered_result))
