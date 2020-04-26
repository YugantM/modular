import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, redirect, url_for, flash,send_from_directory,jsonify


import json,sys
from werkzeug.utils import secure_filename


# In[100]:


from collections import Counter


# In[101]:


import pandas as pd



import urllib.request


app = Flask(__name__)


@app.route("/sql_generate")
def foo():
	return "hi there"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001',debug=True)
