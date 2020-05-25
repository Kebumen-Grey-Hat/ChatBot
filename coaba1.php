<?php


$yu = curl_init();
curl_setopt($yu,CURLOPT_URL,"http://localhost:4444");
curl_setopt($yu,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($yu,CURLOPT_POST, 1);
$respon = curl_exec($yu);


$js = json_decode($respon);
print_r($js);


?>
