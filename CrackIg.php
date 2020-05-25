
<?php


$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,"https://mtsn8kebumen.sch.id/wp1/");
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch,CURLOPT_POST, 1);

$respon = curl_exec($ch);


$res = explode('<h1 class="site-title"><a href="https://mtsn8kebumen.sch.id/wp1/" rel="home">',$respon);

$one = explode('</a></h1>',$res[1]);
echo $one[0];


?>
