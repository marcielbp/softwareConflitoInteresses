for d in */; do
	#echo $d
	cd "$d"
	for f in *.xml
	do
		cd ..
		python -W ignore app.py "$d/$f" candidatos.txt
		#unzip -p "$f" curriculo.xml > "$f".xml
	done
	
done



