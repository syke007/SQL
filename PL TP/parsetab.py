
# parsetab.py
# This file.txt is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND AS CALL CREATE DISCARD DO END FROM JOIN LIMIT LOAD PROCED SAVE SELECT SHOW TABLE USING WHERE nr str string var recur : S  recur : recur S  S : commands\n              | proced\n              | v\n              | callf  v : varcommands : LOAD table\n                    | DISCARD table\n                    | SHOW table\n                    | SAVE table\n                    | SELECT select\n                    | CREATE table  table : TABLE var ';'\n                  | TABLE var from\n                  | TABLE var as select : '*' from\n                  | v_list from  v_list : var  v_list : v_list ',' var as : AS var ';'  from : FROM var ';'\n                 | FROM var where\n                 | FROM commands\n                 | FROM var join\n                 | FROM string ';'join : JOIN var usingusing : USING '(' var '=' nr ')' ';'\n                 | USING '(' var '=' string ')' ';'where : WHERE operator  operator : var '=' nr op\n                     | var '=' string op\n                     | var '<' '>' nr op\n                     | var '<' '>' string op\n                     | var '<' nr op\n                     | var '>' nr op\n                     | var '<' '=' nr op\n                     | var '>' '=' nr op op : ';'\n               | AND operator\n               | LIMIT nr ';' proced : PROCED var DO listt ENDlistt : commandslistt : listt commands callf : CALL var ';' "
    
