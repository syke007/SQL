# logic_grammar.py
from logic_lexer import LogicLexer
import ply.yacc as pyacc

class LogicGrammar:
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.lexer = None

    def build(self, **kwargs):
        self.lexer = LogicLexer()
        self.lexer.build(**kwargs)
        self.tokens =self.lexer.tokens
        self.yacc =pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    def p_recur0(self, p):
          """ recur : S """
          p[0] = [p[1]]

    def p_recur1(self, p):
            """ recur : recur S """
            p[0] = [p[1]]
            p[0].append(p[2])

    def p_s(self,p):
        """ S : commands
              | proced
              | v
              | callf """
        p[0] = p[1]

    def p_var(self, p):
        """ v : var"""
        p[0] = p[1]

    def p_Com(self, p):
        """commands : LOAD table
                    | DISCARD table
                    | SHOW table
                    | SAVE table
                    | SELECT select
                    | CREATE table """
        p[0] = {"var": p[2], "arg": p[1]}

    def p_tab(self, p):
        """ table : TABLE var ';'
                  | TABLE var from
                  | TABLE var as """

        if len(p) == 4:
            p[0] = {"var": p[2], "arg": p[1], "Cont": p[3]}
        else:
            p[0] = p[1]

    def p_select(self, p):
        """select : '*' from
                  | v_list from """
        p[0] = {"var": p[1], "arg": p[2]}

    def p_VLIST0(self, p):
        """ v_list : var """
        p[0] = [p[1]]

    def p_VLIST1(self, p):
        """ v_list : v_list ',' var """
        p[0] = p[1]
        p[0].append(p[3])

    def p_as(self, p):
        """as : AS var ';' """
        p[0] = {"var": p[1], "arg": p[2], "Cont": p[1]}

    def p_from(self, p):
        """ from : FROM var ';'
                 | FROM var where
                 | FROM commands
                 | FROM var join
                 | FROM string ';'"""
        if len(p) == 3:
          p[0] = {"var": p[2], "arg": p[1]}
        else:
          p[0] = {"var": p[2], "arg": p[1], "cont": p[3]}

    def p_join(self, p):
        """join : JOIN var using"""
        p[0] = {"var": p[2], "arg": [p[1],p[3]]}

    def p_using(self, p):
        """using : USING '(' var '=' nr ')' ';'
                 | USING '(' var '=' string ')' ';'"""
        p[0] = {"var": [p[3],p[5]], "arg": p[1],"op": p[4], "": p[7]}

    def p_where(self, p):
        """where : WHERE operator """
        p[0] = {"var": p[1], "arg": p[2]}

    def p_operator0(self,p):
        """ operator : var '=' nr op
                     | var '=' string op
                     | var '<' '>' nr op
                     | var '<' '>' string op
                     | var '<' nr op
                     | var '>' nr op
                     | var '<' '=' nr op
                     | var '>' '=' nr op"""
        if len(p) == 5:
            p[0] = {"var": [p[1], p[3]], "op": p[2], 'arg': p[4]}
        elif len(p) == 6:
            p[0] = {"var": [p[1], p[4]], "op": [p[2],p[3]], 'arg' : p[5]}

    def p_operator1(self, p):
        """ op : ';'
               | AND operator
               | LIMIT nr ';' """
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = {"op": p[1], "arg": p[2]}
        elif len(p) == 4:
            p[0] = {"op": p[1], "arg": p[2], 'f': p[3]}

    def p_proced(self, p):
      """proced : PROCED var DO listt END"""
      p[0] = {"var": p[2], "list":p[4], 'arg': [p[1],p[3],p[3]]}

    def p_proced1(sel, p):
        """listt : commands"""
        p[0] = [p[1]]

    def p_proced2(sel, p):
        """listt : listt commands"""
        p[0] = p[1]
        p[0].append(p[2])

    def p_callf(self,p):
        """ callf : CALL var ';' """
        p[0] = {"arg": p[1], "var": p[2], "f": p[3]}

    def p_error(self, p):
     if p:
        raise Exception(f"Syntax Error: Unexpected'{p.type}'")
     else:
        raise Exception("Syntax Error: Unexpected end of the file.txt")















