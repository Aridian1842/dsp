[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34.27%

```python
from __future__ import print_function, division

import thinkstats2
import thinkplot

%matplotlib inline
```

##Exercise 5.1

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

<tt>scipy.stats</tt> contains objects that represent analytic distributions


```python
import scipy.stats
```

For example <tt>scipy.stats.norm</tt> represents a normal distribution.


```python
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)
```




    scipy.stats._distn_infrastructure.rv_frozen



A "frozen random variable" can compute its mean and standard deviation.


```python
dist.mean(), dist.std()
```




    (178.0, 7.7000000000000002)



It can also evaluate its CDF.  How many people are more than one standard deviation below the mean?  About 16%


```python
dist.cdf(mu-sigma)
```




    0.15865525393145741



How many people are between 5'10" and 6'1"?


```python
dist.cdf(170)
```




    0.14941142826225556




```python
# percentage of people less than 5'10"
lower_bound = dist.cdf(177.8)
lower_bound
```




    0.48963902786483265




```python
# percentage of people less than 6'1"
upper_bound = dist.cdf(185.42)
upper_bound
```




    0.83238586549630633




```python
# percentage of people between 5'10" and 6'1"
upper_bound - lower_bound
```




    0.34274683763147368