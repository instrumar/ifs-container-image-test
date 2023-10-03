# Use a simple base for downloading and setting permissions
FROM alpine as downloader
ADD https://github.com/streamnative/pulsar-io-lakehouse/releases/download/v3.1.0.4/pulsar-io-lakehouse-3.1.0.4-cloud.nar /tmp/pulsar-io-lakehouse-3.1.0.4-cloud.nar
ADD https://github.com/streamnative/pulsar-io-lakehouse/releases/download/v3.1.0.4/pulsar-io-lakehouse-3.1.0.4.nar /tmp/pulsar-io-lakehouse-3.1.0.4.nar
RUN chmod 644 /tmp/pulsar-io-lakehouse-3.1.0.4-cloud.nar

# Use the Pulsar image
FROM apachepulsar/pulsar-all:3.1.0
COPY --from=downloader /tmp/pulsar-io-lakehouse-3.1.0.4-cloud.nar /pulsar/connectors/pulsar-io-lakehouse-3.1.0.4-cloud.nar
COPY --from=downloader /tmp/pulsar-io-lakehouse-3.1.0.4.nar /pulsar/connectors/pulsar-io-lakehouse-3.1.0.4.nar

# Continue with the rest of your Dockerfile...
COPY ./iceberg.json /pulsar/connectors/iceberg.json
