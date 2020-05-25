echo "Ecit y/n"
read pil;

if [ $pil = "y" ];
then
   echo "loading"
   exit -y
else
   echo "salah"
fi
