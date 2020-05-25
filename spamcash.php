<?php


function send($nomor){
     $ch = curl_init();

     curl_setopt($ch,CURLOPT_URL,"https://www.tokocash.com/oauth/otp");
     curl_setopt($ch,CURLOPT_RETURNTRANSFERS, 1);
     curl_setopt($ch,CURLOPT_POST, 1);

     $respon = curl_exec($ch);
}

echo "MASUKAN NOMOR: ";
$nomor = trim(fgets(STDIN));


