import os 
from sqlalchemy import create_engine
import numpy as np
import json
from graphviz import Digraph
from collections import defaultdict


DB_CONFIG = {
    'connection': 'postgres://postgres:postgres@localhost:5432/grp_old',
    'schemas' : ['cmn', 'sec', 'hrm', 'inv', 'ast', 'prc']
}

OUTPUT_DIRECTORY = 'out'

db = create_engine(DB_CONFIG['connection'])

def get_query_result():
    query = f'select * from sec.grp_user;'
    result = db.execute(query)
    return list(result)


if __name__ == "__main__":
    print(get_query_result())



