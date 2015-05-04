sed -i 's/[" "\t]/\n/g' text.txt
sed  -i '/^$/d' text.txt
tr "[A-Z]" [a-z] <text.txt|sort|uniq >text2.txt
mv text2.txt text.txt
comm -2 -3 text.txt dict.txt >dict_text.out.txt

