[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
import scipy.stats
lower = scipy.stats.norm.cdf(177.8, loc=178, scale=7.7)
upper = scipy.stats.norm.cdf(185.5, loc=178, scale=7.7)
upper - lower
```
