#!/bin/bash

printf "cc/cf/atc/other? "


read CONPLT

cd ..
if [ "$CONPLT" = "cf" ]
then
    echo "Entering as cf"
    echo "Round? "
    read ROUND
    echo "div? "
    read DIV
    mkdir "Cf_""$ROUND""_div""$DIV"
    
    cp temp.cpp "Cf_""$ROUND""_div""$DIV"/A.cpp
    cp temp.cpp "Cf_""$ROUND""_div""$DIV"/B.cpp
    cp temp.cpp "Cf_""$ROUND""_div""$DIV"/C.cpp
    cp temp.cpp "Cf_""$ROUND""_div""$DIV"/D.cpp
    touch "Cf_""$ROUND""_div""$DIV"/input.txt
    touch "Cf_""$ROUND""_div""$DIV"/output.txt
    echo "Cf_""$ROUND""_div""$DIV"
    
elif  [ "$CONPLT" = "cc" ]
then
    echo "Entering as cc"
    
    printf "Long / Cook-off / Lunchtime / others?  "
    read ROUND
    printf "Month?"
    read MONTH
    echo "div?"
    read DIV
    mkdir "CC_""$MONTH""_""$ROUND""_div""$DIV"
    
    cp temp.cpp "CC_""$MONTH""_""$ROUND""_div""$DIV"/1.cpp
    cp temp.cpp "CC_""$MONTH""_""$ROUND""_div""$DIV"/2.cpp
    cp temp.cpp "CC_""$MONTH""_""$ROUND""_div""$DIV"/3.cpp
    cp temp.cpp "CC_""$MONTH""_""$ROUND""_div""$DIV"/4.cpp
    touch "CC_""$MONTH""_""$ROUND""_div""$DIV"/input.txt
    touch "CC_""$MONTH""_""$ROUND""_div""$DIV"/output.txt
    echo "CC_""$MONTH""_""$ROUND""_div""$DIV"

elif  [ "$CONPLT" = "atc" ]
then
    echo "Round? "
    read ROUND
    echo "div? "
    read DIV
    mkdir "ATC_""$ROUND""_div""$DIV"
    
    cp temp.cpp "ATC_""$ROUND""_div""$DIV"/A.cpp
    cp temp.cpp "ATC_""$ROUND""_div""$DIV"/B.cpp
    cp temp.cpp "ATC_""$ROUND""_div""$DIV"/C.cpp
    cp temp.cpp "ATC_""$ROUND""_div""$DIV"/D.cpp
    touch "ATC_""$ROUND""_div""$DIV"/input.txt
    touch "ATC_""$ROUND""_div""$DIV"/output.txt
    echo "ATC_""$ROUND""_div""$DIV"
else
    printf "title?"
    read ROUND
    mkdir $ROUND
    cp temp.cpp $ROUND/1.cpp
    cp temp.cpp $ROUND/2.cpp
    cp temp.cpp $ROUND/3.cpp
    cp temp.cpp $ROUND/4.cpp
    cp temp.cpp $ROUND/5.cpp
    cp temp.cpp $ROUND/6.cpp
    touch $ROUND/input.txt
    touch $ROUND/output.txt
    echo $ROUND
fi
