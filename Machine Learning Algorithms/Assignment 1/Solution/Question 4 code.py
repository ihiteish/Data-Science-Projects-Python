
# ML estimate.
def pois_ML(k, lambda_ml):
    e = 2.71
    return (((lambda_ml)**k) * e**(-lambda_ml))/fact(k)

# MAP estimate.
def pois_MAP(k, lambda_map, theta):
    e = 2.71
    prior = theta * e**(-lambda_map * theta)
    return ((((lambda_map)**k) * e**(-lambda_map))/fact(k)) * prior

# Calculate factorial.
def fact(k):
    if k==0 or k==1:
        return 1
    return k * fact(k-1)


import matplotlib.pyplot as plt

# Find distribution for ML estimate.
pois_dist_ML = []
for k in range(0,25):
    pois_dist_ML.append(pois_ML(k,8.778))

# Find distribution for MAP estimate.
pois_dist_MAP = []
for k in range(0,25):
    pois_dist_MAP.append(pois_MAP(k,8.316,theta = 1.5)) ## Change the theta here.
    
# Plot the probability distribution.
def plot_dist(values,s):
    plt.plot(values)
    plt.axvline(values.index(max(values)), c = 'red')
    plt.title("Poisson distribution for number of accidents using %s" %s)
    plt.xlabel("Number of accidents")
    plt.ylabel("Probability of accident")
    plt.xlim((0,25))
    plt.show()

plot_dist(pois_dist_ML, "MLE")
plot_dist(pois_dist_MAP,"MAP")
