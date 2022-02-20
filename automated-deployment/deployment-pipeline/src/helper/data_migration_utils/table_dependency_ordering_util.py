import os 
from sqlalchemy import create_engine
import numpy as np
import json
from graphviz import Digraph
from collections import defaultdict


DB_CONFIG = {
    'connection': 'postgres://postgres:postgres@localhost:5432/grp_new',
    'schemas' : ['cmn', 'sec', 'hrm', 'inv', 'ast', 'prc']
}

OUTPUT_DIRECTORY = 'out'

db = create_engine(DB_CONFIG['connection'])
tables = []
graph = {}
visited = defaultdict(lambda : False)
ordered_tables = []


def get_dependency_list(schema_name, table_name, key_name):
    '''
        get list of all the tables in the database which are dependent (foreign key dependency) on a specific table 
    '''

    query = f"""
        SELECT R.table_name , R.table_schema
        FROM   information_schema.constraint_column_usage u 
            INNER JOIN information_schema.referential_constraints FK  
                    ON U.constraint_catalog = FK.unique_constraint_catalog 
                        AND U.constraint_schema = FK.unique_constraint_schema 
                        AND U.constraint_name = FK.unique_constraint_name 
            INNER JOIN information_schema.key_column_usage R 
                    ON R.constraint_catalog = FK.constraint_catalog 
                        AND R.constraint_schema = FK.constraint_schema 
                        AND R.constraint_name = FK.constraint_name 
        WHERE  U.column_name = '{key_name}' 
            AND U.table_schema = '{schema_name}' 
            AND U.table_name = '{table_name}';
        """ 
    return list(db.execute(query))





def construct_dependency_graph():
    '''
        construct a directed graph out of all the tables 
    '''
    for schema in DB_CONFIG['schemas']:
        table_list = db.execute(f"SELECT * FROM information_schema.tables WHERE table_schema = '{schema}'")  
        for table in table_list:
            TABLE_NAME = table[2]
            column_list = db.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = '{schema}' AND table_name   = '{TABLE_NAME}';")
            column_list = [column[0] for column in column_list]
            total_dependency = []
            for column in column_list:
                dependency_list = get_dependency_list(schema, TABLE_NAME, column)
                for dependency in dependency_list:
                    total_dependency.append(dependency[1] + '.' +dependency[0])
                # if len(dependency_list) != 0 :
                #     print(f'Table {TABLE_NAME} has total {len(dependency_list)} dependencies for key {column}')
            total_dependency = list(set(total_dependency))
            if total_dependency: 
                # print(f'Table {schema}.{TABLE_NAME} has {len(total_dependency)} dependencies => {total_dependency}')
                pass
            graph[f'{schema}.{TABLE_NAME}'] = total_dependency

            



def get_topological_sort_order(node):
    '''
        Run Depth-First-Search to get a sorted order for inserting the rows in the tables 
    '''
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            get_topological_sort_order(child)
    ordered_tables.append(node)
    


def draw_graph():
    dot =  Digraph(comment='GRP Tables Dependency Graph', node_attr={'color': 'lightblue2', 'style': 'filled'})
    dot.attr(overlap='false')
    
    for node in graph:
        dot.node(f'{node}', f'{node}')
        for child in graph[node]:
            dot.edge(f'{node}', f'{child}')
        if not visited[node]:
            get_topological_sort_order(node)
            
    dot.render(f'{OUTPUT_DIRECTORY}/GRP__Tables_Foreign_Key_References.gv')  
    os.system(f'cd {OUTPUT_DIRECTORY}; dot -Ksfdp -o GRP__Tables_Foreign_Key_References.svg -Tsvg GRP__Tables_Foreign_Key_References.gv; rm -rf *.pdf;')
    # RUN this command in shell : dot -Ksfdp -o output.svg -Tsvg GRP__Tables_Dependency.gv


def get_sorted_table_list():
    global graph
    construct_dependency_graph()
    with open('graph.json', 'w') as fp:
        json.dump(graph, fp, indent=4)
    graph = json.load(open('graph.json'))
    for node in graph:
        if not visited[node]:
            get_topological_sort_order(node)
    return list(ordered_tables)[::-1]





# if __name__ == "__main__":

#     construct_dependency_graph()
#     with open('graph.json', 'w') as fp:
#         json.dump(graph, fp, indent=4)

#     graph = json.load(open('graph.json'))

#     draw_graph()

#     for node in graph:
#         if not visited[node]:
#             get_topological_sort_order(node)

#     print(list(ordered_tables))
    
