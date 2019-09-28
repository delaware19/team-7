from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content =db.Column(db.String(200),nullable=False)
    
    completed = db.Column(db.Integer, default=0)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<task %r>' % self.id

@app.route('/', methods=['POST','GET'])

def index():
    if request.method =='POST':
       task_content = request.form['content']
       story1_content=request.form['story_item_1']
       story2_content=request.form['story_item_2']
       story3_content=request.form['story_item_3']
       link_content=request.form['link']
       
       
       new_task = Todo(content=task_content,)
       new_story1=Todo(content=story1_content)
       new_story2=Todo(content=story2_content)
       new_story3=Todo(content=story3_content)
       new_link=Todo(content=link_content)
       
    
       
       
       try:
         db.session.add(new_task)
         db.session.commit()
         db.session.add(new_story1)
         db.session.commit()
         db.session.add(new_story2)
         db.session.commit()
         db.session.add(new_story3)
         db.session.commit()
         db.session.add(new_link)
         db.session.commit()
         
         db.session.commit()
         return redirect('/')
       except:
         return 'there was an issue'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
        
        
        
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    
    try:    
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem in that task'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task=Todo.query.get_or_404(id)
    if request.method == 'POST':
        try:    
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem in that task' 
    else: 
        return render_template('update.html', task=task)           
                       
        
if __name__=="__main__":
    app.run(debug=True)