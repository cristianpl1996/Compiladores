<?php
// OJO: estos metodos ya NO ESTAN soportados.
// Los validos estan descritos arriba.

// Usar import_request_variables() - esta funcion ha sido eliminada en PHP 5.4.0
   import_request_variables('p', 'p_');
   echo $p_username;

// Usar register_globals. Esta caracteristica fue eliminada en PHP 5.4.0
   echo $username;
?>
