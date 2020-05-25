<?php


echo "

<html>
<form action='' method='POST'>
Nama :<br>
<input type='text' name='nama'><br>
<input type='radio' name='jenis' value='L'>Laki-Laki<br>
<input type='radio' name='jenis' value='P'>Perempuan<br>
<input type='submit' value='simpan'><br>
</form>
</html>

Nama Lengkap  : $_POST[nama]<br>
Jenis Kelamin : $_POST[jenis]<br>

"
?>
