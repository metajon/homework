mkdir converted/
for file in *.txt; do
    iconv -f utf-16le -t utf-8 "$file" > "converted/${file%.txt}.utf8.txt"
done
# grep '[ \t][0-9]\{9\}' <<filename>> | awk '{ print $3 }'

