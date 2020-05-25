<?php



echo "

<!DOCTYPE html>
<html>
<head>
<title>LOGIN MEMBER</title>
</head>
<body bgcolor='yellow'>
<br>
<br>
<br>
<br>
<br>
<br>
<center>
<p id='pesan'>
<form action=''>
<input type='text' id='fusername' placeholder='username'><br>
<input type='password' id='fpassword' placeholder='password'><br>
<input type='submit' value='LOGIN' onclick='LOGIN();'><br>
</form>
</html>

<script>
function LOGIN(){
         var usr = document.getElementById('fusername').value;
         var pas = document.getElementById('fpassword').value;
         if(usr===''){
             document.getElementById('pesan').innerHTML = 'masukan usrrname';
         }else if(pas===''){
             document.getElementById('pesan').innerHTML = 'masukan password';
         }else if(usr==='admin' && pas=='12345'){
             alert('LOGIN BERHASIL');
         }else{
             alert('LOGIN GAGAL');
         }
         }
</script>
</html>
"
?>
