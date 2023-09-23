from flask_app import app
from flask import request, session, redirect, render_template
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


# process new recipe
@app.route("/process_recipe", methods=['POST'])
def process_recipe():
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "cooked_date" : request.form['cooked_date'],
        "can_be_cooked_in_30mins" : request.form['can_be_cooked_in_30mins'],
        "user_id": session['user_id']
    }
    Recipe.save(data)
    return redirect('/recipes')



# All posted recipes
@app.route("/recipes")
def recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    # withrecipes=User.get_user_with_recipes(data)
    # print(withrecipes)
    return render_template("recipe.html", user = User.get_user_by_id(data),all_recipes= Recipe.get_all_recipes_with_users())

# create new recipe form
@app.route("/recipes/new")
def new_recipe():
    return render_template("recipe_form.html")


# create edit recipe form
@app.route("/recipes/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    data={
        'id' : recipe_id
    }
    return render_template("edit_recipe.html", details =Recipe.get_one_recipe(data))



# process recipe update
@app.route("/process_update", methods=['POST'])
def process_update():
    data = {
        "id":request.form['id'],
        "name":request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "can_be_cooked_in_30mins": request.form['can_be_cooked_in_30mins'],
        "cooked_date": request.form['cooked_date']
    }
    Recipe.update_recipe(data)
    return redirect('/recipes')

#  details of a specific recipe
@app.route("/recipes/details/<int:recipe_id>")
def recipe_details(recipe_id):
    data = {
        'id': recipe_id
    }
    return render_template("recipe_details.html", details= Recipe.get_one_recipe_with_creator(data))


# process recipe update
@app.route("/recipes/destroy/<int:recipe_id>")
def destroy_recipe(recipe_id):
    data ={
        'id' : recipe_id
    }
    Recipe.destroy_recipe(data)
    return redirect('/recipes')

