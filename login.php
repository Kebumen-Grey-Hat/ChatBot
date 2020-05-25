<?php

echo "

<!DOCTYPE html>
<html>
<head>
<title>ADMIN SCHOOL HACKING</title>
<script>
alert('welcome to admin school hacking')
</script>
</head>
<br>
<br>
<br>
<br>
<br>
<table border='1' cellpadding='20'>
</tr>
<tr>
<th>
<p id='pesan'>
<form action='#'>
<input type='text' id='fusername' placeholder='USERNAME'><br>
<input type='password' id='fpassword' placeholder='PASSWORD'><br>
<input type='submit' value='LOGIN' onclick='LOGIN();'><br>
</form>

<script>
function Login(){
      var usr = document.getElementById('FUSERNAME').value;
      var pas = document.getElementById('FPASSWORD').value;
      if(usr===''){
        document.getElementById('pesan').innerHTML = 'masukan username';
      }else if(pas===''){
        document.getElementById('pesan').innerHTML = 'masukan password';
      }else if(usr==='admin' && pas=='restugans'){
        alert('LOGIN SUCCESFULLY');
      }else{
        alert('LOGIN FAILED');
      }
      }
      </script>
      </html>
"
?>
