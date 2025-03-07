import scipy

n = 10000
alpha = 0.95
_p = 4000 / 10000

percentile = scipy.stats.norm.ppf(1 - alpha / 2)
deviation = percentile * (_p * (1 - _p) / n) ** .5

l = _p - deviation
r = _p + deviation

print(f"[{l}, {r}]")