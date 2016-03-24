[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>
Exercise from Think Stats, 2nd Edition (thinkstats2.com)<br>
Allen Downey


```python
from __future__ import print_function, division

import thinkstats2
import thinkplot

import numpy as np

import first
import hypothesis

%matplotlib inline
```

Read the data:


```python
live, firsts, others = first.MakeFrames()
```

This is a copy of the class defined in `hypothesis.py`:


```python
class DiffMeansPermute(thinkstats2.HypothesisTest):
    """Tests a difference in means by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant
        """
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat

    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data
```

Compute the p-value of the difference in weights between first babies and others:


```python
data = (firsts.prglngth.dropna().values,
        others.prglngth.dropna().values)
ht = hypothesis.DiffMeansPermute(data)
p_value = ht.PValue(iters=10000)
print('\nmeans permute prglngth')
print('p-value =', p_value)
print('actual =', ht.actual)
print('ts max =', ht.MaxTestStat())
```


    means permute prglngth
    p-value = 0.1666
    actual = 0.0780372667775
    ts max = 0.227544662011



```python
data = (firsts.totalwgt_lb.dropna().values,
        others.totalwgt_lb.dropna().values)
ht = hypothesis.DiffMeansPermute(data)
p_value = ht.PValue(iters=10000)
print('\nmeans permute birthweight')
print('p-value =', p_value)
print('actual =', ht.actual)
print('ts max =', ht.MaxTestStat())
```


    means permute birthweight
    p-value = 0.0
    actual = 0.124761184535
    ts max = 0.120385534165


Exercise 9.2: In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.

An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.

Write a class named `DiffMeansResample` that inherits from `DiffMeansPermute` and overrides `RunModel` to implement resampling, rather than permutation.

Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?


```python
class DiffMeansResample(DiffMeansPermute):

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        group1, group2 = self.data
        count = 0

        sample1 = np.random.choice(self.pool, self.n, replace=True)
        sample2 = np.random.choice(self.pool, self.m, replace=True)

        return sample1, sample2
```

Here's some code to test your implementation of `DiffMeansResample`.


```python
def GetMeansPermute(attribute):
    thinkstats2.RandomSeed(18)
    data = firsts[attribute].dropna().values, others[attribute].dropna().values
    ht = DiffMeansResample(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute',attribute)
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())
```


```python
GetMeansPermute('prglngth')
```


    means permute prglngth
    p-value = 0.1674
    actual = 0.0780372667775
    ts max = 0.226752436104



```python
GetMeansPermute('totalwgt_lb')
```


    means permute totalwgt_lb
    p-value = 0.0
    actual = 0.124761184535
    ts max = 0.115015425044


The results are very similar in both models. Therefore, the model does not appear to affect the results much in this case.

