# Import components from the risingwave.udf module
import statistics

from risingwave.udf import udf, UdfServer
import struct
import socket


# Define a table function
@udf(input_types='real', result_type='real')
def median(n):
    return statistics.median(n)
        

if __name__ == '__main__':
    server = UdfServer(location="0.0.0.0:8815") # You can use any available port in your system. Here we use port 8815.
    server.add_function(median)

