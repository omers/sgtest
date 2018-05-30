__all__ = ["JustDoIt"]

def JustDoIt(x,y):
    return  x+y

def __JustDoIt2(x,y):
    return  x+y

class UiDTO:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.PostitionId = "0xsgerc"
        self.Amount = "222"
        self.UserId = "24cv356f"
        self.UserName ="Avi"


    def __ThisShouldntBeExposed(self, name, age):
        self.sdfg = 45

    def ThisShouldBeExposed(self, name, age):
        self.sdfg = 45


class SecondUiDTO:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __ThisShouldntBeExposed(self, name, age):
        self.sdfg = 45

    def ThisShouldBeExposed(self, name, age):
        self.sdfg = 45



class _AnotherUiDTO:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __ThisShouldntBeExposed(self, name, age):
        self.sdfg = 45

    def ThisShouldBeExposed(self, name, age):
        self.sdfg = 45

