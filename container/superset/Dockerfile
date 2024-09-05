FROM apache/superset:4.0.2

USER root

# Install Trino driver
RUN pip install trino

RUN rm superset/static/assets/images/superset.png
RUN rm superset/static/assets/images/superset-logo-horiz.png
RUN rm superset/static/assets/images/favicon.png

# Directly update the superset config
RUN sed -i "s/\"GENERIC_CHART_AXES\": True,/\"GENERIC_CHART_AXES\": True, /g" /app/superset/config.py && \
    sed -i "s/\"ENABLE_TEMPLATE_PROCESSING\": False,/\"ENABLE_TEMPLATE_PROCESSING\": True,/g" /app/superset/config.py &&\
    sed -i "s/\"DRILL_BY\": False,/\"DRILL_BY\": True,/g" /app/superset/config.py

# Switching back to using the `superset` user
USER superset

# Copy files from asset folder to the desired location in the container
COPY ./assets/* /app/superset/static/assets/images/



