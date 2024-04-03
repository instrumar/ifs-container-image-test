# Import components from the risingwave.udf module
import numpy as np
from risingwave.udf import udf, UdfServer
import struct
import socket


# Define a table function
@udf(input_types=['integer[]', 'numeric', 'numeric'], result_type='numeric')
def chisquared_numeric(data, data_mean, data_std):
    print(data)
    data_array = np.array(data)
    print(data_array)
    print(len(data_array))
    return (((data_array - data_mean)/data_std)**2).sum()/len(data_array)

# Define a table function
@udf(input_types=['real[]', 'double precision', 'double precision'], result_type='double precision')
def chisquared_double(data, data_mean, data_std):
    data_array = np.array(data)
    return (((data_array - data_mean)/data_std)**2).sum()/len(data)

        

if __name__ == '__main__':
    server = UdfServer(location="0.0.0.0:8815") # You can use any available port in your system. Here we use port 8815.
    server.add_function(chisquared_double)
    server.add_function(chisquared_numeric)
    server.serve()

