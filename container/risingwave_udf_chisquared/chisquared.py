from decimal import Decimal, InvalidOperation
import numpy as np
from risingwave.udf import udf, UdfServer

@udf(input_types=['integer[]', 'numeric', 'numeric'], result_type='numeric')
def chisquared_numeric(data, data_mean, data_std):
    try:
        data_array = np.array(data)
        if data_array.size == 0 or data_mean is None or data_std is None or data_mean == 0 or data_std == 0:
            return Decimal(0.0)
        else:
            return Decimal((((data_array - float(data_mean))/float(data_std))**2).sum()/data_array.size)
    except (TypeError, InvalidOperation) as e:
        # Handle unexpected data types or operations
        return Decimal(0.0)

@udf(input_types=['real[]', 'double precision', 'double precision'], result_type='numeric')
def chisquared_double(data, data_mean, data_std):
    try:
        data_array = np.array(data)
        if data_array.size == 0 or data_mean is None or data_std is None or data_mean == 0 or data_std == 0:
            return Decimal(0.0)
        else:
            return Decimal((((data_array - float(data_mean))/float(data_std))**2).sum()/data_array.size)
    except (TypeError, InvalidOperation) as e:
        # Handle unexpected data types or operations
        return Decimal(0.0)


        

if __name__ == '__main__':
    server = UdfServer(location="0.0.0.0:8815") # You can use any available port in your system. Here we use port 8815.
    server.add_function(chisquared_double)
    server.add_function(chisquared_numeric)
    server.serve()

