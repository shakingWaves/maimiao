#!/bin/sh
#grep -F -f aaa.txt bbb.txt|sort >intersection.out.txt
echo -n 'Enter your File one: '
read f1
echo -n 'Enter your File two: '
read f2
grep -F -f  $f1 $f2 |sort >intersection.out.txt
echo 'intersection of '$f1'and' $f2' have saved in intersection.out.txt'

