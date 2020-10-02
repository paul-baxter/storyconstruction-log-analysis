#!/usr/bin/env python3
#
# viz-assoc.py
#
# need to use > python 3.5.3 (to use pandas)
#   assuming use of python3.8 in Ubuntu 20.04
#   sudo apt install python3-pip
#   sudo apt install python3-numpy python3-pandas python3-matplotlib python3-scipy
#   python3 -m pip install --upgrade bootstrapped
#
# "analysis of log files from story construction study, 2019"
# "University of Lincoln, U.K."
#
# run using (where data.dat is a log file):
#   python3 viz-assoc.py data.dat
#

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas.plotting as pandplot
import statsfunctions as sf
from dython.nominal import associations

data = pd.read_csv('data/raw-data-complete.csv')

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 16}
plt.rc('font', **font)

lines = {'linewidth' : '2',
         'color'     : 'black',
         'linestyle' : '-'}
plt.rc('lines', **lines)

box = {'boxprops.color'         : 'black',
       'boxprops.linewidth'     : '2',
       'boxprops.linestyle'     : '-',
       'whiskerprops.color'     : 'black',
       'whiskerprops.linewidth' : '2',
       'whiskerprops.linestyle' : '-',
       'capprops.color'         : 'black',
       'capprops.linewidth'     : '2',
       'capprops.linestyle'     : '-',
       'medianprops.color'      : 'C1',
       'medianprops.linewidth'  : '3',
       'medianprops.linestyle'  : '-',
       'meanprops.color'        : 'C2',
       'meanprops.marker'       : 'X',
       'meanprops.markerfacecolor' : 'C2',
       'meanprops.markeredgecolor' : 'C2',
       'meanprops.markersize'   : '14',
       'meanprops.linestyle'    : '--',
       'meanprops.linewidth'    : '2'}
plt.rc('boxplot', **box)

#prepare groups by age
groupby_agegroup1 = data[(data.age == 3)]
groupby_agegroup1.insert(1, "AgeGroup", "3", True)
groupby_agegroup2 = data[(data.age == 4)]
groupby_agegroup2.insert(1, "AgeGroup", "4", True)
groupby_agegroup3 = data[(data.age == 5)]
groupby_agegroup3.insert(1, "AgeGroup", "5", True)
groupby_agegroup4 = data[(data.age == 6)]
groupby_agegroup4.insert(1, "AgeGroup", "6", True)
groupby_agegroup5 = data[(data.age == 7)]
groupby_agegroup5.insert(1, "AgeGroup", "7", True)
#prepare full data set with added age group labels: group_labeled_data
#  then split up by age group for further analysis: age_grouped_summary
ageframes = [groupby_agegroup1, groupby_agegroup2, groupby_agegroup3, groupby_agegroup4, groupby_agegroup5]
group_labeled_data_age = pd.concat(ageframes)
age_grouped_summary = group_labeled_data_age.groupby('AgeGroup')

#prepare groups by gender
groupby_gender0 = data[(data.gender == 0)]
groupby_gender0.insert(1, "GenderGroup", "0", True)
groupby_gender1 = data[(data.gender == 1)]
groupby_gender1.insert(1, "GenderGroup", "1", True)
#full data by gender and with labels
genderframes = [groupby_gender0, groupby_gender1]
group_labeled_data_gender = pd.concat(genderframes)
gender_grouped_summary = group_labeled_data_gender.groupby('GenderGroup')

#overall data visualisation
plots, axes = plt.subplots(1,4)
data.boxplot(column=['IntLength'], showmeans=True, ax=axes[0])
data.boxplot(column=['PtimeMean'], showmeans=True, ax=axes[1])
data.boxplot(column=['PttsNmean'], showmeans=True, ax=axes[2])
data.boxplot(column=['PttsTimeMeanPooled'], showmeans=True, ax=axes[3])
axes[0].set_ylabel("Interaction length (s)")
axes[1].set_ylabel("Mean time per page (s)")
axes[2].set_ylabel("Mean number of robot TTS utterances per page")
axes[3].set_ylabel("Mean time between TTS utterances (s)")
plots, axes = plt.subplots(1,6,sharey=True)
data.boxplot(column=['SP'], showmeans=True, ax=axes[0])
data.boxplot(column=['SS'], showmeans=True, ax=axes[1])
data.boxplot(column=['IE'], showmeans=True, ax=axes[2])
data.boxplot(column=['B'], showmeans=True, ax=axes[3])
data.boxplot(column=['D'], showmeans=True, ax=axes[4])
data.boxplot(column=['F'], showmeans=True, ax=axes[5])
axes[0].set_ylabel("Response (in range [1,5])")
#data.boxplot(column=['SP','SS','IE','B','D','F'], showmeans=True, ax=None)

