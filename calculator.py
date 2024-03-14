class Calculator:
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
        if op == "+":
            return self._sum(n1, n2)
        elif op == "-":
            return self._subtract(n1, n2)
        elif op == "*":
            return self._multiply(n1, n2)
        elif op == "/":
            return self._divide(n1, n2)
        else:
            raise ValueError("Error: a la funcion solve llego un valor no soportado en el parametro 'op'.\n"+op)
    
    def split_expression(self, str):
        #este metodo se encarga de separar los numeros del signo de operacion en un string que recibe
        #y devuelve una lista con los numeros y el signo
        #solo quiero que entren 2 numeros y un signo, si la expresion tiene mas de 2 terminos en la operacion, quiero que salga error
        i = 0
        position = -1
        ops = self.operations

        while position == -1 and i< len(ops):
                position = str.find(ops[i])
                i+=1
        if position != -1:
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
            raise ValueError("No se pudo identificar la expresion matematica, o simplemente no llego una expresion matematica. \n" + "str: ",str)      