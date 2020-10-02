sudo echo ""
clear
echo "Story Construction Visualisation and Analysis"
echo ""

cp src/statsfunctions.py statsfunctions.py
cp src/viz-assoc.py viz-assoc.py

python3 viz-assoc.py data/raw-data-complete.csv

rm viz-assoc.py
rm statsfunctions.py

echo ""
echo "All Done"
echo ""
