FROM python:3.8-slim

# Install any dependencies
RUN pip install pulsar-client

# Add your task script
COPY dag.py /dag.py

CMD ["python", "/dag.py"]
