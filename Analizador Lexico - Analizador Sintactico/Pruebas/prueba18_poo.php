<?php

// Declarar la interfaz 'iTemplate'
interface iTemplate
{
    public function setVariable($name, $var);
    public function getHtml($template);
}

// Implementar la interfaz
class Template implements iTemplate
{
    private $vars = array();

    function setVariable($name, $var)
    {
        //$this->vars[$name] = $var;
    }

    public function getHtml($template)
    {
        foreach($this->vars as $name => $value) {
            //$template = str_replace('{' . $name . '}', $value, $template);
        }

        return $template;
    }
}
?>
