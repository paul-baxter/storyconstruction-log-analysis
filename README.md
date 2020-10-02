# storyconstruction-log-analysis

Analysis of log files from 2019 Lincoln Summer Scientist study using a robot to mediate a story construction activity for children

Create directory 'tts' for extracted TTS strings

To run (assuming log files are in /data - remember to remove dummy.dat):

    ./analysis.sh

Results files produced:

- 'processedData.dat': stats from the robot log files (in /data)
- 'allTTS.dat': all the TTS strings uttered by the robot, from all robot log files
- Files in '/tts': individual files, one per robot log file, containing only robot TTS utterances

Second pass of analysis involves use of csv in which all data is collected (including both data from logfiles, and data from questionnaires), 'data/raw-data-complete.csv'. This analysis first starts with visualisation of data in boxplots (all data, then by age, then by gender), followed by an association analysis between variables of particular interest. To run this analysis, call:

    ./viz.sh

No results files produced, but seven plots using matplotlib. These are labelled.

Legend:
- IntLength: Interaction length in total (according to robot logs)
- PtimeMean: Mean time (s) spent on each page of the activity
- PttsNmean: Mean number of robot TTS utterances per page of the activity
- PttTimeMeanPooled: Mean amount of time between consecutive robot TTS events, per page
- SP: Social Presence metric, derived from 12 questionnaire questions
- SS: Social support metric, derived from 2 questionnaire questions, is only a subset of the original social support scale, so this is only an unvalidated indicator
- IE: Interest/Enjoyment metric, derived from 2 questionnaire questions, is only a subset of the original IMI Interest/Enjoyment scale, so this is only an unvalidated indicator
- B: Question B from the questionnaire ("")
- D: Question D from the questionnaire ("")
- F: Question F from the questionnaire ("")
- robotIs: Question from questionnaire (""), coded as {0: don't know, 1: younger than me, 2: same age as me, 3: older than me}
- robotLike: Question from questionnaire (""), coded as {1: computer, 2: toy, 3: pet, 4: friend, 5: teacher}
