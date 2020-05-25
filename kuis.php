<?php
system('clear');

echo "[~] Jawab Soal Dengan Baik Semoga Sukses [~]\n";
"\n";
"\n";
$a = 5;
$b = 1;




echo "\n";
echo "1. Bahasa Python adalah bahasa yang pemrograman tingkat tinggi\n";
echo "Banyak orang yang menggunakan bahasa python karena keunggulanya\n";
echo "bahasa python di ciptakan oleh seseorang bernama ...??\n";
echo "\n";
echo "A. James Krypto\n";
echo "B. Guido Van Rossum\n";
echo "C. Pro.James Van Raise\n";
echo "D. Ali Al Jabar\n";


echo "JAWAB : ";
$pil = trim(fgets(STDIN));

if ($pil == "B"){
    echo "Jawaban Benar [√]\n";
    $t = ($a * $b);
    echo "Nilai anda adalah ".$t."\n";
    sleep(3);
}else{
    echo "Jawaban Salah [?]";
    echo "Nilai Anda 0\n";
}




echo "\n";
echo "2. Pengertian Deface Upload File Menurut Bahasa Indonesia\n";
echo "\n";
echo "A. Menghilangkan Tampilan Website\n";
echo "B. Mengubah Semua Tampilan Depan Website\n";
echo "C. Hanya Mengubah Di Bagian Upload\n";
echo "D. Menghapus Directory Website\n";

echo "JAWAB : ";
$wa = trim(fgets(STDIN));
if ($wa == "C"){
    $y = ($t + $a);
    echo "Jawaban Benar Nilai Anda Sekarang ".$y."\n";
}else{
    echo "Jawaban Salah Nilai Anda Masih ".$t."\n";
}
?>