_lr_action_items = {'LOAD':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,52,53,54,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[7,7,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,7,-18,7,-45,-14,-15,-16,-24,7,-43,-22,-23,-25,-26,-42,-44,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'DISCARD':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,52,53,54,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[8,8,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,8,-18,8,-45,-14,-15,-16,-24,8,-43,-22,-23,-25,-26,-42,-44,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'SHOW':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,52,53,54,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[9,9,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,9,-18,9,-45,-14,-15,-16,-24,9,-43,-22,-23,-25,-26,-42,-44,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'SAVE':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,52,53,54,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[10,10,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,10,-18,10,-45,-14,-15,-16,-24,10,-43,-22,-23,-25,-26,-42,-44,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'SELECT':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,52,53,54,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[11,11,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,11,-18,11,-45,-14,-15,-16,-24,11,-43,-22,-23,-25,-26,-42,-44,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'CREATE':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,52,53,54,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[12,12,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,12,-18,12,-45,-14,-15,-16,-24,12,-43,-22,-23,-25,-26,-42,-44,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'PROCED':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,32,35,36,37,38,41,47,48,49,52,53,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[13,13,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,-18,-45,-14,-15,-16,-24,-22,-23,-25,-26,-42,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'var':([0,1,2,3,4,5,6,11,13,14,15,16,17,18,19,20,21,22,26,30,31,32,33,35,36,37,38,39,41,47,48,49,50,51,52,53,55,56,62,71,72,73,74,76,79,81,84,86,87,88,89,91,96,97,],[14,14,-1,-3,-4,-5,-6,25,27,-7,28,-2,-8,29,-9,-10,-11,-12,-13,-17,40,-18,43,-45,-14,-15,-16,46,-24,-22,-23,-25,57,58,-26,-42,-21,-30,-27,83,-31,-39,57,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'CALL':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,32,35,36,37,38,41,47,48,49,52,53,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[15,15,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,-18,-45,-14,-15,-16,-24,-22,-23,-25,-26,-42,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'$end':([1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,32,35,36,37,38,41,47,48,49,52,53,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[0,-1,-3,-4,-5,-6,-7,-2,-8,-9,-10,-11,-12,-13,-17,-18,-45,-14,-15,-16,-24,-22,-23,-25,-26,-42,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'TABLE':([7,8,9,10,12,],[18,18,18,18,18,]),'*':([11,],[23,]),'END':([17,19,20,21,22,26,30,32,36,37,38,41,44,45,47,48,49,52,54,55,56,62,72,73,76,79,81,84,86,87,88,89,91,96,97,],[-8,-9,-10,-11,-12,-13,-17,-18,-14,-15,-16,-24,53,-43,-22,-23,-25,-26,-44,-21,-30,-27,-31,-39,-32,-35,-36,-40,-33,-34,-37,-38,-41,-28,-29,]),'FROM':([23,24,25,29,43,],[31,31,-19,31,-20,]),',':([24,25,43,],[33,-19,-20,]),'DO':([27,],[34,]),';':([28,29,40,42,46,64,65,67,69,77,78,80,82,85,94,95,],[35,36,47,52,55,73,73,73,73,73,73,73,73,91,96,97,]),'AS':([29,],[39,]),'string':([31,59,66,90,],[42,65,78,93,]),'WHERE':([40,],[50,]),'JOIN':([40,],[51,]),'=':([57,60,61,83,],[59,68,70,90,]),'<':([57,],[60,]),'>':([57,60,],[61,66,]),'USING':([58,],[63,]),'nr':([59,60,61,66,68,70,75,90,],[64,67,69,77,80,82,85,92,]),'(':([63,],[71,]),'AND':([64,65,67,69,77,78,80,82,],[74,74,74,74,74,74,74,74,]),'LIMIT':([64,65,67,69,77,78,80,82,],[75,75,75,75,75,75,75,75,]),')':([92,93,],[94,95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'recur':([0,],[1,]),'S':([0,1,],[2,16,]),'commands':([0,1,31,34,44,],[3,3,41,45,54,]),'proced':([0,1,],[4,4,]),'v':([0,1,],[5,5,]),'callf':([0,1,],[6,6,]),'table':([7,8,9,10,12,],[17,19,20,21,26,]),'select':([11,],[22,]),'v_list':([11,],[24,]),'from':([23,24,29,],[30,32,37,]),'as':([29,],[38,]),'listt':([34,],[44,]),'where':([40,],[48,]),'join':([40,],[49,]),'operator':([50,74,],[56,84,]),'using':([58,],[62,]),'op':([64,65,67,69,77,78,80,82,],[72,76,79,81,86,87,88,89,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> recur","S'",1,None,None,None),
  ('recur -> S','recur',1,'p_recur0','logic_grammar_.py',22),
  ('recur -> recur S','recur',2,'p_recur1','logic_grammar_.py',26),
  ('S -> commands','S',1,'p_s','logic_grammar_.py',31),
  ('S -> proced','S',1,'p_s','logic_grammar_.py',32),
  ('S -> v','S',1,'p_s','logic_grammar_.py',33),
  ('S -> callf','S',1,'p_s','logic_grammar_.py',34),
  ('v -> var','v',1,'p_var','logic_grammar_.py',38),
  ('commands -> LOAD table','commands',2,'p_Com','logic_grammar_.py',42),
  ('commands -> DISCARD table','commands',2,'p_Com','logic_grammar_.py',43),
  ('commands -> SHOW table','commands',2,'p_Com','logic_grammar_.py',44),
  ('commands -> SAVE table','commands',2,'p_Com','logic_grammar_.py',45),
  ('commands -> SELECT select','commands',2,'p_Com','logic_grammar_.py',46),
  ('commands -> CREATE table','commands',2,'p_Com','logic_grammar_.py',47),
  ('table -> TABLE var ;','table',3,'p_tab','logic_grammar_.py',51),
  ('table -> TABLE var from','table',3,'p_tab','logic_grammar_.py',52),
  ('table -> TABLE var as','table',3,'p_tab','logic_grammar_.py',53),
  ('select -> * from','select',2,'p_select','logic_grammar_.py',61),
  ('select -> v_list from','select',2,'p_select','logic_grammar_.py',62),
  ('v_list -> var','v_list',1,'p_VLIST0','logic_grammar_.py',66),
  ('v_list -> v_list , var','v_list',3,'p_VLIST1','logic_grammar_.py',70),
  ('as -> AS var ;','as',3,'p_as','logic_grammar_.py',75),
  ('from -> FROM var ;','from',3,'p_from','logic_grammar_.py',79),
  ('from -> FROM var where','from',3,'p_from','logic_grammar_.py',80),
  ('from -> FROM commands','from',2,'p_from','logic_grammar_.py',81),
  ('from -> FROM var join','from',3,'p_from','logic_grammar_.py',82),
  ('from -> FROM string ;','from',3,'p_from','logic_grammar_.py',83),
  ('join -> JOIN var using','join',3,'p_join','logic_grammar_.py',90),
  ('using -> USING ( var = nr ) ;','using',7,'p_using','logic_grammar_.py',94),
  ('using -> USING ( var = string ) ;','using',7,'p_using','logic_grammar_.py',95),
  ('where -> WHERE operator','where',2,'p_where','logic_grammar_.py',99),
  ('operator -> var = nr op','operator',4,'p_operator0','logic_grammar_.py',103),
  ('operator -> var = string op','operator',4,'p_operator0','logic_grammar_.py',104),
  ('operator -> var < > nr op','operator',5,'p_operator0','logic_grammar_.py',105),
  ('operator -> var < > string op','operator',5,'p_operator0','logic_grammar_.py',106),
  ('operator -> var < nr op','operator',4,'p_operator0','logic_grammar_.py',107),
  ('operator -> var > nr op','operator',4,'p_operator0','logic_grammar_.py',108),
  ('operator -> var < = nr op','operator',5,'p_operator0','logic_grammar_.py',109),
  ('operator -> var > = nr op','operator',5,'p_operator0','logic_grammar_.py',110),
  ('op -> ;','op',1,'p_operator1','logic_grammar_.py',117),
  ('op -> AND operator','op',2,'p_operator1','logic_grammar_.py',118),
  ('op -> LIMIT nr ;','op',3,'p_operator1','logic_grammar_.py',119),
  ('proced -> PROCED var DO listt END','proced',5,'p_proced','logic_grammar_.py',128),
  ('listt -> commands','listt',1,'p_proced1','logic_grammar_.py',132),
  ('listt -> listt commands','listt',2,'p_proced2','logic_grammar_.py',136),
  ('callf -> CALL var ;','callf',3,'p_callf','logic_grammar_.py',141),
]
