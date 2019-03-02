<?php
class ClaseExtendida extends ClaseSencilla
{
    // Redefinición del método padre
    function mostrarVar()
    {
        echo "Clase extendida\n";
        //parent::mostrarVar();
    }
}

$extendida = new ClaseExtendida();
$extendida->mostrarVar();
?>
