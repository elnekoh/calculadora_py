from icecream import *
class Calculator:
    MESSAGE_ERROR = "Error"
    OPERATIONS = ["+","-","*","/"]

    def __init__(self):
        self._ans = None

    #Operaciones
    def _sum(self, number1: float | int, number2: float | int):
        return number1+number2

    def _subtract(self, number1: float | int, number2: float | int):
        return number1-number2

    def _multiply(self, number1: float | int, number2: float | int):
        return number1*number2

    def _divide(self, number1: float | int, number2: float | int):
        if number2!=0:
            return number1/number2
        else:
            print("no se puede dividir por cero!")
            return(None)
    
    #Resolver
    def solve(self, number1: float | int, number2: float | int, operator: str):
        """
        Método que resuelve una operación entre 2 números.
        operator: string --> posible valores "+", "-", "*", "/"
        """
        if number1 is None or number2 is None or operator is None:
            return self.M_ERROR
        
        result = 0
        if operator == "+":
            result = self._sum(number1, number2)
        elif operator == "-":
            result = self._subtract(number1, number2)
        elif operator == "*":
            result = self._multiply(number1, number2)
        elif operator == "/":
            result = self._divide(number1, number2)
            if result is None:
                return self.M_ERROR
        else:
            return self.M_ERROR
        
        if isinstance(result, float) and self.has_no_decimal(result):
            return int(result)
        else:
            return result
    
    def has_no_decimal(self, number: float): 
        """
        Este método tiene como fin, saber si un float no tiene decimales, para poder parsearlo a int
        sin perder sus decimales

        number --> float, int (idealmente float)
        """
        return abs(number - int(number)) < 0.000001

    def split_expression(self, text: str):
        """
        Este método recibe texto (string) y separa ese texto en 3 strings (guardados en una lista)
        el texto se divide si encuentra una coincidencia, el primer valor (num1) sera lo encontrado antes de
        la coincidencia, el segundo valor (num2) lo que se encuentre después de la coincidencia,
        y el ultimo (op), es la coincidencia.
        """
        operators = self.OPERATIONS
        i = 0
        position = -1

        #busca coincidencias
        while position == -1 and i< len(operators):
                position = text.find(operators[i])
                i+=1

        #encontro coincidencia?
        if position != -1:
            text_before_match = text[:position]
            text_after_match = text[position+1:]
            operator = text[position]
            #aca el metodo controla si el primer valor es "-"
            if text_before_match == "":
                if text_after_match == "":
                    print("Llego solo un operador a split_expression()")
                    return [None, None, None]
                else:
                    if text[position] == "-": #confirmamos si lo que esta en str[position] es "-"
                        #Si llega hasta aca, entonces la primer coincidencia era el simbolo negativo del primer numero
                        #entonces, se vuelve a splitear la expresion pero esta vez quitando el simbolo negativo.
                        splitted_text = self.split_expression(text_after_match)
                        try:
                            number1 = float(splitted_text[0])
                            #checkeamos si en realidad este numero no tiene decimales
                            if self.has_no_decimal(number1):
                                number1 = int(number1)
                            
                            #pasamos num1 a negativo, ya que previamente le quitamos el simbolo negativo.
                            return [number1*-1, splitted_text[1], splitted_text[2]]
                        except:
                            print("Fallo el casteo a float de split[0] en split_expression()")
                            print("return [float('-'+split[0]), split[1], split[2]]")
                            return [None, None, None] 
                    else:
                        print("Llego un operador como primer char de txt a split_expression()")
                        return [None, None, None]
            else:   #Si no esta vacio lo encontrado antes de la coincidencia: 
                try:
                    number1 = float(text_before_match)
                except:
                    #si no podemos pasarlo a float, devolvemos none en todo, siempre que hay error se devuelve none en todo
                    print("Error al intentar castear lo que se encontro antes de op a float en 'split_expression()'.")
                    print("( num1 = float(str[:position]) )")
                    return [None, None, None]
                
                try:
                    #si el float no tiene decimales, se pasa a int
                    if self.has_no_decimal(number1):
                        number1 = int(number1)
                    number2 = float(text_after_match)
                except:
                    #si no se puede pasar a float lo que hay despues de la coincidencia, se devuelve solo el num1 y el operador
                    print("Error al intentar castear lo que se encontro despues de op a float en 'split_expression()'.")
                    print("( num2 = float(str[position+1:]) )")
                    return [number1, None, operator]
                
                if self.has_no_decimal(number2):
                        number2 = int(number2)

                return [number1,number2,operator]
        else:
            #no encontro coincidencia:
            #esta vacio el stream?. si da true, entonces llego vacio, si da false, entonces solo llego un numero
            if text == "":
                return [None, None, None]
            else:
                try:
                    #si se puede pasar a float, lo pasamos a int si no tiene decimales
                    text = float(text)
                    if self.has_no_decimal(text):
                        text = int(text)
                    return [text, None, None]
                except:
                    print("Error al intentar castear str como un float (return [float(str), None, None] )")
                    print("str = ")
                    print(text)
                    return [None, None, None]