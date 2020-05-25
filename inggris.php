<?php



$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,"http://localhost:8080");
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch,CURLOPT_POST, 1);

$respon = curl_exec($ch);


$satu = explode("<form action=''>", $respon);

$dua = explode("</form>", $satu[1]);

echo $dua[0];




?>
