<?php


$url = "https://www.tokocash.com/aouth/otp";

echo "NO: ";
$no = trim(fgets(STDIN));


$no = curl_init();

curl_setopt($no,CURLOPT_URL, $url);
curl_setopt($no,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($no,CURLOPT_POST, 1);

$respon = curl_exec($no);


$js = json_decode($respon);
print_r($js);

?>
