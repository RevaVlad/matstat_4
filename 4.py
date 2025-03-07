import scipy
sigma = 20
alpha = 0.1
qwant = scipy.stats.norm.ppf(1 - alpha / 2)
print((sigma * qwant / 15) ** 2)