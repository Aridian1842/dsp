[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)


The distribution of income is famously skewed to the right. In this exercise, we’ll measure how strong that skew is.

The Current Population Survey (CPS) is a joint effort of the Bureau of Labor Statistics and the Census Bureau to study income and related variables. Data collected in 2013 is available from http://www.census.gov/hhes/www/cpstables/032013/hhinc/toc.htm. I downloaded hinc06.xls, which is an Excel spreadsheet with information about household income, and converted it to hinc06.csv, a CSV file you will find in the repository for this book. You will also find hinc2.py, which reads this file and transforms the data.

The dataset is in the form of a series of income ranges and the number of respondents who fell in each range. The lowest range includes respondents who reported annual household income “Under $5000.” The highest range includes respondents who made “$250,000 or more.”

To estimate mean and other statistics from these data, we have to make some assumptions about the lower and upper bounds, and how the values are distributed in each range. hinc2.py provides InterpolateSample, which shows one way to model this data. It takes a DataFrame with a column, income, that contains the upper bound of each range, and freq, which contains the number of respondents in each frame.

It also takes log_upper, which is an assumed upper bound on the highest range, expressed in log10 dollars. The default value, log_upper=6.0 represents the assumption that the largest income among the respondents is 106, or one million dollars.

InterpolateSample generates a pseudo-sample; that is, a sample of household incomes that yields the same number of respondents in each range as the actual data. It assumes that incomes in each range are equally spaced on a log10 scale.

Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?


```python
import numpy as np

import pandas as pd

from pandas import Series, DataFrame

%matplotlib inline

import thinkstats2
import thinkplot
import hinc2
import hinc
import density
```


```python
df = hinc.ReadData()
```


```python
def SummarizeInterpolation(df, log_upper=6.0, print_plots=False):
    log_sample = hinc2.InterpolateSample(df, log_upper)
    log_cdf = thinkstats2.Cdf(log_sample)

    summary_stats = {}

    sample = np.power(10, log_sample)
    summary_stats['mean'] = sample.mean()
    summary_stats['median'] = thinkstats2.Median(sample)
    summary_stats['skewness'] = thinkstats2.Skewness(sample)
    summary_stats['pearson_skew'] = thinkstats2.PearsonMedianSkewness(sample)

    cdf = thinkstats2.Cdf(sample)
    summary_stats['cdf[mean]'] = cdf[summary_stats['mean']]

    if print_plots:
        thinkplot.Cdf(log_cdf)
        thinkplot.Show(xlabel='household income',
                   ylabel='CDF')
        pdf = thinkstats2.EstimatedPdf(sample)
        thinkplot.Pdf(pdf)
        thinkplot.Show(xlabel='household income',
                       ylabel='PDF')

    return summary_stats
```


```python
SummarizeInterpolation(df)
```




    {'cdf[mean]': 0.66000587956687196,
     'mean': 74278.707531187203,
     'median': 51226.454478940461,
     'pearson_skew': 0.73612580191417953,
     'skewness': 4.9499202444295793}




```python
SummarizeInterpolation(df, log_upper=6.5)
```




    {'cdf[mean]': 0.73544398895947993,
     'mean': 88703.396679146201,
     'median': 51226.454478940461,
     'pearson_skew': 0.52996542255731482,
     'skewness': 9.1085279548732814}




```python
SummarizeInterpolation(df, log_upper=7.0)
```




    {'cdf[mean]': 0.8565630665207663,
     'mean': 124267.39722164703,
     'median': 51226.454478940461,
     'pearson_skew': 0.39156450927742104,
     'skewness': 11.603690267537795}



As `log_upper` increases, `cdf[mean]`, `mean`, and `skewness` all increase, while the `median` stays constant, as expected. Surprisingly, `pearkson_skew` decreases as `log_upper` increases.

