from flask_app import app
from flask import render_template,redirect


# register  route
@app.route("/")
def register():
    return render_template("register.html")

# login route
@app.route("/login")
def login():
    return render_template("login.html")

# process login
@app.route("/process_login", methods=['POST'])
def process_login():
    return redirect('/recipes')

# process register
@app.route("/process_register", methods=['POST'])
def process_register():
    return redirect('/recipes')


# All posted recipes
@app.route("/recipes")
def recipe():
    return render_template("recipe.html")

# create new recipe form
@app.route("/recipes/new")
def new_recipe():
    return render_template("recipe_form.html")


# create edit recipe form
@app.route("/recipes/edit")
def edit_recipe():
    return render_template("edit_recipe.html")

# process new recipe
@app.route("/process_recipe", methods=['POST'])
def process_recipe():
    return redirect('/recipes')

# process recipe update
@app.route("/process_update", methods=['POST'])
def process_update():
    return redirect('/recipes')

#  details of a specific recipe
@app.route("/recipes/details")
def recipe_details():
    return render_template("recipe_details.html")








