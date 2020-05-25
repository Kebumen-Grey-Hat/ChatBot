<?php

$ch = curl_init();

//CURLOPT_URL itu di isi link atau API otp sms nya
echo "Input No : ";
$no = trim(fgets(STDIN));

curl_setopt($ch, $no, CURLOPT_URL, "https://register.grab.com/id/otp?country_code=ID&phone_number=NP%2FxAwEBB3BheWxvYWQB%2F%2FIAAQMBA0tleQEKAAEFTm9uY2UB%2F%2FQAAQdNZXNzYWdlAQoAAAAZ%2F%2FMBAQEJWzI0XXVpbnQ4Af%2F0AAEGATAAAP4BB%2F%2FyAf%2B4AQIBAHgvV83s1VfqAUxU30fUPV8Mn53rdvPTSgi3FQcpogojrQFHnS5A2L4%2FSTZBdApqnyFzAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMInVVo0EbnyzwrohAAgEQgDuqJe%2FT2q6BglTiTJxX%2FggoteZXND9Pi655ysNOy9smotvjB1paWHhJZcy%2FbaowjrszZh8zeExZuyRufAEY%2F4n%2FqR3%2F1B9gcP%2F6Gf%2Ba%2F5oK%2F%2FMK%2F4n%2Ftxf%2Fm%2F%2FbNP%2FY%2F4f%2F4P%2BFAR6FOh0iiagPVF5nDAIezbxbBZ2FvgVD1AzYTw5R6U4A%7C2666&grabcom_form=1&grabcom_service=GB&grabcom_phone=0d3940beb09803995a54f77a5c6289fe0b0a2eebe1508c9edf508239e9f9e84c");
curl_setopt($ch, $no, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, $no, CURLOPT_POST, 1);

//CURLOPT_POSTFIELDS di isi dengan data yang mau kita post atau kirim, liat di bagian contoh email & nomer hp target di bawah

$x = curl_exec($ch);
curl_close($ch);

//karena bentuk respon nya masih JSON, maka kita decode dulu

$js = json_decode($x);
print_r($js);

?>

