import os 
from sqlalchemy import create_engine
import numpy as np
import json
from graphviz import Digraph
from collections import defaultdict
from table_dependency_ordering_util import get_sorted_table_list
import traceback


DB_CONFIG = {
    'connection': 'postgres://postgres:postgres@localhost:5432/grp_bcc_live',
    'schemas' : ['cmn', 'sec', 'hrm', 'inv', 'ast', 'prc']
}

OUTPUT_DIRECTORY = 'out'

db = create_engine(DB_CONFIG['connection'])
tables = []
graph = {}
visited = defaultdict(lambda : False)
ordered_tables = []


def get_column_info(schema_name, table_name):
    '''
        get list of all the tables in the database which are dependent (foreign key dependency) on a specific table 
    '''

    query = f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = '{schema_name}'
        AND table_name   = '{table_name}'
        """ 
    return list(db.execute(query))



def get_column_info_list():
    column_info = []
    for schema in DB_CONFIG['schemas']:
        table_list = db.execute(f"SELECT * FROM information_schema.tables WHERE table_schema = '{schema}'")  
        for table in table_list:
            TABLE_NAME = table[2]
            # print(f'table -> {schema}.{TABLE_NAME}')
            # print(f'Table {schema}.{TABLE_NAME} has these columns : ' + str(get_column_info(schema, TABLE_NAME)))
            column_info += [[schema, TABLE_NAME, get_column_info(schema, TABLE_NAME)]]
    return column_info


def generate_insert_sql(source_db_name, column_info):
    schema_name, table_name, column_data_type_list = column_info[0], column_info[1], column_info[2]
    column_string = column_data_type_list[0][0]
    column_data_type_str = column_data_type_list[0][0] + " " + column_data_type_list[0][1]
    for col in column_data_type_list[1:]:
        column_string += ', ' + col[0]
        column_data_type_str += ', ' + col[0] + ' ' + col[1]
    insert_sql = f"INSERT INTO {schema_name}.{table_name}({column_string})\n" \
                 f"SELECT {column_string}\n" \
                 f"FROM dblink('dbname={source_db_name}',\n'SELECT {column_string}\nFROM {schema_name}.{table_name}')\n" \
                 f"AS x({column_data_type_str});\n"
    return insert_sql


if __name__ == "__main__":
    column_info = get_column_info_list()
    sorted_table_list = get_sorted_table_list()
    print(f'Total Tables = {len(sorted_table_list)}')
    # print(sorted_table_list)
    insert_into_select_queries = {}
    for table in column_info:
        insert_into_select_statement = generate_insert_sql('grp_bcc_live', table)
        insert_into_select_queries[table[0] + '.' + table[1]] = insert_into_select_statement
        # print(insert_into_select_queries[table[0] + '.' + table[1]])
        # fp = open(f'insert_into_select/{table[0]}_{table[1]}.sql', 'w')
        # fp.write(insert_into_select_statement)


    DESTINATION_DB_NAME = 'grp_new'
    db_destination = create_engine(f'postgres://postgres:postgres@localhost:5432/{DESTINATION_DB_NAME}')
    for table in sorted_table_list:
        try:
            db_destination.execute(f'truncate {table} cascade')
            # print(f'Truncated Table {table}')
            db_destination.execute(insert_into_select_queries[table])
            print(f'Migrated data for table {table}')
        except Exception as e:
            print(f'Table : {table} migration FAILED , table or view does not exist')
            # traceback.print_exc()

