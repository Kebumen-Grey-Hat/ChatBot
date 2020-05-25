<?php


$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,"http://localhost:8080");
curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch,CURLOPT_POST, true);

$respon = curl_exec($ch);

echo $respon;

?>
