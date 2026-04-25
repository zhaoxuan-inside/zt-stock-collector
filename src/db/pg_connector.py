from psycopg2.extras import execute_values
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
from typing import Iterable
from abc import ABC

class PGConnector(ABC):
    
    def __init__(self, dsn: str, table_name: str, create_sql: str, min_conn=1, max_conn=10):
        self._dsn = dsn
        self._table_name = table_name
        self._create_sql = create_sql
        self._pool = SimpleConnectionPool(min_conn, max_conn, dsn)

    @contextmanager
    def _get_conn(self):
        conn = self._pool.getconn()
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            self._pool.putconn(conn)

    def init_tables(self) -> None:
        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(self._create_sql)
            conn.commit()

    def _execute(self, sql: str, params: Iterable[tuple], page_size=100) -> int:
        with self._get_conn() as conn:
            with conn.cursor as cur:
                execute_values(cur, sql, params, page_size)
                return cur.rowcount

    def insert(self, data: Iterable[tuple], page_size=100) -> int:
        if not data:
            return 0
        sql = f"INSERT INTO {self._table_name} VALUES %s"

        return self._execute(sql, data, page_size)

    def update(self, set_clause: str, where_clause: str, data: Iterable[tuple]) -> int:
        if not data:
            return 0
        sql = f"UPDATE {self._table_name} SET {set_clause} WHERE {where_clause}"

        return self._execute(sql, data)

    def delete(self, where_clause: str, data: Iterable[tuple]) -> int:
        if not data:
            return 0
        sql = f"DELETE FROM {self._table_name} WHERE {where_clause}"
        return self._execute(sql, data)
    
    def select(self, columes: str="id", where_clause: str="", order_clause: str="", asc: bool=True, data: tuple=(), page_size=100) -> List[tuple]:
        
        sql = ""
        if columes:
            sql = f"SELECT {columes} FROM {self._table_name} "

        if where_clause:
            sql += f" WHERE {where_clause} "
        
        if order_clause:
            sql += f" ORDER BY {order_clause} "
            if asc:
                sql += " ASC "
            else:
                sql += " DESC "

        sql += f" LIMIT {page_size} "
        
        with self._get_conn() as conn:
            with conn.cursor as cur:
                cur.execute(sql, data)
                return cur.fetchall()

    def close(self):
        self._pool.closeall()