from flask import Blueprint,render_template,request, redirect, url_for,flash,session
from app import db
from app.models import Task



task_bp = Blueprint('task',__name__,)

@task_bp.route('/')
def view_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('task.html',tasks=tasks)


@task_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
         return redirect(url_for('auth.login'))
    
    title = request.form.get('new_task')
    print("Title : ",title)
    if title:
     new_task =Task(title=title,status="Pending")
    #  status = request.form.get('status')
     db.session.add(new_task)
     db.session.commit()
     flash("Task added Successfully", 'success')
    
    # tasks = Task.query.all()
    return redirect(url_for('task.view_task'))




@task_bp.route('/toggle/<int:task_id>',methods=['GET','POST'])
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == 'Pending':
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Done"
        else:
            task.status = "Pending"  
        
        db.session.commit()
    return redirect(url_for("task.view_task"))     



@task_bp.route("/clear", methods= ["POST"])
def clear_task():
    Task.query.delete()
    db.session.commit()
    flash("All task clear ","info")
    return redirect(url_for("task.view_task")) 


@task_bp.route('/delete/<int:task_id>', methods=['GET','POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully","warning")
    return redirect(url_for("task.view_task"))