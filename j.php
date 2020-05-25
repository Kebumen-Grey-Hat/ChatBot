<?php


$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,"http://ip-api.com/json/24.48.0.1");
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch,CURLOPT_POST, 1);

$respon = curl_exec($ch);


$js = json_decode($respon);
print_r($js);



?>
