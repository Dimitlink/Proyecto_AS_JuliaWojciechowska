<!DOCTYPE html>
<!--Fichero html que muestra el servidor http-->
<html>
<head>
<!--Título de la página web-->
  <title>Data</title>
  <!--Definición del estilo de la página web-->
  <style>
   body {
  background-color: lightyellow;
  }
  h1 {
  color: black;
  font-family: arial;
  }
  h2 {
  color: black;
  font-family: arial;
  font-size: 23px;
  }
  p {
  font-family: arial;
  font-size: 20px;
  }
  </style>
</head>
<!--Cuerpo de la página web-->
<body>
  <h1>Data in the database capitals</h1>
  <h2>Table capitals</h2>
  <p>
    <!--Script en PHP cuya función es imprimir los datos del fichero txt-->
    <?php
    //Apertura del fichero
    $data = fopen("data.txt", "r");
    if ($data) {
    //Mientras el fichero txt contiene texto
      while (($line = fgets($data)) !== false) {
        //Se imprime el texto línea por línea
        echo $line;
        echo nl2br("\n");
    }
    //Cierre del fichero
    fclose($data);
    }  
    ?>
  </p>
</body>
</html>


