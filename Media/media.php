<!DOCTYPE html>
<html>
    <head> 
    <link href="CSS/style.css" rel="stylesheet">       
        <title>Calculando media</title>
    </head>
<body>
  <div>
<form action='' method="get">
   <input type="text" placeholder="nota 1" name="num1">
   <br><br>
   <input type="text" placeholder="nota 2" name="num2">
   <br><br>
   <input type="text" placeholder="nota 3" name="num3">
   <br><br>
   <button type="submit">Calcular</button>
</form>
  </div>
<span class="resultado">
<?php
$num1 = $_GET['num1'];
$num2 = $_GET['num2'];
$num3 = $_GET['num3'];

$media = ($num1 + $num2 + $num3)/3;

echo "Sua média é: $media";
?>
</span>
</body>
</html>