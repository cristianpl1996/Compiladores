import ply.yacc as yacc
from miniphp_lexer import tokens
import miniphp_lexer
import sys

VERBOSE = 1

val=False

def p_inicio(p):
    '''program : SLABEL import declaracion_sentencias ELABEL
                | SLABEL import ELABEL
                | SLABEL declaracion_sentencias ELABEL'''
    pass


def p_declaracion_sentencias(p):
    '''declaracion_sentencias : sentencias declaracion_sentencias
                                | sentencias'''
    pass


def p_sentencias(p):
    '''sentencias : sentassign
                    | call_function SEMICOLON
                    | sentif
                    | sentecho
                    | sentfunc
                    | sentreturn
                    | sentfor
                    | sentwhile
                    | sentdowhile
                    | sentforeach
                    | sentswitch
                    | sentconst
                    | sentclass
                    | met_clases
                    | var_declaration
                    | sentinterface
                    |
                    '''
    pass

#Declaracion de variables
def p_vardeclaration(p):
    ''' var_declaration : ID SEMICOLON var_declaration
                        | ID SEMICOLON
                        | ID EQUAL INTEGER SEMICOLON var_declaration
                        | ID EQUAL INTEGER SEMICOLON
                        | ID EQUAL FLOAT SEMICOLON var_declaration
                        | ID EQUAL FLOAT SEMICOLON
                        | ID EQUAL STRING SEMICOLON var_declaration
                        | ID EQUAL STRING SEMICOLON
                        | ID EQUAL bool SEMICOLON var_declaration
                        | ID EQUAL bool SEMICOLON
                        | ID EQUAL ID SEMICOLON var_declaration
                        | ID EQUAL ID SEMICOLON
                        | ID EQUAL exp SEMICOLON var_declaration
                        | ID EQUAL exp SEMICOLON
                        | ID EQUAL NEW call_function SEMICOLON var_declaration
                        | ID EQUAL NEW call_function SEMICOLON
                        | ID EQUAL declaracion_array  var_declaration
                        | ID EQUAL declaracion_array
                        | REFERENCE ID SEMICOLON var_declaration
                        | REFERENCE ID SEMICOLON
                        | ID EQUAL call_function SEMICOLON var_declaration
                        | ID EQUAL call_function SEMICOLON
                        | met_clases
	'''
    pass


#---------------------------CLASES--------------------

#Sentencia CLASES
def p_sentclass(p):
    ''' sentclass : CLASS NFUNCTION cuerpoclase
                    | CLASS NFUNCTION EXTENDS NFUNCTION cuerpoclase
                    | CLASS NFUNCTION IMPLEMENTS NFUNCTION cuerpoclase
    '''
    pass

def p_sentinterface(p):
    ''' sentinterface : INTERFACE NFUNCTION LKEY cuerpo_interface RKEY
    '''
    pass

def p_cuerpo_interface(p):
    ''' cuerpo_interface : scopes FUNCTION NFUNCTION LPARENTHESIS arg RPARENTHESIS SEMICOLON cuerpo_interface
                            | scopes FUNCTION NFUNCTION LPARENTHESIS arg RPARENTHESIS SEMICOLON
    '''
    pass

def p_cuerpoclase(p):
    ''' cuerpoclase :  LKEY listaatributos listametodos RKEY
                        | LKEY listaatributos RKEY
                        | LKEY listametodos RKEY
    '''
    pass

def p_listaatributos(p):
    ''' listaatributos : listaatributos scopes var_declaration
                        | scopes var_declaration
                        | scopes STATIC var_declaration'''
    pass

def p_listametodos(p):
    ''' listametodos : listametodos scopes sentfunc
                    | scopes sentfunc
                    | listametodos sentfunc
                    | sentfunc
                    | listametodos scopes STATIC sentfunc
                    | scopes STATIC sentfunc
                    '''
    pass

def p_scopes(p):
    ''' scopes : PUBLIC
                | PRIVATE
                | PROTECTED
    '''
    pass

