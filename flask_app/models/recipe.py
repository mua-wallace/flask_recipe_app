from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.cooked_date = data["cooked_date"]
        self.can_be_cooked_in_30mins = data["can_be_cooked_in_30mins"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes(name, description, instructions, cooked_date, can_be_cooked_in_30mins, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(cooked_date)s ,%(can_be_cooked_in_30mins)s, %(user_id)s);"
        return connectToMySQL("recipe").query_db(query, data)

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        recipes_from_db = connectToMySQL("recipe").query_db(query)
        recipes = []
        for r in recipes_from_db:
            recipes.append(cls(r))
        return recipes

    @classmethod
    def get_all_recipes_with_users(cls):
        query = "SELECT recipes.id, name, description, instructions, cooked_date, can_be_cooked_in_30mins, user_id, recipes.created_at, recipes.updated_at, first_name, last_name, email, password, users.created_at AS uc_at,users.updated_at AS uu_at FROM recipes JOIN users ON recipes.user_id = users.id;"
        
        # Get all recipes alongside their creator's info
        recipes_from_db =  connectToMySQL('recipe').query_db(query)

        # list to hold the objects returned
        recipes =[]

        # iterate through the list returned which is recipes_from_db
        for recipe in recipes_from_db:
            
            # convert each recipe into recipe object
            recipe_obj = cls(recipe)
            
            # convert the joined user data into a user object
            recipe_obj.user = user.User({
                'id' : recipe['user_id'],
                'first_name' : recipe['first_name'],
                'last_name' : recipe['last_name'],
                'email' : recipe['email'],
                'password' : recipe['password'],
                'created_at' : recipe['uc_at'],
                'updated_at' : recipe['uu_at'],
            })
            recipes.append(recipe_obj)
        # return the recipes  list with creator info
        return recipes


    @classmethod
    def get_one_recipe_with_creator(cls, data):
        query = "SELECT recipes.id, name, description, instructions, cooked_date, can_be_cooked_in_30mins, user_id, recipes.created_at, recipes.updated_at, first_name, last_name, email, password, users.created_at AS uc_at,users.updated_at AS uu_at FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        #  # Get a specific recipe alongside their creator's info
        recipe_from_db = connectToMySQL("recipe").query_db(query, data)
        
        result = recipe_from_db[0]
        # convert result into a recipe object
        recipe = cls(result)
        
        # convert joined user data into a user object
        recipe.user = user.User({
            'id': result['user_id'],
            'first_name': result['first_name'],
            'last_name': result['last_name'],
            'email': result['email'],
            'password': result['password'],
            'created_at': result['uc_at'],
            'updated_at': result['uu_at']
        })
        # return the recipe
        return recipe

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        recipe_from_db = connectToMySQL("recipe").query_db(query, data)
        return cls(recipe_from_db[0])

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, can_be_cooked_in_30mins=%(can_be_cooked_in_30mins)s, cooked_date=%(cooked_date)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL("recipe").query_db(query, data)

    @classmethod
    def destroy_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL("recipe").query_db(query, data)
