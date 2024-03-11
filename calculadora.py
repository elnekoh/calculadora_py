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

    def sumar(self, n1, n2):
        return n1+n2

    def subtract(self, n1, n2):
        return n1-n2

    def multiply(self, n1, n2):
        return n1*n2

    def divide(self, n1, n2):
        if n2!=0:
            return n1/n2
        else:
            print("no se puede dividir por cero!")
            return(None)
