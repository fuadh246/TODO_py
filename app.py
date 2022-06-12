from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from flask import Flask, render_template, request, redirect, url_for,session
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

# cur = mysql.connection.cursor()
# cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
# mysql.connection.commit()
# cur.close()


todo_list = list()
@app.route('/' , methods= ['GET','POST']) # this decorator create the home route
def home():
    if request.method == 'GET':
        return render_template('index.html', title='TODOpy',todo_list=todo_list)
    if request.method == 'POST':
        topic = request.form['topic']
        date_due = request.form['date']
        if topic and date_due != '':
            add_dic(topic,date_due)
            return redirect('/')
        else:
            return render_template('index.html', title='TODOpy',todo_list=todo_list)

def add_dic(topic,date_due):
    todo_list.append((topic,date_due))
    #print(todo_list)


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True,host='0.0.0.0',port=port)