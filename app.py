from flask import Flask, render_template, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
mongouri=os.getenv("mongo_uri")
client = MongoClient(mongouri)
db = client['test']
collection = db['todo']
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form['itemName']
    item_description = request.form['itemDescription']
    todo_item = {
        'name': item_name,
        'description': item_description
    }
    collection.insert_one(todo_item)
    return f'To-do item "{item_name}" added successfully!'
if __name__ == '__main__':
    app.run(debug=True, port=5001)
