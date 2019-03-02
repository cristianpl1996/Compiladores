<?php
class BaseClass {
   function __construct() {
       echo "string"; echo "En el constructor BaseClass\n";
   }
}

class SubClass extends BaseClass {
   function __construct() {

       echo "En el constructor SubClass\n";
   }
}

class OtherSubClass extends BaseClass {
    // heredando el constructor BaseClass
}

// En el constructor BaseClass
$obj = new BaseClass();

// En el constructor BaseClass
// En el constructor SubClass
$obj = new SubClass();

// En el constructor BaseClass
$obj = new OtherSubClass();
?>
