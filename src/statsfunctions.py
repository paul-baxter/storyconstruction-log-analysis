#!/usr/bin/env python3
#
# statsfunctions.py
#
# need to use > python 3.5.3 (to use pandas),
# some dependencies required,
# assuming use of python3.8 in Ubuntu 20.04:
#   sudo apt install python3-pip
#   sudo apt install python3-numpy python3-pandas python3-matplotlib python3-scipy
#   python3 -m pip install --upgrade bootstrapped
#
# "Useful stats functions"
#

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas.plotting as pandplot
import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats
import bootstrapped.compare_functions as bs_compare

def summary (in_data):
    mn = np.mean(in_data)
    print('\tMean:\t', mn[0])

def ci_bootstrap (label, in_data, n_samples=1000000):
    #assume that in_data is a pandas dataframe
    np_array = in_data.to_numpy()
    m = np.mean(np_array)
    n = len(np_array)
    #finds the empirical bootstrapped 95% confidence interval
    mean_result = bs.bootstrap(np_array, stat_func=bs_stats.mean)
    print(label,"\tn: ",n,"\tbootstrapped ci: ", mean_result)
    return mean_result

def ci_diff_bootstrap (label, data_test, data_control, n_smaples=1000000):
    #assume that input data is a pandas dataframe
    np_array_test = data_test.to_numpy()
    np_array_control = data_control.to_numpy()
    n_test = len(np_array_test)
    n_control = len(np_array_control)
    #a/b test comparison between the two input data sets
    result = bs.bootstrap_ab(np_array_test, np_array_control, stat_func=bs_stats.mean, compare_func=bs_compare.difference)
    print("CI difference: ", label, "\t\tn_0: ", n_test, "  n_1: ", n_control)
    print("\t\t", result)
    #print("\t\t", (np.mean(np_array_test) - np.mean(np_array_control)), " - actual difference")
    return result
