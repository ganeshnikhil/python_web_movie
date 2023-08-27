from flask import Flask, render_template, request
import csv 
import json 
import ast

app = Flask(__name__)

@app.route('/')
def load_logo():
   return render_template('intro.html')

@app.route('/index', methods=['GET', 'POST'])
def hello_world():
   all_todo=[]
   if request.method=='POST':
      title = request.form['title'].lower().strip()
      with open("films-2-update.csv", 'r') as file:
         
         csv_data = csv.reader(file)
         next(csv_data)
         
         for row in csv_data:
            movie_title=row[1].lower().strip()
            if  title==movie_title:
               all_todo.append([row[1],row[2]])
               break
            
            if  title in movie_title:
               all_todo.append([row[1],row[2]])
               
               
      if len(all_todo)==0:
         all_todo.append(["None","Not Found !"])
         
   return render_template('index.html', allTodo=all_todo)

@app.route('/about')
def about():
   return render_template('about.html')
   

if __name__ == "__main__":
   app.run(debug=True, port=8000)
