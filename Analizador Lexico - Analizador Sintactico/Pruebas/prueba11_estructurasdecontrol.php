<?php

//Prueba de estructura de Control


if ($a > $b) {
    echo "a es mayor que b";
} elseif ($a == $b) {
    echo "a es igual que b";
} else {
    echo "a es menor que b";
}


//if ($a > $b):
//    echo $a."es mayor que".$b;
//else if ($a == $b): // No compilará
//    echo "La linea anterior provoca un error del interprete.";
//endif;

$i = 0;
do {
    echo $i;
} while ($i > 0);

$i = 1;
for ($i = 0; $i<100 ; $i++ ) {
    //if ($i > 10) {
    //    $i = $i //break;
    //}
    echo $i;
    $i++;
}

$array = array(1, 2, 3, 4);
foreach ($array as $valor) {
    $valor = $valor * 2;
}


switch ($i) {
    case 0:
        echo "i es igual a 0";
        //$y = $x * 1;
        break;
    case 1:
        echo "i es igual a 1";
        break;
    case 2:
        echo "i es igual a 2";
        break;
}



echo "b";
return;


?>
