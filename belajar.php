






<?php









echo "Hello Dunia Saya Sedang Belajar Php\n";

$nama = "ARJUNA AGUNG MAULANA";
echo "NAMA ANDA: ".$nama;"\n";
$umur = 15;
echo "\nUMUR ANDA: ".$umur;"\n";


// kondisi

$temen = "Doni";

if ($temen == "Andy"){
   echo "\n".$temen." Adalah Teman Saya";
}else{
   echo "\n".$temen." Bukan Teman Saya";
}


// perulangan

$no = 0;

while (True){
    $no++;
    echo "\nPerualangan While Ke:". $no;"\n";
    sleep(1);
    if ($no == 5){
       break;
    }
}


echo "/nMasukan Nama Anda:\n";

echo '<input type="text" name="nama">'



?>

