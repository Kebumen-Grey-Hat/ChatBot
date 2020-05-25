
R='\x1b[1;31m'
G='\x1b[1;32m'
B='\x1b[1;34m'
Y='\x1b[1;33m'
C='\x1b[1;36m'
D='\x1b[0m'



function Percent(){
    message="$1"
    max=$2
    #make loop
    while true; do
        i=0
        while [ $i -le $max ]; do
            echo -ne "\r${G}[+]${D} $message ${C}$i${D} %"
            sleep 0.1
            if [ $i -eq 100 ]; then
                echo -ne "${C} [complete!]${D}\n"
                Percent "Loading..." 100
            fi
            let i++
        done
    done
}
Percent "Loading..." 100

project1(){
        echo 'What Do You Whant to Continue (y/N)'
        read pil;
        if [ $pil == 'y' ] || [ $pil == 'Y' ];
        then
           clear
           python2 banner.py
           precent "Wait Project.."
           read -p 'input number one : ' one;
           read -p 'input number two : ' two;
           $tmb = ($one / $two);
           echo 'Result to '$one'/'$two'='$tmb
        else
           echo 'Wrong Input Eror..!!!'
           sleep 2
           echo 'Bye Bye Sayang'
           exit
        fi
project1()
