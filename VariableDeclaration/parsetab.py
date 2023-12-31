
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOLEAN_MISSING EQUALS ID LARROW NUMBER RARROW STRING\n    declaration : ID LARROW value\n                | ID EQUALS value\n                | value RARROW ID\n    \n    value   : STRING\n            | NUMBER\n            | BOOLEAN_MISSING\n    '
    
_lr_action_items = {'ID':([0,9,],[2,12,]),'STRING':([0,7,8,],[4,4,4,]),'NUMBER':([0,7,8,],[5,5,5,]),'BOOLEAN_MISSING':([0,7,8,],[6,6,6,]),'$end':([1,4,5,6,10,11,12,],[0,-4,-5,-6,-1,-2,-3,]),'LARROW':([2,],[7,]),'EQUALS':([2,],[8,]),'RARROW':([3,4,5,6,],[9,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration':([0,],[1,]),'value':([0,7,8,],[3,10,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaration","S'",1,None,None,None),
  ('declaration -> ID LARROW value','declaration',3,'p_declaration','var_yacc.py',36),
  ('declaration -> ID EQUALS value','declaration',3,'p_declaration','var_yacc.py',37),
  ('declaration -> value RARROW ID','declaration',3,'p_declaration','var_yacc.py',38),
  ('value -> STRING','value',1,'p_value','var_yacc.py',43),
  ('value -> NUMBER','value',1,'p_value','var_yacc.py',44),
  ('value -> BOOLEAN_MISSING','value',1,'p_value','var_yacc.py',45),
]
