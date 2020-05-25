<?php

$url = "https://ipapi.co/112.215.154.150/json/";

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL, $url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch,CURLOPT_POST, 1);
$respon = curl_exec($ch);

$js = json_decode($respon);
print_r($js);

?>
