import os
import sys
import sqlalchemy

DB_URL = os.getenv('DB_URL')

def query_db(mindepth, mingradient):
    engine = sqlalchemy.create_engine(DB_URL)
    conn = engine.connect()
    query = sqlalchemy.text(""" 
        SELECT latitude, longitude, depth, gradient
        FROM wells
        WHERE depth > :mindepth AND gradient > :mingradient;
    """)
    result = conn.execute(query, {'mindepth':mindepth, 'mingradient':mingradient})
    return result.fetchall()

if __name__ == '__main__':
    mindepth = float(sys.argv[1])
    mingradient = float(sys.argv[2])
    print(query_db(mindepth, mingradient))