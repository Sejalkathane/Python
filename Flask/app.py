from flask import Flask , render_template , url_for , request , redirect
# Flask -> Creates the Flask application.
# render_template -> Displays HTML pages from the templates folder.
# url_for -> Creates URLs automatically.
# request -> Gets data sent by the user (forms).
# redirect -> Redirects the user to another page.


from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy -> Used to connect Flask with the database.

from datetime import datetime # datetime -> Used to store the current date and time.



app = Flask(__name__)
#  creates your application object. __name__ tells Flask where the app is located, so it can find things like templates and static files later. Think of app as "the whole website."

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
# This line tells Flask ::c "Use SQLite database."
# and  :: "Store it in a file named test.db."
# The three slashes (///) mean the database file is in the current project directory.

db=SQLAlchemy(app)   #This connects SQLAlchemy with your Flask application.

class Todo(db.Model):   # Create a table called Todo.
    id=db.Column(db.Integer, primary_key=True)  #This creates a column named id, which is an integer and the primary key for the table.
    content=db.Column(db.String(200),nullable=False) #Creates another column named content, which is a string with a maximum length of 200 characters. The nullable=False argument means that this column cannot be empty.
    completed=db.Column(db.Integer, default=0) #Creates another column named completed, which is an integer. The default=0 argument means that if no value is provided for this column, it will be set to 0.
    date_created=db.Column(db.DateTime,default=datetime.utcnow) #creates another column named date_created, which is a DateTime. The default=datetime.utcnow argument means that if no value is provided for this column, it will be set to the current date and time.

    def __repr__(self):
       return '<Task %r>' % self.id

# def → Defines a function (method).
# __repr__ → Special Python method called when an object needs a string representation.
# self → Refers to the current object.
#self.id  == Gets the id of the current task.
#%r is an older Python string formatting operator.
    #  It means: Insert the representation (repr()) of the value. == <Task 5>


@app.route('/', methods=['POST','GET']) 
#  this is a decorator that tells Flask what URL should trigger our function
# '/' means Home page.
# GET -> Show the page.
# POST -> Receive data from the form.
def index():
     # If the user submits the form
    if request.method == 'POST':
        # return "Hello, Hii There"
        task_content=request.form['content']  # Get the value entered in the input field named "content".

        new_task =Todo(content=task_content)
        
        try:
            db.session.add(new_task)     # Add the object to the database session.

            db.session.commit()       # Save the changes permanently.

            return redirect('/')        # Reload the home page.

        except:
            return "There was an issue adding your task"             # If an error occurs


    else:
            tasks=Todo.query.order_by(Todo.date_created).all()
            return render_template('index.html',tasks=tasks)
    # return "Hello, World!"



@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task"


@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    # return "Update Page"
    task=Todo.query.get_or_404(id)

    if request.method=='POST':
        task.content =request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem Updating that task"
    else:
       return render_template('update.html' ,task=task)


if __name__=="__main__":
    app.run(debug=True)