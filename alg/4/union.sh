#!/bin/sh
echo -n 'Enter your File one: '
read f1
echo -n 'Enter your File two: '
read f2
cat $f1 $f2|sort|uniq >file.out.txt 
echo 'union of '$f1'and' $f2' have saved in union.out.txt'
