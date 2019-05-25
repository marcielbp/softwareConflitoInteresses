#!/bin/sh
for d in */; do
	#echo $d
	cd "$d"
	for f in *.xml
	do
		cd ..
		python -W ignore app.py "$d/$f" candidatos.txt
	done
	
done
