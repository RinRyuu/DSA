import ctypes

class listss:
    
    def __init__(self) -> None:
        self.size = 1
        self.n = 0
        
        self.A = self.__make_array(self.size)
        
    def __make_array(self,capcity):
        return (capcity*ctypes.py_object)()
    
    
L = listss()
print(L)