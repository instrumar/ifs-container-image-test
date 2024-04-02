# Import components from the risingwave.udf module
import statistics

from risingwave.udf import udf, UdfServer
import struct
import socket


# Define a table function
@udf(input_types='array', result_type='double precision')
def median(n):
    statistics.median(n)
        

if __name__ == '__main__':
    server = UdfServer(location="0.0.0.0:8815") # You can use any available port in your system. Here we use port 8815.
    server.add_function(median)
    server.serve()

