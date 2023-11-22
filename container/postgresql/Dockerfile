# Use the official PostgreSQL image as a base
FROM postgres:15.5

# Set environment variables if necessary
# ENV POSTGRES_PASSWORD=yourpassword
# ENV POSTGRES_USER=youruser
# ENV POSTGRES_DB=yourdb

# Update packages and install pgagent
RUN apt-get update && apt-get install -y \
    postgresql-contrib \
    pgagent

# Run any additional commands if necessary
# RUN some-additional-command

# Expose the PostgreSQL port
EXPOSE 5432

# Set the default command to run when starting the container
# This command will start PostgreSQL and pgAgent
CMD ["postgres"]
