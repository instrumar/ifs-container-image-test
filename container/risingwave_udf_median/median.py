# Import components from the risingwave.udf module
import statistics

from risingwave.udf import udf, UdfServer
import struct
import socket


# Define a table function
@udf(input_types=['numeric[]'], result_type='numeric')
def median_numeric(n):
    return statistics.median(n)

# Define a table function
@udf(input_types=['double precision[]'], result_type='double precision')
def median_double(n):
    return statistics.median(n)
        

if __name__ == '__main__':
    server = UdfServer(location="0.0.0.0:8815") # You can use any available port in your system. Here we use port 8815.
    server.add_function(median_double)
    server.add_function(median_numeric)
    server.serve()

