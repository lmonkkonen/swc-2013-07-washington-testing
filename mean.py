#!/usr/bin/env python

def mean(numlist):
    """Calculate the mean of the values in numlist

    Input
    =====
    `numlist` (`list` or `tuple`) - List of values whose mean will be calculated

    Output
    ======
    (`float`) - Mean of the values in numlist
    
    """
    try: 
        for item in numlist:
            assert not isinstance(item, str)
    except: 
	print "List must contain numbers"
    try :
        total = sum(numlist)
        length = len(numlist)
    except TypeError :
        raise TypeError("The list was not numbers.")
    except :
        print "Something unknown happened with the list."
    return float(total)/length
def test_try():
    assert False
    assert_equal(1,2)
