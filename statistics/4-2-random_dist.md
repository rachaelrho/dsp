[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

####The distribution is indeed uniform.

```
rand = np.random.uniform(0,1,1000)
cdf = thinkstats2.Cdf(rand)
ranks = [cdf.PercentileRank(x) for x in rand]

rank_cdf = thinkstats2.Cdf(ranks)
thinkplot.Cdf(rank_cdf)
thinkplot.Show()

pmf = thinkstats2.Pmf(rand)
thinkplot.Pmf(pmf, linewidth = .01)
thinkplot.Show()
```
