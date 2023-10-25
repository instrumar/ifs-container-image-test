FROM apache/superset:2.1.0

USER root
# Example: installing the MySQL driver to connect to the metadata database
# if you prefer Postgres, you may want to use `psycopg2-binary` instead
# Install Trino driver
RUN pip install trino
# Example: installing a driver to connect to Redshift
# Find which driver you need based on the analytics database
# you want to connect to here:
# https://superset.apache.org/installation.html#database-dependencies
# Switching back to using the `superset` user
USER superset

FROM apache/superset:3.0.1

USER root

# Install Trino driver
RUN pip install trino

RUN rm superset/static/assets/images/superset.png
RUN rm superset/static/assets/images/superset-logo-horiz.png

# Switching back to using the `superset` user
USER superset

# Copy files from asset folder to the desired location in the container
COPY asset/* /app/superset/static/assets/images/



