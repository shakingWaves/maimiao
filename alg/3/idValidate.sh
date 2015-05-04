#!/bin/sh
echo -n "Enter your id:"
read id
if [ ${#id} -ne 18 ] ;then
	echo "Your iiiid is wrong"
	exit
fi
echo "Your id is : $id"
#校验行政区划代码是否正确
region=$(grep ${id:0:6} idcode.txt)
if [ -z region ];then   #测试返回值是否为零，为零表明不存在该行政区划
	echo "Your id is wrong"
	exit
else
	echo "Your region is : $region "
fi
#校验生日是否符合要求
birth=${id:6:8}  #获取生日部分
echo "Your birthday is : $birth"
regl="(19|20)\d{2}(1[0-2]|0[1-9])(0[1-9]|[1-2][0-9]|3[0-1])" #生日正则表达式
year=${id:6:4}
month=${id:10:2}
days=${id:12:2}
#删除月份和日期的前导0
month=$(echo $month|sed 's/^0//')
days=$(echo $days|sed 's/^0//')
#echo $year
#echo $month
#echo $days
#leap year 
if [ $[year % 400 ] -eq 0 ] && [ $[year % 4 ] -eq 0 -o  $[year % 100 ] -ne 0  ];then
	if [ $[month] -eq 2 -a  $[days] -gt 29  ];then
		echo "birthday error"
		exit
	fi  
else
	if [ $[month] -eq 2 -a $[days] -gt 28  ];then
                echo "birthday error"
		exit
        fi
fi  
#身份证序号和校验码判断
weight=(7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2)
checkCode=(1 0 10 9 8 7 6 5 4 3 2)
result=0
for i in $(seq 17);do
	#echo ${id:i-1:1}
	#echo ${weight[$i-1]}
	result=$[result+$[${weight[$i-1]}*${id:i-1:1}]]
	#echo $result
done;
result=$[$[result]%11]
#echo $result
#echo $[${checkCode[$[result]]}]
if [ $[${checkCode[$[result]]}] -eq  ${id:17:1} ];then
	echo "Your id is correct!"
else
	echo "check code error"
	echo "Your id is incorrect!"
fi