def p_met_clases(p):
    ''' met_clases : ISSET LPARENTHESIS ID RPARENTHESIS
                    | GET_CLASS LPARENTHESIS ID RPARENTHESIS SEMICOLON
                    | NFUNCTION DOUBLE_COLON call_function SEMICOLON
                    | ID DOUBLE_COLON call_function SEMICOLON
                    | CONST STRING EQUAL typevar SEMICOLON
                    | ID EQUAL NEW call_function SEMICOLON
                    | ID CMETHOD call_function SEMICOLON
                    | ID CMETHOD NFUNCTION
                    | ID CMETHOD PUBLIC SEMICOLON
                    | ID CMETHOD PROTECTED SEMICOLON
                    | ID CMETHOD PRIVATE SEMICOLON
                    | FUNCTION CONSTRUCTOR LPARENTHESIS argfunc RPARENTHESIS LKEY declaracion_sentencias RKEY
                    | FUNCTION DESTRUCTOR LPARENTHESIS argfunc RPARENTHESIS LKEY declaracion_sentencias RKEY
                    | FUNCTION NFUNCTION LPARENTHESIS argfunc RPARENTHESIS LKEY declaracion_sentencias RKEY
                    |
    '''


#sentencia de constante

def p_declaracion_constante(p):
    ''' sentconst : DEFINE LPARENTHESIS STRING COMMA declaracion_array RPARENTHESIS SEMICOLON
                    | DEFINE LPARENTHESIS STRING COMMA typevar RPARENTHESIS SEMICOLON'''
    pass
#sentendia ARRAY

def p_declaracion_array(p):
    ''' declaracion_array : ARRAY LPARENTHESIS cuerpo_array RPARENTHESIS SEMICOLON
                            |  ARRAY LPARENTHESIS cuerpo_array RPARENTHESIS
    '''
    pass

def p_cuerpoarray(p):
    ''' cuerpo_array : typevar COMMA cuerpo_array
                    | typevar EQUALG typevar COMMA cuerpo_array
                    | typevar
                    | typevar EQUALG typevar
                    | empty
    '''
    pass

#sentencia return
def p_sentreturn(p):
    '''sentreturn : RETURN type SEMICOLON
                    | RETURN cond SEMICOLON
                    | RETURN var_declaration
                    | RETURN expsimple SEMICOLON
                    | RETURN SEMICOLON'''

# sentencia para imprimir
def p_sentecho(p):
    '''sentecho : ECHO typevar SEMICOLON
                | ECHO exp SEMICOLON
                | ECHO cond SEMICOLON
                | ECHO met_clases '''
    pass

# para el if, else if, else
def p_sentif(p):
    '''sentif : IF genif auxsentif'''
    pass

def p_auxsentif(p):
    '''auxsentif : ELSE IF genif auxsentif
                    | ELSE LKEY declaracion_sentencias RKEY
                    | empty'''
    pass

def p_generatorif(p):
    '''genif : LPARENTHESIS cond RPARENTHESIS LKEY declaracion_sentencias RKEY
                | LPARENTHESIS met_clases RPARENTHESIS LKEY declaracion_sentencias RKEY
    '''
    pass
#asignaciones
def p_sentassign(p):
    '''sentassign :  ID EQUAL exp SEMICOLON
                    | ID PLUS PLUS SEMICOLON
                    | ID EQUAL declaracion_array
                    | ID MINUS MINUS SEMICOLON
                    '''
    pass


#expresiones logicas


def p_booleanos(p):
    '''bool : TRUE
            | FALSE '''
    pass

def p_operadoreslogicos(p):
    '''oplogicos : AND
                    | OR
                    | XOR
                    | NOT '''
    pass



#expresiones de comparacion

def p_exp(p):
    '''exp : expsimple  opcomparacion  expsimple
            | LPARENTHESIS expsimple  opcomparacion  expsimple RPARENTHESIS
            | expsimple'''
    pass


def p_opcomparacion(p):
    '''opcomparacion : EQUALEQUAL
                        | NEQUAL
                        | IDENTICAL
                        | GREATER
                        | GEQUAL
                        | LESS
                        | LEQUAL'''



#expresiones matematicas
def p_expression_simple(p):
    '''expsimple :  expsimple  opsuma term
                | term'''
    pass

def p_term(p):
    '''term : term opmult factor
            | factor'''
    pass

def p_factor(p):
    '''factor : INTEGER
                | FLOAT
                | ID
                | call_function
                | LPARENTHESIS expsimple RPARENTHESIS'''
    pass

def p_typevar(p):
    '''typevar : STRING
                | INTEGER
                | TRUE
                | FALSE
                | FLOAT
    '''
    pass

