#!/bin/bash
for f in *.zip
do
	unzip -p "$f" curriculo.xml > "$f".xml
done
