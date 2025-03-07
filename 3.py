import scipy

samples = [0.47, 0.13, -0.98, 0.74, -2.11, -3.36, -0.35, -2.21, 1.14, -0.13, 1.12, 1.49, 0.77, 0.79, 1.13, -1.45, 0.92, -0.08, 0.62, -0.51]
n = len(samples)
alpha = 1 - 0.95

s2 = sum(x ** 2 for x in samples) / n

percentileL = scipy.stats.chi2(n).ppf(1 - alpha / 2)
percentileR = scipy.stats.chi2(n).ppf(alpha / 2)

l = n * s2 / percentileL
r = n * s2 / percentileR

print(f"({l}, {r})")