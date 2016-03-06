# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
"""
Answers to string function pre-work
"""

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    num = 'many'
    if (count < 10) and (count >= 0):
        num = str(count)
    return 'Number of dunuts: ' + num


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    ret_s = ''
    str_len = len(s)
    if str_len > 1:
        ret_s = s[:2] + s[str_len-2:str_len]
    return ret_s


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    first_chr = s[0]
    s = s.replace(first_chr, '*')
    s = first_chr + s[1:]
    return s


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a_first_chrs = a[0:2]
    b_first_chrs = b[0:2]
    a = b_first_chrs+a[2:len(a)]
    b = a_first_chrs+b[2:len(b)]
    return a + ' ' + b


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    length = len(s)
    if length >= 3:
        if s[length-3:length] == 'ing':
            s += 'ly'
        else:
            s += 'ing'
    return s


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    not_loc = s.find('not')
    bad_loc = s.find('bad')
    if not_loc > -1 and (bad_loc > not_loc):
        s = s[:not_loc] + 'good' + s[bad_loc+3:]
    return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    a_len = len(a)
    b_len = len(b)
    a_correction = 1
    b_correction = 1

    if a_len % 2 == 0:
        a_correction = 0

    if b_len % 2 == 0:
        b_correction = 0

    a_cut = a_len/2 + a_correction
    b_cut = b_len/2 + b_correction

    a_front = a[:a_cut]
    a_back = a[a_cut:]

    b_front = b[:b_cut]
    b_back = b[b_cut:]

    return a_front + b_front + a_back + b_back
