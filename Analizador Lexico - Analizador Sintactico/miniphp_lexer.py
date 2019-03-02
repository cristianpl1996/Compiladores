import ply.lex as lex
import sys
import glob
import os.path as path

# list of tokens
tokens = (
# Reserverd words
    'TRUE',
    'FALSE',
    'ECHO',
    'FUNCTION',
    'INCLUDE',
    'RETURN',
    'ITERABLE',
    'ARRAY',
    'AS',
    'CLASS',
    'NEW',
    'OBJECT',
    'ISSET',
    'THROW',
    'EMPTY',
    'INSTANCEOF',
    'NULL',
    "CMETHOD",
    "DEFINE",
    "CONST",
    "EXTENDS",
    "CONSTRUCTOR",
    "DESTRUCTOR",
    "PUBLIC",
    "PRIVATE",
    "PROTECTED",
    "STATIC",
    "IMPLEMENTS",
    "INTERFACE",
    "ABSTRACT",
    "TRAIT",
    "USE",
    'NAMESPACE',
    '__UNSET',
    'UNSET',
    '__SET',
    '__GET',
    '__ISSET',
    '__CALL',
    '__CALLSTATIC',
    '__SLEEP',
    '__WAKEUP',
    '__TOSTRING',
    '__INVOKE',
    '__SET_STATE',
    '__CLONE',
    '__DEBUGINFO',
    '__CLASS__',
    'MIXED',
    'FINAL',
    'SELF',
    'SERIALIZE',
    'UNSERIALIZE',
    'SPL_AUTOLOAD_REGISTER',
    'DOUBLECOLONCLASS',
    'GET_CLASS', #::CLASS

    # Control structures
    'IF',
    'ELSE',
    'ELSEIF',
    'WHILE',
    'DO',
    'FOREACH',
    'FOR',
    'BREAK',
    'CONTINUE',
    'SWITCH',
    'CASE',
    'DECLARE',
    'REQUIRE',
    'REQUIRE_ONCE',
    'INCLUDE_ONCE',
    'GOTO',

# Symbols
    'LPARENTHESIS',
    'RPARENTHESIS',
    'LKEY',
    'RKEY',
    'LSBRACKETS',
    'RSBRACKETS',
    'TWOPOINTS',
    'COMMA',
    'SEMICOLON',

    # Arithmetic operators
    'MINUS',
    'PLUS',
    'TIMES',
    'DIV',
    'MODULE',
    'EXPONENTIATION',

    # Assignment operator
    "EQUAL",
    'EQUALG',

    #Reference operator
    'REFERENCE',

    # Comparison Operators
    'EQUALEQUAL',
    'NEQUAL',
    'IDENTICAL',
    'GREATER',
    'GEQUAL',
    'LESS',
    'LEQUAL',

    # Logical operators
    'AND',
    'OR',
    'XOR',
    'NOT',

    # String operators
    'CONCATSTR',

    #scope control Operators
    'DOUBLE_COLON',
# Identifiers, Numbers, etc
    'SLABEL',
    'ELABEL',
    'ID',
    'STRING',
    'NFUNCTION',
    'FLOAT',
    'INTEGER',
# default
    'DEFAULT'
)

# Reserverd words
def t_TRUE(t):
    r'TRUE|true|True'
    return t

def t_FALSE(t):
    r'FALSE|False|false'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_ITERABLE(t):
    r'iterable'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_AS(t):
    r'as'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_NEW(t):
    r'new'
    return t

def t_OBJECT(t):
    r'object'
    return t

def t_ISSET(t):
    r'isset'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_NULL(t):
    r'NULL|Null|null'
    return t

def t_CMETHOD(t):
    r'->'
    return t

def t_DEFINE(t):
    r'define'
    return t


def t_CONST(t):
    r'const'
    return t

def t_EXTENDS(t):
	r'extends '
	return t

def t_CONSTRUCTOR(t):
	r'__construct'
	return t

def t_DESTRUCTOR(t):
	r'__destruct'
	return t

def t_PUBLIC(t):
	r'public'
	return t

def t_PRIVATE(t):
	r'private'
	return t

def t_PROTECTED(t):
	r'protected'
	return t

def t_STATIC(t):
	r'static'
	return t

def t_IMPLEMENTS(t):
	r'implements'
	return t

def t_INTERFACE(t):
	r'interface'
	return t

def t_ABSTRACT(t):
	r'abstract'
	return t

def t_TRAIT(t):
	r'trait'
	return t

def t_USE(t):
	r'use'

	return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t___UNSET(t):
    r'__unset'
    return t

def t_UNSET(t):
    r'unset'
    return t

