import sys
import sqlalchemy

conn_string = "postgresql://tdi:qKmd8s5ze7WAYV@adventureworks.tditrain.com:5431/wells"

def query_db(mindepth, mingradient):
    engine = sqlalchemy.create_engine(conn_string)
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