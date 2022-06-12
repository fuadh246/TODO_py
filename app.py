from crypt import methods
from flask import Flask, render_template, request, redirect, url_for,session
import os
import pymongo
MONGODB_URI ='mongodb+srv://fuad:Fuad@todopy.z78my1s.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client.TODOpy
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

todo_list = list()
@app.route('/' , methods= ['GET','POST']) # this decorator create the home route
def home():
    show_data()
    if request.method == 'GET':
        return render_template('index.html', title='TODOpy',todo_list=todo_list)
    if request.method == 'POST':
        topic = request.form['topic']
        due_date = request.form['date']
        if topic and due_date != '':
            db.tasks.insert_one({'topic': topic, 'due_date': due_date})
            return redirect('/')
        else:
            return render_template('index.html', title='TODOpy',todo_list=todo_list)

@app.route('/update', methods= ['GET','POST'])
def update():
    return render_template('update.html',title='TODOpy')
    
def show_data():
    collection = db['tasks']
    datas = collection.find({})
    for data in datas:
        if (data['topic'],data['due_date']) not in todo_list:
            todo_list.append((data['topic'],data['due_date']))


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True,host='0.0.0.0',port=port)