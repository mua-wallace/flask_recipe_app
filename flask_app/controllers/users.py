from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect, request,session, flash

from flask_app.models.user import User

bcrypt = Bcrypt(app)
# register  route
@app.route("/")
def register():
    return render_template("register.html")

# login route
@app.route("/login")
def login():
    return render_template("login.html")

# logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# process login
@app.route("/process_login", methods=['POST'])
def process_login():
    data = {
        "email" : request.form['email']
    }
    user = User.get_user_by_email(data)
    if not user:
        flash("Invalid credentials", 'login')
        return redirect('/login')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid credentials", 'login')
        return redirect('/login')
    
    session['user_id'] = user.id
    
    return redirect('/recipes')

# process register
@app.route("/process_register", methods=['POST'])
def process_register():
    if not User.validate_user(request.form):
        # redirect to the route where the user form is rendered.
        return redirect('/')
    # hashing user password using bcrypt
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": hashed_pw
    }
    id = User.save(data)
    # save userId to session
    session['user_id'] = id
    return redirect('/recipes')


# All posted recipes
@app.route("/recipes")
def recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("recipe.html", user = User.get_user_by_id(data))

# create new recipe form
@app.route("/recipes/new")
def new_recipe():
    return render_template("recipe_form.html")


# create edit recipe form
@app.route("/recipes/edit")
def edit_recipe():
    return render_template("edit_recipe.html")



# process recipe update
@app.route("/process_update", methods=['POST'])
def process_update():
    return redirect('/recipes')

#  details of a specific recipe
@app.route("/recipes/details")
def recipe_details():
    return render_template("recipe_details.html")








