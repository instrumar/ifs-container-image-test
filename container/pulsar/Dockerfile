# # Use a simple base for downloading and setting permissions
# FROM alpine as downloader
# # ADD https://github.com/streamnative/pulsar-io-lakehouse/releases/download/v3.1.0.2/pulsar-io-lakehouse-3.1.0.2-cloud.nar /tmp/pulsar-io-lakehouse-3.1.0.2-cloud.nar
# # ADD https://github.com/streamnative/pulsar-io-lakehouse/releases/download/v3.1.0.2/pulsar-io-lakehouse-3.1.0.2.nar /tmp/pulsar-io-lakehouse-3.1.0.2.nar
# # ADD https://repo1.maven.org/maven2/org/apache/hive/hive-metastore/3.1.2/hive-metastore-3.1.2.jar /tmp/hive-metastore-3.1.2.jar
# # ADD https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-hive-runtime/0.13.2/iceberg-hive-runtime-0.13.2.jar /tmp/iceberg-hive-runtime-0.13.2.jar

# # RUN chmod 644 /tmp/pulsar-io-lakehouse-3.1.0.2-cloud.nar
# # RUN chmod 644 /tmp/pulsar-io-lakehouse-3.1.0.2.nar
# # RUN chmod 644 /tmp/hive-metastore-3.1.2.jar
# # RUN chmod 644 /tmp/iceberg-hive-runtime-0.13.2.jar

# ADD https://github.com/streamnative/kop/releases/download/v3.1.1.1/pulsar-protocol-handler-kafka-3.1.1.1.nar /tmp/pulsar-protocol-handler-kafka-3.1.1.1.nar

# Use the Pulsar image
FROM apachepulsar/pulsar-all:3.1.1
# COPY --from=downloader /tmp/pulsar-protocol-handler-kafka-3.1.1.1.nar /protocols/pulsar-protocol-handler-kafka-3.1.1.1.nar
RUN pip install requests


# # Continue with the rest of your Dockerfile...
# COPY ./iceberg.json /pulsar/connectors/iceberg.json
