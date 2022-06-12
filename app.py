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
    if request.method == 'GET':
        show_data()
        return render_template('index.html', title='TODOpy',todo_list=todo_list)
    if request.method == 'POST':
        topic = request.form['topic']
        due_date = request.form['date']
        if topic and due_date != '':
            db.tasks.insert_one({'topic': topic, 'due_date': due_date})
            show_data()
            return redirect('/')
        else:
            show_data()
            return render_template('index.html', title='TODOpy',todo_list=todo_list)

def show_data():
    collection = db['tasks']
    datas = collection.find({})
    for data in datas:
        todo_list.append((data['topic'],data['due_date']))


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True,host='0.0.0.0',port=port)