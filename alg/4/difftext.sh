#!/bin/sh
#comm <(sort aaa.txt) <(sort bbb.txt) -2 -3
echo -n 'Enter your File one: '
read f1
echo -n 'Enter your File two: '
read f2
grep -F -v -f $f1 $f2
echo 'intersection of '$f1'and' $f2' have saved in diff.out.txt'

