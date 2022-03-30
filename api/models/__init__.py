from pydantic import BaseModel,create_model
from typing import Literal,List

name_counter=0

def ogmodel(*args,**fields):
    name=None
    base=None
    for a in args:
        if isinstance(a,str): name=a
        if isinstance(a,type): base=a
        if isinstance(a,tuple): base=a
        if isinstance(a,dict): d=a
    d={'__annotations__':{}}

    for f_name, f_def in fields.items():
        f_annotation=f_def if isinstance(f_def,type) else None
        f_annotation=f_def[0] if isinstance(f_def,tuple) else None
        f_value=f_def if not isinstance(f_def,type) else None
        f_value=f_def[1] if isinstance(f_def,tuple) and len(f_def)>1 else f_value

        d[f_name] = f_value
        if f_annotation: d['__annotations__'][f_name] = f_annotation

    global name_counter
    name_counter=name_counter+1
    base=base if isinstance(base,tuple) else (base,)
    if not name: name='_'.join(b.__name__ for b in base)+'_'+str(name_counter)
    return type(name,base,d)

class PaginationInput(BaseModel):
    page:int|None=1
    pageSize:int|None=10

class SortInput(BaseModel):
    sortOrder: Literal['ASC','DESC']|None = 'DESC'

class LanguageInput(BaseModel):
    lang:Literal['en','ru']|None='en'

class PaginationData(BaseModel):
    page:int
    pageSize:int
    pagesTotal:int

class PaginationOptions(BaseModel):
    objTotal:int
    total:int|None
    pagination:PaginationData

class PaginatedOutput(BaseModel):
    options:PaginationOptions
    items:List

class Timestamp(BaseModel):
    created:int |None = 0
    changed:int

