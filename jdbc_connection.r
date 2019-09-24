options(java.parameters = "-Xmx8g")

library(DBI)
library(rJava)
library(RJDBC)


# ===== 1 - Check if connection can be established error free

drv <- JDBC("net.sourceforge.jtds.jdbc.Driver",
            "jtds-1.3.1.jar")

conn <- try(
  dbConnect(drv,"jdbc:jtds:sqlserver://<sql server address>/<db name>;user=<user name>;password=<password>;")
  , silent = T
)

sql_cond <- isTRUE(inherits(x = conn, what = 'try-error'))

if (sql_cond) {stop(' SQL connection is failed; Check the connection string')}
