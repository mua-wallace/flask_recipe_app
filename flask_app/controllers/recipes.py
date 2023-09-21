from flask_app import app
from flask import request, session, redirect
from flask_app.models.recipe import Recipe


# process new recipe
@app.route("/process_recipe", methods=['POST'])
def process_recipe():
    data = {
        "name" : request.form['name'],
        "desc" : request.form['desc'],
        "instructions" : request.form['instructions'],
        "cooked_date" : request.form['cooked_date'],
        "can_be_cooked_in_30mins" : request.form['can_be_cooked_in_30mins'],
        "user_id": session['user_id']
    }
    Recipe.save(data)
    return redirect('/recipes')