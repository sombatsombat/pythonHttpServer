connection_string = 'postgres://sombat@127.0.0.1/infraredRF'

import json  
import sqlalchemy  
db = sqlalchemy.create_engine(connection_string)  
engine = db.connect()  
meta = sqlalchemy.MetaData(engine)  

result = engine.execute("SELECT 1")
print (result.rowcount)
