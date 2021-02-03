<?php
?>
<html>
<head>
    <title>En az para ile para üstü</title>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
</head>
<body>
<form aciton = "?" method = "post">
    <h1>En az para ile para üstü</h1>
    <h2>Lütfen para üstünü giriniz</h2>
    <h3>Para Üstü (2 Lira 57 Kuruş = 2.57)</h3>
    <input type = "" name = "sayi" id = "sayi" autocomplete="off">
    <br><br>
    <button type = "button" name = "gonder" id = "gonder">Hesapla</button>
</form>
<script type="text/javascript">
$("#gonder").click(function(){
    var sayi = $("#sayi");  

    var num = sayi.val()*100;
    var bir_tl = 0;
    var ceyrek_kurus = 0;
    var on_kurus = 0;
    var bir_kurus = 0;
    var x = 0;
    x = num%100;
    bir_tl = (num - x)/100;
    ceyrek_kurus = parseInt(x/25);

    if(x%25 < 10){
        bir_kurus = x%25;
        on_kurus = 0;
    }
    else{
        on_kurus = parseInt((x%25)/10);
        bir_kurus = (x%25)%10;
    }

    alert(bir_tl + " adet 1TL, " + ceyrek_kurus + " adet 25 kuruş, " + on_kurus + " adet 10 kuruş, " + bir_kurus + " adet 1 kuruş para üstü verilmelidir.");

});
</script>
</body>
</html>
