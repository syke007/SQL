#logic_eval
import pandas as panda

class LogicEval:
    symbols = {}
    data = {}

    # Design Pattern: Dispatch Table
    operators = {
        'LOAD':lambda arg: LogicEval.loadfunction(arg),
        'SHOW':lambda arg: LogicEval.showfunction(arg),


    }
    @staticmethod
    def evaluate(arg):
        if type(arg) is list:
            ans = None
            for a in arg:
                ans = LogicEval.evaluate(a)
                return ans

        if arg['arg'] in LogicEval.operators:
            f = LogicEval.operators[arg['arg']]
            return f(arg)

    def loadfunction(arg):
        nameTable = arg['var']['var']
        nameFile = arg['var']['Cont']['var']['str']
        print(nameFile)

        if nameTable not in LogicEval.data:
            LogicEval.data[nameTable] = panda.read_csv(nameFile)
            modify(nameTable)
        else:
            print("Tabela ja existe")

    def showfunction(arg):
        nameTable = arg['var']['var']
        if nameTable not in LogicEval.data:
            print("Tabela nao existe")
        else:
            print(LogicEval.data[nameTable])


def modify(nameTable):
    for x in LogicEval.data[nameTable]:
        for i in LogicEval.data[nameTable][x]:
            check = isinstance(i, float)
            if check == True:
                i = float(i)


