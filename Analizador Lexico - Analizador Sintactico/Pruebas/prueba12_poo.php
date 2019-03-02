<?php
class ClaseSencilla
{
    // Declaración de una propiedad
    public $var = 'un valor predeterminado';

    // Declaración de un método
    public function mostrarVar() {
        echo $this->var;
    }
}




class A
{
    function foo()
    {
        if (isset($this)) {
            echo '$this esta definida (';
            echo get_class($this);
            echo ")\n";
        } else {
            echo "\$this no esta definida.\n";
        }
    }
}

class B
{
    function bar()
    {
        A::foo();
    }
}

$a = new A();
$a->foo();

A::foo();
$b = new B();
$b->bar();

B::bar();

?>
