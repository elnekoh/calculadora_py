from icecream import *
class Calculator:
    M_ERROR = "Error"
    OPERATIONS = ["+","-","*","/"]

    def __init__(self):
        self._ans = None
    
    @property
    def ans(self):
        return self._ans

    @ans.setter
    def ans(self, new_ans):
        self._ans = new_ans

    #Operaciones
    def _sum(self, n1, n2):
        return n1+n2

    def _subtract(self, n1, n2):
        return n1-n2

    def _multiply(self, n1, n2):
        return n1*n2

    def _divide(self, n1, n2):
        if n2!=0:
            return n1/n2
        else:
            print("no se puede dividir por cero!")
            return(None)
    
    #Resolver
    def solve(self, n1, n2, op: str):
        """
        Metodo que resuelve una operacion entre 2 numeros.
        n1 y n2: int o float
        op: string --> posible valores "+", "-", "*", "/"
        """
        #si llega none en alguno de los parametros, error
        if n1 is None or n2 is None or op is None:
            return self.M_ERROR
        
        r = 0
        if op == "+":
            r = self._sum(n1, n2)
        elif op == "-":
            r = self._subtract(n1, n2)
        elif op == "*":
            r = self._multiply(n1, n2)
        elif op == "/":
            r = self._divide(n1, n2)
            if r is None:
                return self.M_ERROR
        else:
            return self.M_ERROR
        
        if isinstance(r, float) and self.has_no_decimal(r):
            return int(r)
        else:
            return r
    
    def has_no_decimal(self, number):
        """
        Este metodo tiene como fin, saber si un float no tiene decimales, para poder parsearlo a int
        sin perder sus decimales

        number --> float, int (idealmente float)
        """
        return abs(number - int(number)) < 0.000001

    def split_expression(self, str: str):
        """
        Este metodo recibe texto (string) y separa ese texto en 3 strings (guardados en una lista)
        el texto se divide si encuentra una coincidencia, el primer valor (num1) sera lo encontrado antes de
        la coincidencia, el segundo valor (num2) lo que se encuentre despues de la coincidencia,
        y el ultimo (op), es la coincidencia.
        """
        ops = self.OPERATIONS
        i = 0
        position = -1

        #busca coincidencias
        while position == -1 and i< len(ops):
                position = str.find(ops[i])
                i+=1

        #encontro coincidencia?
        if position != -1:
            
            op = str[position]
            
            #aca el metodo controla si el primer valor es "-"
            if str[:position] == "": #Si lo que esta antes de la coincidencia esta vacio
                if str[position+1:] == "":
                    print("Llego solo un operador a split_expression()")
                    return [None, None, None]
                else:
                    if str[position] == "-": #confirmamos si lo que esta en str[position] es "-"
                        #Si llega hasta aca, entonces la primer coincidencia era el simbolo negativo del primer numero
                        #entonces, se vuelve a splitear la expresion pero esta vez quitando el simbolo negativo.
                        split = self.split_expression(str[position+1:])
                        try:
                            num1 = float(split[0])
                            #checkeamos si en realidad este numero no tiene decimales
                            if self.has_no_decimal(num1):
                                num1 = int(num1)
                            
                            #pasamos num1 a negativo, ya que previamente le quitamos el simbolo negativo.
                            return [num1*-1, split[1], split[2]]
                        except:
                            print("Fallo el casteo a float de split[0] en split_expression()")
                            print("return [float('-'+split[0]), split[1], split[2]]")
                            return [None, None, None] 
                    else:
                        print("Llego un operador como primer char de txt a split_expression()")
                        return [None, None, None]
            else:   #Si no esta vacio lo encontrado antes de la coincidencia: 
                try:
                    num1 = float(str[:position])
                except:
                    #si no podemos pasarlo a float, devolvemos none en todo, siempre que hay error se devuelve none en todo
                    print("Error al intentar castear lo que se encontro antes de op a float en 'split_expression()'.")
                    print("( num1 = float(str[:position]) )")
                    return [None, None, None]
                
                try:
                    #si el float no tiene decimales, se pasa a int
                    if self.has_no_decimal(num1):
                        num1 = int(num1)
                    num2 = float(str[position+1:])
                except:
                    #si no se puede pasar a float lo que hay despues de la coincidencia, se devuelve solo el num1 y el operador
                    print("Error al intentar castear lo que se encontro despues de op a float en 'split_expression()'.")
                    print("( num2 = float(str[position+1:]) )")
                    return [num1, None, op]
                
                if self.has_no_decimal(num2):
                        num2 = int(num2)

                return [num1,num2,op]
        else:
            #no encontro coincidencia:
            #esta vacio el stream?. si da true, entonces llego vacio, si da false, entonces solo llego un numero
            if str == "":
                return [None, None, None]
            else:
                try:
                    #si se puede pasar a float, lo pasamos a int si no tiene decimales
                    str = float(str)
                    if self.has_no_decimal(str):
                        str = int(str)
                    return [str, None, None]
                except:
                    print("Error al intentar castear str como un float (return [float(str), None, None] )")
                    print("str = ")
                    print(str)
                    return [None, None, None]