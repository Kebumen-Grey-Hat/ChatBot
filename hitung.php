<?php

echo "

<html>
<body>
<p></p>
<script>

var harga = 100.000;
var uang = 200.000;

if(harga == uang){
document.getElementsByTagName('p')[0].innerHTML = 'Kamu Dapat Membeli Uang Kamu Pas';
}else if(harga < uang){
document.getElementsByTagName('p')[0].innerHTML = 'Kamu Dapat Membeli Uang Kamu Masih Sisa';
}else{
document.getElementsByTagName('p')[0].innerHTML = 'Kamu Tidak Dapat Membeli Uang Kamu Kurang';
}
</script>
</body>

</html>
"
?>


