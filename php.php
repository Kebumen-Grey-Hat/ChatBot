<?php

// Belajar Membuat Project Sederhana Php

echo "Hay kak masukan code verifikasi script => ";
      $pil = trim(fgets(STDIN));

if($pil == 240604){
   sleep(3);
   echo "Login Berhasil";
   sleep(3);
   system('clear');
}else{
   sleep(3);
   echo "kode verifikasi failed please check your code";
}

?>
