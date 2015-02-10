# ###module to generate mathematicla functions###

import math
from math import *
import random


operators = ["+", "-", "/", "*", "**"]


class SimpleFunction:
    def __init__(self, name, prefix="", *arguments):
        if "int" in str(type(arguments[0])):
            self.numArg = arguments[0]
            self.args = []
            for i in range(self.numArg):
                self.args.append("x" + str(int(i)))
        else:
            self.args = arguments
            self.numArg = len(arguments)
        self.prefix = prefix
        self.name = name

    def __str__(self):
        s = ""
        if self.numArg > 1:
            s = self.name + str(self.args)
            s = s.replace("[", "(")
            s = s.replace("]", ")")
            s = s.replace("'", "")

        else:
            s = self.name + "(" + self.args[0] + ")"
        if self.prefix == "":
            pass
        else:
            s = self.prefix + s
        return s

    def __repr__(self):
        return self.__str__()


class RandomFunction:
    def __init__(self, functionsList, operatorsList, seed, maxLenght=10, singleArgumentOnly=True, maxCoef=255,
                 variable="x"):
        self.operators = operatorsList
        self.functions = functionsList
        self.main = ""
        self.seed = seed
        self.main=self.generate(maxLenght)
        self.singleOnly = singleArgumentOnly
        self.maxCoeficient = 255
        self.variable ="x"
        for i in range(5):
            if random.choice((True,False,False)):
                print ("recursividad")
                self.main=self.main.replace("x",self.generate(4),1)

    def generate(self, maxLenght):
        if self.seed == 0:
            random.seed()
        else:
            random.seed(self.seed)
        lenght = random.randint(1, maxLenght)
        fs = []
        for i in range(lenght):  # ###escoger funciones
            t = random.choice(self.functions)
            while t.numArg > 1:
                t = random.choice(self.functions)
            fs.append(t)
        os = []
        for j in range(lenght - 1):  # ##escoger operaddores
            os.append(random.choice(self.operators))
        s = ["", ] * lenght
        primo = 1
        for k in range(lenght):  # ##combinar operadores y funciones de forma alternada
            if primo > 0:
                s[k] = fs.pop()
            else:
                s[k] = os.pop()
            primo *= -1
        if s[-1] in self.operators:
            s.pop()
        for h in range(len(s)):  # #rempalazar algunos con funciones más lineales
            if s[h] in self.functions:
                if random.choice((True, False, False)):
                    if random.choice((True, False, True)):
                        s[h] = "x"
                    else:
                        s[h] = str(random.randint(1, 255))
        for i in range(len(s)):  # #coeficientes
            if s[i] not in self.operators:
                cof = random.randint(1, 255)
                if cof != 1:
                    s[i] = "(" + str(cof) + "*" + str(s[i]) + ") "
        primo = 1

        ss = ""  # string form
        for i in s:
            if i in self.operators:
                ss += " " + str(i) + " "
            else:
                ss += str(i)
        ss = ss.replace("x0", "x")
        ###Deep1
        ssList = []
        for i in ss:  # ###string to list
            ssList.append(i)
        for i in range(len(ssList)):  # Rempalzar x porfunciones
            if ssList[i] == "x" and ssList[i - 1] == "(" and random.choice((True, False, False, False)):
                t = random.choice(self.functions)
                while t.numArg > 1:
                    t = random.choice(self.functions)
                ssList[i] = t

        ss = ""
        for i in ssList:  # ##Listo to str
            ss += str(i)
        ss = ss.replace("x0", "x")
        #self.main = ss
        return ss
    def noMath(self):
        self.main.replace("math","")

    def __str__(self):
        return self.main

    def __repr__(self):
        return self.__str__()

class DefaultRandomFunction(RandomFunction):
    def __init__(self):
        RandomFunction.__init__(self,listMathFunct, operators, 0)

def getArgs_builtin(obj):
    """ Describe a builtin function """

    # wi('+Built-in Function: %s' % obj.__name__)
    # Built-in functions cannot be inspected by
    # inspect.getargspec. We have to try and parse
    # the __doc__ attribute of the function.
    docstr = obj.__doc__
    args = ''

    if docstr:
        items = docstr.split('\n')
        if items:
            func_descr = items[0]
            s = func_descr.replace(obj.__name__, '')
            idx1 = s.find('(')
            idx2 = s.find(')', idx1)
            if idx1 != -1 and idx2 != -1 and (idx2 > idx1 + 1):
                args = s[idx1 + 1:idx2]
                # wi('\t-Method Arguments:', args)

    if args == '':
        pass
        # wi('\t-Method Arguments: None')
    return args


def listMathFunctions():
    functions = {}
    d = math.__dict__
    for i in d:
        if hasattr(d[i], "__call__") and "_" not in i:
            functions[i] = getArgs_builtin(d[i])
    return functions


def convertToNameNumArgs(d):
    c = {}
    for i in d:
        numCommas = d[i].count(",")
        c[i] = numCommas + 1
    return c


def convertNameNumArgsToFunction(d, prefix=True):
    l = []
    for i in d:
        if prefix:
            l.append(SimpleFunction(i, "math.", d[i]))
        else:
            l.append(SimpleFunction(i, "", d[i]))
    return l


listOfMathFunctions = listMathFunctions()
listOfMathFunctions.pop("fsum")
listOfMathFunctions.pop("isnan")
listOfMathFunctions.pop("modf")
listOfMathFunctionsConvertedToNameNumArgs = convertToNameNumArgs(listOfMathFunctions)
listMathFunct = convertNameNumArgsToFunction(listOfMathFunctionsConvertedToNameNumArgs,False)

if __name__ == "__main__":
    # print(listMathFunct)
    a = DefaultRandomFunction()
    x=1
    print(a)
    print(eval(a.main))

