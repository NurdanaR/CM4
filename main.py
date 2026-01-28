import numpy as np

x = list(map(float, input("Enter x values: ").split()))
fx = list(map(float, input("Enter f(x) values: ").split()))

n = len(x)
h = x[1] - x[0]

delta = np.zeros((n, n))
delta[:,0] = fx

for j in range(1, n):
    for i in range(n-j):
        delta[i][j] = delta[i+1][j-1] - delta[i][j-1]

print("\nForward Difference Table:")
header = ["x", "f(x)"] + [f"Δ^{i}f" for i in range(1, n)]
print("{:<6}".format(header[0]), end="")
for hname in header[1:]:
    print("{:<10}".format(hname), end="")
print()

for i in range(n):
    print("{:<6}".format(x[i]), end="")
    for j in range(n-i):
        print("{:<10}".format(delta[i][j]), end="")
    print()

f_prime = [(delta[i][1]/h) for i in range(n-1)]
print("\nApproximate first derivative f':")
for i in range(n-1):
    print(f"f'({x[i]}) ≈ {f_prime[i]}")

f_double_prime = [(delta[i][2]/h**2) for i in range(n-2)]
print("\nApproximate second derivative f'':")
for i in range(n-2):
    print(f"f''({x[i]}) ≈ {f_double_prime[i]}")
