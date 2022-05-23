import psycopg2
from psycopg2.extras import RealDictCursor


class Database:

    def __init__(self, dbname="habrdb", user="habrkirill", password="qwerty", host="pgsql", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def decorate(func):
        """Database connection"""

        def wrapper(self, *args, **kwargs):
            ps_connection = psycopg2.connect(user=self.user,
                                             password=self.password,
                                             host=self.host,
                                             port=self.port,
                                             database=self.dbname)
            ps_connection.autocommit = True
            cursor = ps_connection.cursor(cursor_factory=RealDictCursor)
            kwargs["cursor"] = cursor
            data = func(self, *args, **kwargs)
            cursor.close()
            ps_connection.close()
            return data

        return wrapper

    @decorate
    def write_data_to_table_result(self, **kwargs) -> str:
        """Writing data to a database table"""
        cursor = kwargs.pop("cursor")

        param = []
        for k, v in kwargs.items():
            if v is not None:
                param.append((k, v))

        keys, values = [x[0] for x in param], {x[0]: x[1] for x in param}
        placeholders = [f"%({x})s" for x in keys]

        sql = f"""
            INSERT INTO result ({', '.join(keys)})
            VALUES ({', '.join(placeholders)})
            ON CONFLICT ({''.join(keys[0:1])}, {''.join(keys[1:2])}) DO UPDATE
            SET {
        ', '.join([f"{keys} = '{values}'" for keys, values in param])
        }
        """

        cursor.execute(sql, values)
        return sql

    @decorate
    def getting_results(self, cursor=None):
        sql = "SELECT id, ip_adress, gender, bju, water, callories FROM result ORDER BY id"

        cursor.execute(sql)
        result = cursor.fetchall()
        return result


if __name__ == '__main__':
    postgre = Database()
