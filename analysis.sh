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
rm statsfunctions.py

echo "All Done"
echo ""
