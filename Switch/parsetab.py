
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA EQUAL ID LARROW LPAREN NUM RPAREN STRING SWITCH\n    switch : ID LARROW SWITCH LPAREN expr COMMA cases RPAREN\n    \n    expr    : NUM   \n            | ID \n    \n    cases   : STRING COMMA cases\n            | STRING EQUAL STRING COMMA cases \n            | STRING EQUAL STRING\n            | STRING\n    '
    
_lr_action_items = {'ID':([0,5,],[2,6,]),'$end':([1,12,],[0,-1,]),'LARROW':([2,],[3,]),'SWITCH':([3,],[4,]),'LPAREN':([4,],[5,]),'NUM':([5,],[8,]),'COMMA':([6,7,8,11,16,],[-3,9,-2,13,17,]),'STRING':([9,13,14,17,],[11,11,16,11,]),'RPAREN':([10,11,15,16,18,],[12,-7,-4,-6,-5,]),'EQUAL':([11,],[14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'switch':([0,],[1,]),'expr':([5,],[7,]),'cases':([9,13,17,],[10,15,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> switch","S'",1,None,None,None),
  ('switch -> ID LARROW SWITCH LPAREN expr COMMA cases RPAREN','switch',8,'p_switch','switch_yacc.py',9),
  ('expr -> NUM','expr',1,'p_expr','switch_yacc.py',14),
  ('expr -> ID','expr',1,'p_expr','switch_yacc.py',15),
  ('cases -> STRING COMMA cases','cases',3,'p_cases','switch_yacc.py',20),
  ('cases -> STRING EQUAL STRING COMMA cases','cases',5,'p_cases','switch_yacc.py',21),
  ('cases -> STRING EQUAL STRING','cases',3,'p_cases','switch_yacc.py',22),
  ('cases -> STRING','cases',1,'p_cases','switch_yacc.py',23),
]
