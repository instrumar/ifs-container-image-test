# Import components from the risingwave.udf module
import statistics

from risingwave.udf import udtf, UdfServer
import struct
import socket


# Define a table function
@udtf(input_types='double precision', result_type='double precision')
def median(n):
    print(n)
    return statistics.median(n)
        

if __name__ == '__main__':
    server = UdfServer(location="0.0.0.0:8815") # You can use any available port in your system. Here we use port 8815.
    server.add_function(median)
    server.serve()

