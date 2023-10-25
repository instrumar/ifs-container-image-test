FROM apache/superset:3.0.1

USER root

# Install Trino driver
RUN pip install trino

RUN rm superset/static/assets/images/superset.png
RUN rm superset/static/assets/images/superset-logo-horiz.png

# Switching back to using the `superset` user
USER superset

# Copy files from asset folder to the desired location in the container
COPY ./assets/* /app/superset/static/assets/images/