#data visualisations: by age
ageplots, axes = plt.subplots(1,4)
group_labeled_data_age.boxplot(column=['IntLength'], by='AgeGroup', showmeans=True, ax=axes[0])
group_labeled_data_age.boxplot(column=['PtimeMean'], by='AgeGroup', showmeans=True, ax=axes[1])
group_labeled_data_age.boxplot(column=['PttsNmean'], by='AgeGroup', showmeans=True, ax=axes[2])
group_labeled_data_age.boxplot(column=['PttsTimeMeanPooled'], by='AgeGroup', showmeans=True, ax=axes[3])
axes[0].set_ylabel("Interaction length (s)")
axes[1].set_ylabel("Mean time per page (s)")
axes[2].set_ylabel("Mean number of robot TTS utterances per page")
axes[3].set_ylabel("Mean time between TTS utterances (s)")
ageplots, axes = plt.subplots(1,6,sharey=True)
group_labeled_data_age.boxplot(column=['SP'], by='AgeGroup', showmeans=True, ax=axes[0])
group_labeled_data_age.boxplot(column=['SS'], by='AgeGroup', showmeans=True, ax=axes[1])
group_labeled_data_age.boxplot(column=['IE'], by='AgeGroup', showmeans=True, ax=axes[2])
group_labeled_data_age.boxplot(column=['B'], by='AgeGroup', showmeans=True, ax=axes[3])
group_labeled_data_age.boxplot(column=['D'], by='AgeGroup', showmeans=True, ax=axes[4])
group_labeled_data_age.boxplot(column=['F'], by='AgeGroup', showmeans=True, ax=axes[5])
axes[0].set_ylabel("Response (in range [1,5])")

#data visualisations: by gender
genderplots, axes = plt.subplots(1,4)
group_labeled_data_gender.boxplot(column=['IntLength'], by='GenderGroup', showmeans=True, ax=axes[0])
group_labeled_data_gender.boxplot(column=['PtimeMean'], by='GenderGroup', showmeans=True, ax=axes[1])
group_labeled_data_gender.boxplot(column=['PttsNmean'], by='GenderGroup', showmeans=True, ax=axes[2])
group_labeled_data_gender.boxplot(column=['PttsTimeMeanPooled'], by='GenderGroup', showmeans=True, ax=axes[3])
axes[0].set_ylabel("Interaction length (s)")
axes[1].set_ylabel("Mean time per page (s)")
axes[2].set_ylabel("Mean number of robot TTS utterances per page")
axes[3].set_ylabel("Mean time between TTS utterances (s)")
genderplots, axes = plt.subplots(1,6,sharey=True)
group_labeled_data_gender.boxplot(column=['SP'], by='GenderGroup', showmeans=True, ax=axes[0])
group_labeled_data_gender.boxplot(column=['SS'], by='GenderGroup', showmeans=True, ax=axes[1])
group_labeled_data_gender.boxplot(column=['IE'], by='GenderGroup', showmeans=True, ax=axes[2])
group_labeled_data_gender.boxplot(column=['B'], by='GenderGroup', showmeans=True, ax=axes[3])
group_labeled_data_gender.boxplot(column=['D'], by='GenderGroup', showmeans=True, ax=axes[4])
group_labeled_data_gender.boxplot(column=['F'], by='GenderGroup', showmeans=True, ax=axes[5])
axes[0].set_ylabel("Response (in range [1,5])")

#association analysis
subset_data = data[["age","IntLength","gender","PtimeMean","PttsNmean","PttsTimeMeanPooled","SP","SS","IE","robotIs","robotLike","B","D","F"]]
associations(subset_data, theil_u=True, nominal_columns=['age','gender','robotIs','robotLike','B','D','F'], mark_columns=True, cmap='vlag', fmt='.3f')

#display the plots
plt.show()
print()
