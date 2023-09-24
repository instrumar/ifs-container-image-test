FROM apachepulsar/pulsar-all:3.1.0

# Add the NAR file
ADD https://github.com/streamnative/pulsar-io-lakehouse/releases/download/v3.1.0.3/pulsar-io-lakehouse-3.1.0.3.nar /pulsar/connectors/pulsar-io-lakehouse-3.1.0.3.nar

# Adjust the permissions on the added file
RUN chmod 644 /pulsar/connectors/pulsar-io-lakehouse-3.1.0.3.nar

# Copy the iceberg configuration file
COPY ./iceberg.json /pulsar/connectors/iceberg.json
