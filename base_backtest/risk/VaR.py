import datetime
import numpy as np
import pandas as pd
from scipy.stats import norm

def var_cov_var(P, c, mu, sigma):
    """
    Variance-Covariance calculation of daily Value-at-Risk
    using confidence level c, with mean of returns mu
    and standard deviation of returns sigma, on a portfolio
    of value P.
    """
    # Percent point function (inverse of cdf) at q of the given RV.累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
    alpha = norm.ppf(1-c, mu, sigma)
    return P - P*(alpha + 1)

if __name__ == "__main__":

    citi = pd.read_csv("../input/SPY.csv")

    citi["rets"] = citi["Close"].pct_change()


    P = 1e6   # 1,000,000 USD
    c = 0.99  # 99% confidence interval
    mu = np.mean(citi["rets"])
    sigma = np.std(citi["rets"])

    var = var_cov_var(P, c, mu, sigma)
    print("Value-at-Risk: $%0.2f" % var)