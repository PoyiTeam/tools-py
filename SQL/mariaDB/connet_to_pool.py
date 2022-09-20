#%%
import mariadb
import sys
#%%

try:
    pool = mariadb.ConnectionPool(pool_reset_connection=False,
                                  host="140.134.76.191",
                                  port=3306,
                                  user="sqltest",
                                  password="Aiotlab309-1",
                                  database="sqltest",
                                  pool_name="pooltest",
                                  pool_size=1)
    print("Connect successful!")

except mariadb.PoolError as e:
    print("Error connecting to MariaDB Platform: {e}".format(e))

pool.add_connection()
print(pool.pool_size)
# %%
