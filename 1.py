import scipy

mean = 249
sigma = 10
n = 100
alpha = 0.1

percentile = scipy.stats.norm.ppf(alpha / 2)

l = mean + percentile * sigma / (n ** .5)
r = mean - percentile * sigma / (n ** .5)

print(f"[{l}, {r}]")