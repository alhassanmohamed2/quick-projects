from flask import Flask,render_template, request,json,redirect
import sqlite3 
import json

app = Flask(__name__)

@app.route("/" )
def home():
    return render_template("index.html")

@app.route("/chat_update", methods=['POST'])
def chat_update():
    connection = sqlite3.connect("data.sqlite") 
    data_array = connection.execute("select * from msg").fetchall()
    connection.commit()
    connection.close() 
    return render_template("chat.html",data_array=data_array)




@app.route('/send', methods=['POST'])
def send():
    msg =  request.form['msg']
    connection = sqlite3.connect("data.sqlite") 
    connection.execute(f'INSERT INTO msg(msg) VALUES("{msg}")')
    connection.commit()
    connection.close()
    return json.dumps({'status':'OK','msg':msg})



@app.route('/delete', methods=['POST'])
def delete():
    connection = sqlite3.connect("data.sqlite") 
    connection.execute("DELETE FROM msg")
    connection.commit()
    connection.close()
    return json.dumps({'status':'OK'})
     



if __name__ == "__main__":
    app.run(debug=True)