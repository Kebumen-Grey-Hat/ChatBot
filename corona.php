<?php

$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,"https://infeksiemerging.kemkes.go.id");
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch,CURLOPT_POST, 1);
$res = curl_exec($ch);

$js = json_encode($res);
print_r($js);

?>
