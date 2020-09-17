# storyconstruction-log-analysis

Analysis of log files from 2019 Lincoln Summer Scientist study using a robot to mediate a story construction activity for children

Create directory 'tts' for extracted TTS strings

To run (assuming log files are in /data - remember to remove dummy.dat):

    ./analysis.sh

Results files produced:

- 'processedData.dat': stats from the robot log files (in /data)
- 'allTTS.dat': all the TTS strings uttered by the robot, from all robot log files
- Files in '/tts': individual files, one per robot log file, containing only robot TTS utterances
