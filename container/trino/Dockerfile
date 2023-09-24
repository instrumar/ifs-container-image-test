FROM trinodb/trino:368

USER root

# Install wget, tar and Java 17
RUN yum install -y wget tar \
    && wget https://download.oracle.com/java/GA/jdk17/0d483333a00540d886896bac774ff48b/35/GPL/openjdk-17_linux-x64_bin.tar.gz -O /tmp/openjdk-17_linux-x64_bin.tar.gz \
    && tar -xzvf /tmp/openjdk-17_linux-x64_bin.tar.gz -C /opt/ \
    && rm /tmp/openjdk-17_linux-x64_bin.tar.gz

# Set Java 17 as the default
ENV JAVA_HOME=/opt/jdk-17
ENV PATH=$JAVA_HOME/bin:$PATH

# Download and Extract Pulsar 3.0.0 connector 
RUN wget https://archive.apache.org/dist/pulsar/pulsar-3.0.0/apache-pulsar-3.0.0-bin.tar.gz -O /tmp/apache-pulsar-3.0.0.tar.gz
RUN tar -xzvf /tmp/apache-pulsar-3.0.0.tar.gz -C /tmp

# Move existing trino dependencies to temporary folder
RUN mv /usr/lib/trino/bin/run-trino /tmp
RUN mv /usr/lib/trino/plugin /tmp

# Replace the existing trino deployment with the trino deployment present in the connector
RUN rm -r /usr/lib/trino
RUN mv /tmp/apache-pulsar-3.0.0/trino/ /usr/lib/

# Move the previously backed-up plugin and the run-trino script to inside the docker image 
RUN mv /tmp/run-trino /usr/lib/trino/bin
RUN mv /tmp/plugin/* /usr/lib/trino/plugin

# Remove generated temporary files
RUN rm -rf /tmp/apache-pulsar-3.0.0.tar.gz /tmp/apache-pulsar-3.0.0

USER trino