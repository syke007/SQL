# logic.py
from logic_grammar_ import LogicGrammar
from functios import LogicEval
from pprint import PrettyPrinter
import sys

pp = PrettyPrinter()
lg = LogicGrammar()
lg.build()

with open("file.txt", "r") as file:
    contents = file.read()
    try:
        ans = lg.parse(contents)
        pp.pprint(ans)
        for x in ans:
            answer = LogicEval.evaluate(x)
            if answer is not None:
                print(f"<< {answer}")
    except Exception as e:
        print(f'\033[91m-> {e}\033[0m')

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        content = file.read()

else:
    for expr in iter(lambda: input(">> "), ""):
        try:
            ans = lg.parse(expr)
            pp.pprint(ans) ## se quiser tirar arvore
            ans1 = LogicEval.evaluate(ans)
            if ans1 is not None:
                print(f"-{ans1}")
        except Exception as e:
            print(f'\033[91m-> {e}\033[0m')