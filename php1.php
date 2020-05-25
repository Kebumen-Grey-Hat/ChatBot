<?php

// variabel
/*
$nama = "ARJUNA AGUNG MAULANA";
$umur = 15;
$hobi = "FUTSAL";

echo "Nama Anda: ". $nama."\n";
echo "Umur Anda: ". $umur."\n";
echo "Hobi Anda: ". $hobi."\n";
*/



// input dan output
/*
echo "Nama: ";
$nam = trim(fgets(STDIN));

echo "SELAMAT DATANG ". $nam. " DI PHP"."\n";
*/



// kondisi

/*
$uang = 1000;

if ($uang == "2000"){
    echo "Uang Anda Cukup";
}else{
    echo "Uang anda Kurang";
}
*/




// percabangan

echo "1. Andy"."\n";
echo "2. Fendy"."\n";
echo "3. Tony"."\n";

echo "Pilih Teman Anda: ";
$teman = trim(fgets(STDIN));

if ($teman == "1"){
    echo "Andy Adalah Teman Anda";
if ($teman == "2"){
    echo "Fendy Juga Teman Anda";
if ($teman == "3"){
    echo "Tony Teman Lama Kamu";
}
}
}
