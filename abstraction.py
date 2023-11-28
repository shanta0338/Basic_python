from abc import ABC, abstractmethod
#above library should be use when we need abstraction class

class Shape(ABC):#abstract class
    """def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2"""
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):#inherite 
    #def __init__(self, dim1, dim2):
        #super().__init__(dim1, dim2)   
    def area(self,dim1, dim2):
        print(0.5 * dim1 * dim2)



s1 = Triangle()
s1.area(12,45)