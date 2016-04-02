[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

firstWgt = df.totalwgt_lb.loc[df.pregordr == 1]
otherWgt = df.totalwgt_lb.loc[df.pregordr != 1]
firstGest = df.wksgest.loc[df.pregordr == 1]
otherGest = df.wksgest.loc[df.pregordr != 1]

np.mean(firstGest)
np.mean(otherGest)
CohenEffectSize(firstWgt, otherWgt)
CohenEffectSize(firstGest, otherGest)
```
####Cohen's d for first vs. other babies is -0.07. First babies also show a ~1 week less gestation period (29.6 weeks) than second babies (30.3 weeks)
