<?php





function send($phone){
   $ch = curl_init();
   curl_setopt($ch,CURLOPT_URL,"https://www.tokocash.com/oauth/otp");
   curl_setopt($ch,CURLOPT_SSL_VERIFYPEER, true);
   curl_setopt($ch,CURLOPT_FOLLOWLOCATION, true);
   curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);
   curl_setopt($ch,CURLOPT_HEADER, true);
   curl_setopt($ch,CURLOPT_POST, true);
   curl_setopt($ch,CURLOPT_POSTIELDS,"msisdn=$phone");
   $res = curl_exec($ch);
   echo $res."\n";


}
echo "MASUKAN NOMOR: ";
$nomor = trim(fgets(STDIN));

$execute = send($nomor);

print $execute;



?>

