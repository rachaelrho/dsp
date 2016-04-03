[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```
%matplotlib inline
import chap01soln

resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh)

import thinkplot
thinkplot.PrePlot
thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.show()

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

bias = BiasPmf(pmf, label = 'bias')
thinkplot.Pmfs([pmf, bias])
thinkplot.show()
