<?php
?>
<html>
<head>
    <title>Asal sayı</title>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
</head>
<body>
<form aciton = "?" method = "post">
    <h1>Asal Sayı Ölçer</h1>
    <h2>Lütfen bir sayı giriniz</h2>
    <input type = "text" name = "sayi" id = "sayi" autocomplete="off">
    <br><br>
    <button type = "button" name = "gonder" id = "gonder">Doğrula</button>
</form>
<script type="text/javascript">
$("#gonder").click(function(){
    var sayi = $("#sayi");
    var x = 0;

    for (let i = 0; i < sayi.val(); i++) {
        if(sayi.val()%i==0){
            x += 1;
        }     
    }   
    
    if(x == 1){
        alert("Girdiğiniz sayı asal sayıdır");
    }
    else{
        alert("Girdiğiniz sayı asal sayı değildir");
    }

});
</script>
</body>
</html>
