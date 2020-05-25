<?php

$url = "http://localhost:8080";

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL, $url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch,CURLOPT_POST, 1);

$respon = curl_exec($ch);

$js = json_encode($respon);
print_r($js);

?>
