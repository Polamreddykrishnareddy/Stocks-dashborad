import re
import db
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
collection_name ="ibm"
ibm_data=db.mongodb_connection(collection_name)
print(ibm_data.head())

def open_stocks_of_ibm():
    open_data = ibm_data.Open
    return open_data
open_stocks_of_ibm()
