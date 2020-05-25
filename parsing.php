<?php

$ch = curl_init();

$url = "https://whatismyipaddress.com";

curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch,CURLOPT_POST, 1);

$result = curl_exec($ch);

$one = explode('<title>', $result);
$two = explode('</title>', $one[0]);

echo $two[0]."\n";

?>
