# Use a simple base for downloading and setting permissions
FROM alpine as downloader
ADD https://github.com/streamnative/pulsar-io-lakehouse/releases/download/v3.1.0.3/pulsar-io-lakehouse-3.1.0.3.nar /tmp/pulsar-io-lakehouse-3.1.0.3.nar
RUN chmod 644 /tmp/pulsar-io-lakehouse-3.1.0.3.nar

# Use the Pulsar image
FROM apachepulsar/pulsar-all:3.1.0
COPY --from=downloader /tmp/pulsar-io-lakehouse-3.1.0.3.nar /pulsar/connectors/pulsar-io-lakehouse-3.1.0.3.nar

# Continue with the rest of your Dockerfile...
COPY ./iceberg.json /pulsar/connectors/iceberg.json
