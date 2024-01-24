import pymysql
import datetime
def create_connect(**kwargs):
    connect = pymysql.connect(**kwargs)

    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)

    return cursor


def insert_obj(connect, table_name, obj):
    fields = ','.join([k for k in obj.keys()])
    # values = ','.join(['%s' if type(v) !=str else "'%s'" for v in obj.values() ])
    values = list()
    for k, v in obj.items():
        if type(v) == str:
            values.append(f"'{v}'")
        elif type(v) == int:
            values.append(f"{v}")
        elif type(v) == bool:
            values.append(f"{v}")
        elif type(v) == float:
            values.append(f"{v}")
        elif type(v) == datetime.datetime:
            values.append(f"'{v}'")
        else:
            raise Exception(f"unprocessing type {type(v)}")
    values = ','.join(values)
    sql = f'insert into {table_name} ({fields}) values({values})'
    return connect.insert(sql)