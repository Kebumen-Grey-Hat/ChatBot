<?php

echo "
<html>
<head>
<title>Input Output Barang</title>
<script>
alert('Selamat Datang');
</script>
</head>
<body bgcolor='green'>
<center>
<br>
<br>
<br>
<br>
<br>
<br>
<h1>Input Barang</h1>
<br>
<table border='1' bgcolor='white' background='black' cellpadding='50'>
</tr>
<tr>
<th>
<table border='1' width='10px' height='10px'>
<tr>
<form action='' method='POST'>
<td>Nama Barang   : <input type='text' name='nama_barang'></td><br>
<td>Harga Barang  : <input type='text' name='harga_barang'></td><br>
<td>Jumlah Barang : <input type='text' name='jumlah_barang'></td><br>
<br>
<br>
</table>
<input type='submit' value='Simpan'><br>
</form>
</table>
<br>
<br>
<table border='1' bgcolor='blue' backgroud='red' cellpadding='200'>
<tr>
<th>
Nama Barang   : $_POST[nama_barang]<br>
Harga Barang  : $_POST[harga_barang]<br>
Jumlah Barang : $_POST[jumlah_barang]<br>
</table>
</html>

"
?>
