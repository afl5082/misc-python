import MySQLdb

db = MySQLdb.connect(host="xyz.rds.amazonaws.com",    # host,localhost
                     user="ACBC",         # username
                     passwd="AYZ",        # password
                     db="XYZ")            # name of the data base
cur = db.cursor()

listid = ['john','beth']
cur.execute("INSERT INTO testlamda (office) VALUES (%s);", [",".join(listid)]) #testlambda is name of table, office is column 

db.commit()