def t___SET(t):
    r'__set'
    return t

def t___GET(t):
    r'__get'
    return t

def t___ISSET(t):
    r'__isset'
    return t

def t___CALL(t):
    r'__call'
    return t

def t___CALLSTATIC(t):
    r'__callstatic'
    return t

def t___SLEEP(t):
    r'__sleep'
    return t

def t___WAKEUP(t):
    r'__wakeup'
    return t

def t___TOSTRING(t):
    r'__toString'
    return t

def t___INVOKE(t):
    r'__invoke'
    return t

def t___SET_STATE(t):
    r'__set_state'
    return t

def t___CLONE(t):
    r'__clone'
    return t

def t___DEBUGINFO(t):
    r'__debugInfo'
    return t

def t___CLASS__(t):
    r'__class__'
    return t

def t_MIXED(t):
    r'mixed'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_SELF(t):
    r'self'
    return t

def t_SERIALIZE(t):
    r'serialize'
    return t

def t_UNSERIALIZE(t):
    r'unserialize'
    return t

def t_SPL_AUTOLOAD_REGISTER(t):
    r'spl_autoload_register'
    return t

def t_DOUBLECOLONCLASS(t):
    r'::class'
    return t

def t_GET_CLASS(t):
    r'get_class'
    return t
    # Control structures

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_REQUIRE_ONCE(t):
    r'require_once'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_DEFAULT(t):
    r'default'
    return t

# Symbols
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LSBRACKETS = r'\['
t_RSBRACKETS = r']'
t_TWOPOINTS = r':'
t_COMMA = r','
t_SEMICOLON = r';'

    # Arithmetic operators
t_MINUS = r'\-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIV   = r'/'
t_MODULE = r'%'
t_EXPONENTIATION = r'\*\*'

    # Assignment operator
t_EQUAL = r'='

def t_EQUALG(t):
    r'=>'
    return t

    # Reference operator
t_REFERENCE = r'&'

    # Comparison Operators
def t_EQUALEQUAL(t):
    r'=='
    return t

def t_NEQUAL(t):
    r'!='
    return t

def t_IDENTICAL(t):
    r'==='
    return t

t_GREATER = r'>'

def t_GEQUAL(t):
    r'>='
    return t

t_LESS = r'<'

def t_LEQUAL(t):
    r'<='
    return t

# Logical operators
def t_AND(t):
    r'and|&&'
    return t

def t_OR(t):
    r'or|\|\|'
    return t

def t_XOR(t):
    r'xor'
    return t

def t_NOT(t):
    r'!'
    return t

# String operators
t_CONCATSTR = r'\.'

#scope resolution operator
def t_DOUBLE_COLON(t):
    r'::'
    return t
# Identifiers, Numbers, etc

def t_SLABEL(t):
    r'<\?php'
    return t

def t_ELABEL(t):
    r'\?>'
    return t

def t_ID(t):
    r'\$\_?[0-9]*[a-zA-Z][a-zA-Z_0-9]*|\$\_?[0-9]*'
    return t

def t_STRING(t):

    r'[\"\'][a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\¡\xc2\xa1\/\\\#\¿\.*\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\:\; \t\n]*[\"\']'
    t.value = str(t.value)
    return t

def t_NFUNCTION(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_FLOAT(t):
    r'\-?[0-9]+\.[0-9]+([eE]\-?[0-9]+(.[0-9]+)?)?'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'0b[01]+|0[0-7]+|0[xX][0-9a-fA-F]+|\-?[1-9][0-9]*|0'
    return t

# Comments
def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

# Errors and tests
def t_error(t):
    #print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    return ("Lexical error: " + str(t.value[0]))


def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

def crear_archivo(nombre,datos):
    arch = open(nombre + '.txt', 'a')
    archivo.write(datos)
    archivo.close()

def cargar_arch():
    pruebas =  glob.glob("Pruebas/*.php")
    #print (pruebas)
    return pruebas

def tokenizar(pruebas):
    for v in pruebas:
        dir = 'resultados/' + v.replace('.php','.txt').replace('Pruebas/',"")
        if path.exists(dir):
            arch = open(dir, 'w')
        else:
            arch = open(dir, 'a')
        f = open(v,'r')
        data = f.read()
        lexer.input(data)
        for tok in lexer:
            arch.write(str(tok)+'\n')
        arch.close()

def tokenizar_argv(fin):
    f = open(fin, 'r')
    data = f.read()
    print (data)
    lexer.input(data)
    test(data, lexer)

lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
        tokenizar_argv(fin)
    else:
        pruebas = cargar_arch()
        tokenizar(pruebas)
