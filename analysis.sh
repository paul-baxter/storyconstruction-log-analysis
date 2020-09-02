sudo echo ""
clear
echo "Story Construction Log File Analysis"
echo ""

# look for contents of /data...
for entry in data/*.dat
do
    #echo "$entry"
    python3 /src/analysis.py "$entry"
done
echo "All Done"
echo ""
