<?php
class A
{
    public $var1 = 0;
    private $var2;
    protected $var3 = "jeje";

    function foo()
    {
        if ($this) {
            echo '$this esta definida (';
            echo $this;
            echo ")\n";
        } else {
            echo "\$this no esta definida.\n";
        }
    }
}




?>
