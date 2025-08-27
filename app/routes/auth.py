from flask import Blueprint, render_template ,request, redirect, url_for,flash,session

auth_bp = Blueprint('auth',__name__)

user_cred = {
     'username': 'admin',
     'password': '1234'
}

@auth_bp.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('pswrd')
        # print(username,password1)
        if username == user_cred['username'] and password == user_cred['password']:
            # session.set('user', username)
            session['user'] = username
            flash('Login Successful','success')
            return redirect(url_for('task.view_task'))
        else:
            flash('invalid user ','danger')    
    return render_template("login.html")

@auth_bp.route('/logout')
def logout():
        session.pop('user',None)
        flash('Logout user ','info')  
        return redirect(url_for('auth.login'))  

@auth_bp.route('/register')
def register():
        return render_template("register.html")  







