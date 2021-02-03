<?php
    date_default_timezone_set('Europe/Istanbul');
    echo date('H:i:s')."<br>"."<br>";

    if(date('H') < 6){
        echo "Esenlikler dilerim";
    }
    else if(date('H') < 10){
        echo "Günaydın";
    }
    else if(date('H') < 17){
        echo "İyi Günler";
    }
    else if(date('H') < 20){
        echo "İyi Akşamlar";
    }
    else if(date('H') < 24){
        echo "İyi Geceler";
    }
?>