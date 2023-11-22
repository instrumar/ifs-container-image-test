# Use the official PostgreSQL image as a base
FROM bitnami/postgresql:15.4.0-debian-11-r10

# Set environment variables if necessary
# ENV POSTGRES_PASSWORD=yourpassword
# ENV POSTGRES_USER=youruser
# ENV POSTGRES_DB=yourdb

USER root
# Update packages and install pgagent
RUN apt-get update && apt-get install -y \
    postgresql-contrib \
    pgagent

USER 1001
# Run any additional commands if necessary
# RUN some-additional-command


