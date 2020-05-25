<?php



echo "


<!DOCTYPE html>
<html>
<head>
<title>INPUT OUTPUT BARANG</title>
<script>
alert('WELCOME TO PHP WEB');
</script>
<body bgcolor='yellow'>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<center>
<table border='1' bgcolor='blue' background='white'>
<tr>
<form action='' method='POST'>
<td><input type='text' name='barang1' placeholder='NAMA BARANG'></td><br>
</tr>
<tr>
<td><input type='text' name='harga1' placeholder='HARGA BARANG'></td><br>
</tr>
<tr>
<td><input type='text' name='jumlah1' placeholder='JUMLAH BARANG'></td><br>
</tr>
</center>
<center>
<td><input type='submit' value='SUBMIT'></td><br>
</center>
</form>
</table>
</html>
<table border='1' bgcolor='blue'>
<td>NAMA BARANG  : $_POST[barang1]</td><br>
<td>HARGA BARANG : $_POST[harga1]</td><br>
<td>JUMLAH BARANG: $_POST[jumlah1]</td><br>
</table>
"
?>
