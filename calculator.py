from icecream import *
class Calculator:
    M_ERROR = "Error"

    def __init__(self):
        self._ans = None
        self._operations = ["+","-","*","/"]
    
    @property
    def ans(self):
        return self._ans

    @ans.setter
    def ans(self, new_ans):
        self._ans = new_ans

    @property
    def operations(self):
        return self._operations.copy()
    
    @operations.setter
    #prefiero no devolver la lista original.
    def operations(self, new_operations):
        self._operations = new_operations

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
        
    def solve(self, n1, n2, op):
        #este metodo se encarga de resolver la expresion, recibe 2 numeros y un string que determina el tipo de operacion
        ic(n1, n2,op)
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
            #raise ValueError("Error: a la funcion solve llego un valor no soportado en el parametro 'op'.\n"+op)
            return self.M_ERROR
        
        if isinstance(r, float) and self.has_no_decimal(r):
            return int(r)
        else:
            return r
        
    def has_no_decimal(self, number):
        return abs(number - int(number)) < 0.000001

    '''
    def split_expression(self, str):

    

        #este metodo se encarga de separar los numeros del signo de operacion en un string que recibe
        #y devuelve una lista con los numeros y el signo
        #solo quiero que entren 2 numeros y un signo, si la expresion tiene mas de 2 terminos en la operacion, quiero que salga error
        i = 0
        position = -1
        ops = self.operations

        if str == "":
            return [None, None, None]

        while position == -1 and i< len(ops):
                position = str.find(ops[i])
                i+=1

        if position != -1:
            op = str[position]

            #podria pasar que llegue "5+3-1". en ese caso, num2 daria error, y esta bien, porque solo quiero resolver
            #operaciones simples
            if not str[position+1:] == "":
                try:
                    num1 = float(str[:position])
                    num2 = float(str[position+1:])
                except ValueError as e:
                    print("Fallo el casteo de num1, num2 en split_expression()")
                    if "num1" in locals():
                        print("El casteo que fallo fue el de num2")
                    else:
                        print("El casteo que fallo fue el de num1")
                    print("ValueError: ", e)
                    return None
                
                return [num1, num2, op]
            else:
                #CODIGO REPETIDO ALERT!!!
                try:
                    return [float(str),None,None]
                except:
                    print("no se pudo castear a float str en la funcion split_expression()")
        else:
            #raise ValueError("No se pudo identificar la expresion matematica, o simplemente no llego una expresion matematica. \n" + "str: ",str)      
            try:
                return [float(str),None,None]
            except:
                print("no se pudo castear a float str en la funcion split_expression()")
    '''
    def split_expression(self, str, ops = 0):
        if ops == 0:
            ops = self.operations
        ic(ops)
        i = 0
        position = -1

        while position == -1 and i< len(ops):
                position = str.find(ops[i])
                i+=1

        if position != -1:
            op = str[position]
            #si
            try:
                num1 = float(str[:position])
            except:
                print("Error al intentar castear lo que se encontro antes de op a float en 'split_expression()'.")
                print("( num1 = float(str[:position]) )")
                return [None, None, None]
            
            try:
                if self.has_no_decimal(num1):
                    num1 = int(num1)
                num2 = float(str[position+1:])
            except:
                print("Error al intentar castear lo que se encontro despues de op a float en 'split_expression()'.")
                print("( num2 = float(str[position+1:]) )")
                return [num1, None, None]
            
            if self.has_no_decimal(num2):
                    num2 = int(num2)

            return [num1,num2,op]
        else:
            #no
            if str == "":
                return [None, None, None]
            else:
                try:
                    str = float(str)
                    if self.has_no_decimal(str):
                        str = int(str)
                    return [str, None, None]
                except:
                    print("Error al intentar castear str como un float (return [float(str), None, None] )")
                    print("str = ")
                    print(str)
                    return [None, None, None]