
from flask import Flask, request, jsonify
import mysql.connector

# initialize the flask application
app = Flask(__name__)

# Create database connection
conn = mysql.connector.connect(
   host="roundhouse.proxy.rlwy.net",
   user="root",
   password="aCa4-GehdH31BGHe1fDh4H4hagdC1hD5",
   database="railway",
   port=14241
)