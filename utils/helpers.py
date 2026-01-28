from scipy.stats import shapiro

def test_difference_wilcoxon(x, y):
    pass


def test_normality_shapirowilk(data, verbose=False):
    """
    Test for normality of `data` using Shapiro-Wilk Test.
    """
    _, pval = shapiro(data)
    if pval > 0.05:
        if verbose: print("Shapiro-Wilk: Data NORMALLY distributed")
        normality = True
    else:
        if verbose: print("Shapiro-Wilk: Data NOT NORMALLY distributed")
        normality = False
    return normality, pval
