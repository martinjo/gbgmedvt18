INPUT=$1
OUTPUT=$2
convert -density 300 -set colorspace RBG -contrast-stretch 3x10% $INPUT intermediate.png
noteshrink -n 15 -S intermediate*.png -o $OUTPUT
rm intermediate*
rm page0*


