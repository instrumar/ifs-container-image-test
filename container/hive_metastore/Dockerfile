# Use the slim version of the Java 8 JRE as the base image
FROM openjdk:8-jre-slim as builder

# Define working directory in the image
WORKDIR /opt

# Set environment variables for software versions and paths
ENV HADOOP_VERSION=3.3.1
ENV METASTORE_VERSION=3.1.2
ENV PSQL_CONN_VERSION=42.3.1
ENV HADOOP_HOME=/opt/hadoop-${HADOOP_VERSION}
ENV HIVE_HOME=/opt/apache-hive-metastore-${METASTORE_VERSION}-bin

# Install required tools and download required binaries
RUN apt update && apt install -y curl && \
    curl -L https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz | tar zxf - && \
    curl -L https://repo1.maven.org/maven2/org/apache/hive/hive-standalone-metastore/${METASTORE_VERSION}/hive-standalone-metastore-${METASTORE_VERSION}-bin.tar.gz | tar zxf - && \
    curl -L https://jdbc.postgresql.org/download/postgresql-${PSQL_CONN_VERSION}.jar -o ${HIVE_HOME}/lib/postgresql-${PSQL_CONN_VERSION}.jar

# Use the slim version of the Java 8 JRE for the final image
FROM openjdk:8-jre-slim

# Set working directory and environment variables in the image
WORKDIR /opt
ENV HADOOP_VERSION=3.3.1
ENV METASTORE_VERSION=3.1.2
ENV HADOOP_HOME=/opt/hadoop-${HADOOP_VERSION}
ENV HIVE_HOME=/opt/apache-hive-metastore-${METASTORE_VERSION}-bin

# Copy binaries from the builder stage to the final image
COPY --from=builder ${HIVE_HOME} ${HIVE_HOME}
COPY --from=builder ${HADOOP_HOME} ${HADOOP_HOME}

# Copy the configuration and entrypoint script into the image
COPY /conf/conf.xml ${HIVE_HOME}/conf/metastore-site.xml
COPY /entrypoint.sh /entrypoint.sh

# Create a user for Hive, set permissions and expose the required port
RUN groupadd -r hive --gid=1000 && \
    useradd -r -g hive --uid=1000 -d ${HIVE_HOME} hive && \
    chown hive:hive -R ${HIVE_HOME} && \
    chown hive:hive /entrypoint.sh && chmod +x /entrypoint.sh && \
    chown -R hive:hive /opt && chmod -R 755 /opt

# Switch to the 'hive' user
USER hive

# Expose the metastore port
EXPOSE 9083

# Set the entrypoint script as the default command to run
ENTRYPOINT ["/entrypoint.sh"]
