sudo echo ""
clear
echo "Story Construction Log File Analysis"
echo ""

cp src/analysis.py analysis.py
cp src/statsfunctions.py statsfunctions.py

# look for contents of /data...
for entry in data/*.dat
do
    #echo "$entry"
    python3 analysis.py "$entry"
done

rm analysis.py

echo ""
echo "Robot TTS Word Frequency Analysis"
echo ""

cp src/text-analysis.py text-analysis.py
python2 text-analysis.py -i allTTS.dat -n 100
rm text-analysis.py
rm statsfunctions.py

echo ""
echo "All Done"
echo ""
