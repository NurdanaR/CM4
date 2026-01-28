def lagrange_interpolation(x, y, X):
    n = len(x)
    P = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (X - x[j]) / (x[i] - x[j])
        P += y[i] * Li
    return P

x = list(map(float, input("Enter x values separated by space: ").split()))
y = list(map(float, input("Enter f(x) values separated by space: ").split()))
X = float(input("Enter the point X to evaluate the interpolating polynomial: "))
exact = float(input("Enter the exact value f(X) for comparison: "))

Px = lagrange_interpolation(x, y, X)
error = abs(Px - exact)

print(f"\n P(x) at x = {X} , f({X}) = {exact}.")
print(f"P({X}) ≈ {Px:.4f}")
print(f" x = {X} -> |P({X}) - f({X})| ≈ |{Px:.4f} - {exact}| = {error:.4f}")
