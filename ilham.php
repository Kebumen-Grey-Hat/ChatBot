<?php

echo "
<br>
<br>
<br>
<br>
<br>
<p name='pesan'>

<form action='#' method='POST'>
USERNAME : <input type='text' nane='username'><br>
<input type='submit' value='Login' onclick='Login();'><br>
</form>

<script>
function Login(){
       var usr = document.getElementByname('username').value;
       if(usr===''){
         document.getElementByname('pesan').innerHTML = 'Masukan Usernane';
       }else if(usr==='admin'){
         alert('Username Cocok');
       }else{
         alert('username tdk cocok');
       }
       }
       </script>

USERNAME ANDA : $_POST[username]<br>

"



?>
