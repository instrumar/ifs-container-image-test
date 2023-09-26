#!/bin/sh


# Check if schema exists
/opt/apache-hive-metastore-3.1.2-bin/bin/schematool -dbType postgres -info

if [ $? -eq 1 ]; then
  echo "Getting schema info failed. Probably not initialized. Initializing..."
  /opt/apache-hive-metastore-3.1.2-bin/bin/schematool -initSchema -dbType postgres
fi

/opt/apache-hive-metastore-3.1.2-bin/bin/start-metastore
