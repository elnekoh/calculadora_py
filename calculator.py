from icecream import *
class Calculator:
    MESSAGE_ERROR: str = "Error"
    OPERATIONS: list = ["+","-","*","/"]

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
            return self.MESSAGE_ERROR
        
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
                return self.MESSAGE_ERROR
        else:
            return self.MESSAGE_ERROR
        
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

        #encontró coincidencia?
        if position != -1:
            text_before_match = text[:position]
            text_after_match = text[position+1:]
            operator = text[position]

            #aca el método controla si el primer valor es "-"
            if text_before_match == "":
                #antes del operador no hay nada
                if text_after_match == "":
                    print("Llego solo un operador a split_expression()")
                    return [None, None, None]
                elif text[position] == "-": #confirmamos si lo que esta en str[position] es "-"
                    #Si llega hasta aca, entonces la primer coincidencia era el símbolo negativo del primer numero
                    #entonces, se vuelve a splittear la expresión pero esta vez quitando el símbolo negativo.
                    splitted_text = self.split_expression(text_after_match)
                    try:
                        number1 = float(splitted_text[0])
                        #checkeamos si en realidad este numero no tiene decimales
                        if self.has_no_decimal(number1):
                            number1 = int(number1)
                        
                        #pasamos num1 a negativo, ya que previamente le quitamos el símbolo negativo.
                        return [number1*-1, splitted_text[1], splitted_text[2]]
                    except:
                        print("Fallo el casteo a float de split[0] en split_expression()")
                        print("return [number1*-1, splitted_text[1], splitted_text[2]]")
                        return [None, None, None] 
                else:
                    print("Llego un operador como primer char de txt a split_expression()")
                    return [None, None, None]
            else:
                #antes del operador hay algo
                try:
                    number1 = float(text_before_match)
                except:
                    print("Error al intentar castear lo que se encontró antes de operator a float en 'split_expression()'.")
                    print("( number1 = float(text_before_match) )")
                    return [None, None, None]
                
                try:
                    #si el float no tiene decimales, se pasa a int
                    if self.has_no_decimal(number1):
                        number1 = int(number1)
                    number2 = float(text_after_match)
                except:
                    #si no se puede pasar a float lo que hay después de la coincidencia, se devuelve solo el num1 y el operador
                    print("Error al intentar castear lo que se encontró después de operator a float en 'split_expression()'.")
                    print("( number2 = float(text_after_match) )")
                    return [number1, None, operator]
                
                if self.has_no_decimal(number2):
                        number2 = int(number2)

                return [number1,number2,operator]
        #a este punto, no se encontró ninguna coincidencia
        elif text == "": 
            return [None, None, None]
        else:
            try:
                #si se puede pasar a float, lo pasamos a int si no tiene decimales
                text = float(text)
                if self.has_no_decimal(text):
                    text = int(text)
                return [text, None, None]
            except:
                print("Error al intentar castear text como un float (return [text, None, None] )")
                print("text = ")
                print(text)
                return [None, None, None]