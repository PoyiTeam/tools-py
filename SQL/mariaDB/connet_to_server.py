#%%
import mariadb
import sys
#%%
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(user="sqltest",
                           password="Aiotlab309-1",
                           host="140.134.76.191",
                           port=3306,
                           database="sqltest")
    print("Connect successful!")

except mariadb.Error as e:
    print("Error connecting to MariaDB Platform: {e}".format(e=e))
    sys.exit(1)
