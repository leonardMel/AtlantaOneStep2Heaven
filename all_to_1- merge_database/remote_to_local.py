#==== header here ===================================================
# Team 16 - city: Atlanta
# Student number: 656982 | Student name: Zhenya Li    | Surname: Li 
# Student number: 616805 | Student name: Meng Li      | Surname: Li
# Student number: 650382 | Student name: Ming Yu      | Surname: Chang
# Student number: 548771 | Student name: Hao Duan     | Surname: Duan
# Student number: 629341 | Student name: Yu Sun       | Surname: Sun
# Student number: 705077 | Student name: Yuxiang Zhou | Surname: Zhou
# ===================================================================
import inspect
import couchdb
from couchdb.design import ViewDefinition
import sys
from collections import Counter
import re

# === I keep this, simply because there is an identification error in my OS
# === have to inspect the couchdb to make the subclass visible.
for name, obj in inspect.getmembers(couchdb):
    if inspect.isclass(obj):
        print obj

# ==== handle input parameters ======
if(len(sys.argv)>=4):
    if(sys.argv[1]):
        local_dbname = sys.argv[1]
    if(sys.argv[2]):
        remote_server_ip = sys.argv[2]
    if(sys.argv[3]):
        remote_dbname = sys.argv[3]
else:
    print "not enough parameter: [local_dbname] [remote_server_ip] [remote_dbname]"

local_server = couchdb.Server()
local_db = local_server[local_dbname]
remote_server = couchdb.Server("http://"+remote_server_ip+":5984")
remote_db = remote_server[remote_dbname]

#========database default assignment ===========
#local_server = couchdb.Server()
#local_db = local_server['test']

#remote_server = couchdb.Server("http://115.146.93.74:5984")
#remote_db = remote_server['test']



for id in remote_db:
    print id
    doc = remote_db[id]
    # try to save this to local, if conflicted? pass. use the local version
    try: 
        local_db.save(doc)
        print "saved? " + doc.id
    except Exception:
        print "one conflict, pass " + doc.id
        pass


