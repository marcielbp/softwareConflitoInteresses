for f in *.zip
do
	unzip -p "$f" curriculo.xml > "$f".xml
done

#unzip -p "$f" curriculo.xml > "$f".xml
