<?php

echo " 1. Nasi Goreng => 15.000\n";
echo " 2. Mie Ayam => 12.000\n";
echo " 3. Bakso Ceker => 20.000\n";

$nasi_goreng = 15000;
$mie_ayam = 12000;
$bakso = 20000;

echo "Pilih Menu : ";
$pil = trim(fgets(STDIN));


if ($pil == 1){
    echo "Jumlah Uang Anda : ";
    $ug = trim(fgets(STDIN));
    $kur = ($ug - $nasi_goreng);
    if ($ug >= $nasi_goreng){
          echo "Anda Dapat Membeli Sisa Uang Anda ".$kur."\n";
    }else{
          echo "Uang Anda Kurang ".$kur."\n";
    }
}



if ($pil == 2){
    echo "Jumalah Uang Anda : ";
    $uang = trim(fgets(STDIN));
    $ku = ($uang - $mie_ayam);
    if ($uang >= $mie_ayam){
        echo "Anda Dapat Membeli Sisa Uang Anda Adalah ".$ku."\n";
    }else{
        echo "Anda Tidak Dapat Membeli Uang Anda Kurang ".$ku."\n";
    }
}

if ($pil == 3){
    echo "Jumlah Uang Anda : ";
    $wng = trim(fgets(STDIN));
    $kul = ($wng - $bakso);
    if ($wng >= $bakso){
        echo "Anda Dapat Membeli Sisa Uang Anda Adalah ".$kul."\n";
    }else{
        echo "Uang Anda Kurang ".$kul."\n";
    }
}


?>

