class calculator:
    def __init__(self):
        self._ans = None
        self._num1 = None
        self._num2 = None
    
    @property
    def ans(self):
        return self._ans

    @ans.setter
    def ans(self, new_ans):
        self._ans = new_ans

    @property
    def num1(self):
        return self.num1

    @num1.setter
    def ans(self, new_num1):
        self._num1 = new_num1

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def ans(self, new_num2):
        self._num2 = new_num2

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
        if op == "+":
            return self._sum(n1, n2)
        elif op == "-":
            return self._subtract(n1, n2)
        elif op == "*":
            return self._multiply(n1, n2)
        elif op == "/":
            return self._divide(n1, n2)
        else:
            raise ValueError("Error: a la funcion solve llego un valor no soportado en el parametro 'op'")
    
    def split_expression(self, str):
        #hardcode, quitar URGENTE, operations deberia ser una variable de clase
        operations = ["+","-","*","/"]
        position = -1
        for operation in operations:
            position = str.find(operation)
        
        if position != -1:
            str_num1 = str[:position]
            str_num2 = str[position+1:]
            op = str[position]

            #podria pasar que llegue "5+3-1". en ese caso, num2 daria error, y esta bien, porque solo quiero resolver
            #operaciones simples

            try:
                num1 = int(str[:position])
                num2 = int(str[position+1:])
            except ValueError as e:
                print("Fallo el casteo de num1, num2 en interpret_operation()")
                if "num1" in locals():
                    print("El casteo que fallo fue el de num2")
                else:
                    print("El casteo que fallo fue el de num1")
                print("ValueError: ", e)
                return None
            
            return [num1, num2, op]
        else:
            raise ValueError("No se pudo identificar la expresion matematica, o simplemente no llego una expresion matematica. /n", "str: ",str)
            
