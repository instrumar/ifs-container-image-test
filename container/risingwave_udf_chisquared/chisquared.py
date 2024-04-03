# Import components from the risingwave.udf module
import numpy as np
from decimal import Decimal
from risingwave.udf import udf, UdfServer
import struct
import socket


# Define a table function
@udf(input_types=['integer[]', 'numeric', 'numeric'], result_type='numeric')
def chisquared_numeric(data, data_mean, data_std):
    data_array = np.array(data)
    if data_array.size == 0 or data_mean == None or data_std == None or data_mean == 0 or data_std == 0:
        return Decimal(0.0)
    else:
        return Decimal((((data_array - data_mean)/data_std)**2).sum()/data_array.size)

# Define a table function
@udf(input_types=['real[]', 'double precision', 'double precision'], result_type='numeric')
def chisquared_double(data, data_mean, data_std):
    data_array = np.array(data)
    if data_array.size == 0 or data_mean == None or data_std == None or data_mean == 0 or data_std == 0:
        return Decimal(0.0)
    else:
        return Decimal((((data_array - data_mean)/data_std)**2).sum()/data_array.size)

        

if __name__ == '__main__':
    server = UdfServer(location="0.0.0.0:8815") # You can use any available port in your system. Here we use port 8815.
    server.add_function(chisquared_double)
    server.add_function(chisquared_numeric)
    server.serve()

