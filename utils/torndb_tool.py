from toolkit.utils.torndb import Connection
import datetime
import pandas as pd


class TornConn(Connection):
    def insert_obj(self,table_name,obj):

        fields = []
        #values = ','.join(['%s' if type(v) !=str else "'%s'" for v in obj.values() ])
        values = list()
        for k,v in obj.items():
            if  pd.isna(v):
                continue
            if type(v) == str:
                fields.append(k)
                values.append(f"'{v}'")
            elif type(v) == int:
                fields.append(k)
                values.append(f"{v}")
            elif type(v) == bool:
                fields.append(k)
                values.append(f"{v}")
            elif type(v) == float:
                fields.append(k)
                values.append(f"{v}")
            elif type(v) == datetime.datetime:
                fields.append(k)
                values.append(f"'{v}'")

            else:
                raise Exception(f"unprocessing type {type(v)}")
        values = ','.join(values)
        fields = ','.join(fields)
        sql = f'insert into {table_name} ({fields}) values({values})'
        return self.insert(sql)




    def upsert_obj(self,table_name,primary,obj):
        fields = ','.join([k for k in obj.keys()])
        values = list()
        updates = list()
        format_list = list()
        for k, v in obj.items():
            if type(v) == str and  '%' in v:
                format_list.append(v.replace('%',''))  #for insert
                format_list.append(v.replace('%',''))  #for update
                v = "%s"
            elif type(v) in (str,datetime.datetime):
                v = f"'{v}'"

            elif type(v) in( int,float):
                pass
            else:
                raise Exception(f"unprocessing type {type(v)}")

            if k != primary:
                updates.append(f"{k}={v}")
            values.append(f"{v}")
        values = ','.join(values)

        updates = ','.join(updates)
        sql =f"INSERT INTO {table_name} ({fields}) values ({values}) " \
              f"ON DUPLICATE KEY UPDATE {updates};"

        if format_list:
            return self.execute_rowcount(sql,*format_list)
        else:
            return self.execute_rowcount(sql)

