#__all__ = ["RegularParser"]

class ParserBase:
    def __init__(self,instructionone):
        self.instructionone = instructionone
        self.data = instructionone
    def getdata(self):
        return self.data


class RegularParser(ParserBase):
    def __init__(self, instruction1, instruction2):
        ParserBase.__init__(instruction1)
        self.insruction2=instruction2


class SpecialParserParser(ParserBase):
    def __init__(self, instruction1,instruction2,instruction3):
        ParserBase.__init__(self, instruction1)
        self.instruction2 = instruction2
        self.instruction3 = instruction3