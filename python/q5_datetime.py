# Hint:  use Google to find python function

import pandas as pd

def print_days_delta(d0, d1, fmt=None):
    dst = pd.to_datetime(d0, format=fmt)
    dsp = pd.to_datetime(d1, format=fmt)

    delta = dsp - dst

    print '%d days' % delta.days

####a) 
date_start = '01-02-2013'
date_stop = '07-28-2015'

print_days_delta(date_start,date_stop)

####b)  
date_start = '12312013'  
date_stop = '05282015' 

print_days_delta(date_start,date_stop, '%m%d%Y') 

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

print_days_delta(date_start,date_stop)