<?php

function main(){
         echo "[1]. penambahan"."\n";
         echo "[2]. pengurangan"."\n";
         echo "[3]. perkalian"."\n";
         echo "[4]. pembagian"."\n";

         echo 'Input Your Number: ';
         $pil = trim(fgets(STDIN));
         if ($pil == 1){
             echo 'Input Angka Pertama: ';
             $a = trim(fgets(STDIN));
             echo 'Input Angka Kedua: ';
             $b = trim(fgets(STDIN));
             $tmb = ($a + $b);
             echo "Hasil Dari ".$a." + ".$b." = ".$tmb."\n";
             echo 'Ingin Mengulang (Y/n) : ';
             $Vok = trim(fgets(STDIN));
             if ($Vok == Y){
                 main();
             }else{
                 echo 'Bye Bye..';
             }
         }else{
                 echo 'Wrong Input Eror';
         }
}
main();
?>