def p_opsuma(p):
    '''opsuma : PLUS
                | MINUS '''
    pass

def p_opmult(p):
    '''opmult : TIMES
                | DIV
                | MODULE
                | EXPONENTIATION '''
    pass

def p_cond(p):
    '''cond : type
            | cond opcomparacion cond
            | cond oplogicos cond
            | LPARENTHESIS type RPARENTHESIS
            | LPARENTHESIS cond RPARENTHESIS'''
    pass


def p_type(p):
	'''type : typevar
				| var_declaration_gen'''
	pass

def p_var_declaration_gen(p):
	'''var_declaration_gen : ID
    						| ID PLUS PLUS
                            | ID MINUS MINUS
    						| MINUS MINUS  ID
                            | PLUS PLUS ID
    						| typevar
                            '''
	pass

def p_arg(p):
	'''arg : var_declaration_gen
			| type
			| type COMMA arg
			| STRING
			| var_declaration_gen COMMA arg
			| STRING COMMA arg
            |'''
	pass

def p_arg2(p):
	'''argfunc : ID
			| ID COMMA argfunc
            |'''
	pass

#referente a funciones
#declara funcionees
def p_sentfunc(p):
    '''sentfunc : FUNCTION NFUNCTION LPARENTHESIS argfunc RPARENTHESIS LKEY declaracion_sentencias RKEY
                | met_clases'''
    pass

# para el llamado de las funciones
def p_call_function(p):
	'''call_function : NFUNCTION
						| NFUNCTION LPARENTHESIS arg RPARENTHESIS
                        | ID LPARENTHESIS arg RPARENTHESIS'''
	pass

#secuencias de los ciclos
def p_sentfor(p):
    '''sentfor : FOR LPARENTHESIS ID EQUAL expsimple SEMICOLON cond SEMICOLON expsimple  RPARENTHESIS LKEY  declaracion_sentencias RKEY
                | FOR LPARENTHESIS ID EQUAL expsimple SEMICOLON cond SEMICOLON ID PLUS PLUS  RPARENTHESIS LKEY  declaracion_sentencias RKEY
                | FOR LPARENTHESIS ID EQUAL expsimple SEMICOLON cond SEMICOLON ID MINUS MINUS  RPARENTHESIS LKEY  declaracion_sentencias RKEY'''
    pass


def p_sentwhile(p):
    '''sentwhile : WHILE LPARENTHESIS cond RPARENTHESIS LKEY declaracion_sentencias RKEY '''
    pass

def p_sentdowhile(p):
    '''sentdowhile : DO LKEY  declaracion_sentencias RKEY WHILE LPARENTHESIS cond RPARENTHESIS SEMICOLON'''
    pass

def p_sentforeach(p):
	'''sentforeach : FOREACH LPARENTHESIS ID AS ID RPARENTHESIS LKEY declaracion_sentencias RKEY
                	| FOREACH LPARENTHESIS ID AS ID EQUALG ID RPARENTHESIS LKEY declaracion_sentencias RKEY
                	| FOREACH LPARENTHESIS declaracion_array AS ID RPARENTHESIS LKEY declaracion_sentencias RKEY
                    | FOREACH LPARENTHESIS met_clases AS ID EQUALG ID RPARENTHESIS LKEY declaracion_sentencias RKEY
	'''
	pass

def p_sentswitch(p):
	'''sentswitch : SWITCH LPARENTHESIS ID RPARENTHESIS LKEY cuerpo_switch RKEY'''
	pass

def p_cuerpo_switch(p):
	'''cuerpo_switch : CASE cuerpo_case cuerpo_switch
                    	| CASE  cuerpo_case
                        | DEFAULT TWOPOINTS declaracion_sentencias BREAK SEMICOLON
	'''
	pass

def p_cuerpo_case(p):
	'''cuerpo_case : INTEGER TWOPOINTS declaracion_sentencias BREAK SEMICOLON'''


#importaciones dentro de php
def p_import(p):
    '''import : INCLUDE STRING SEMICOLON'''
    pass

def p_empty(p):
    'empty : '
    pass

# Error rule for syntax errors
def p_error(p):
    if VERBOSE:
        if p is not None:
            print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
        else:
            print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
    else:
        raise Exception('syntax', 'error')

# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'Pruebas/prueba22_poo.php'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	if not val :
		print("Tu parser reconocio correctamente todo")
	#input()
