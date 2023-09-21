from flask_app.config.mysqlconnection import connectToMySQL


class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.desc = data["desc"]
        self.instructions = data["instructions"]
        self.cooked_date = data["cooked_date"]
        self.can_be_cooked_in_30mins = data["can_be_cooked_in_30mins"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes(name, desc, instructions, cooked_date, can_be_cooked_in_30mins, user_id) VALUES (%(name)s, %(desc)s, %(instructions)s, %(cooked_date)s ,%(can_be_cooked_in_30mins)s, %(user_id)s);"
        return connectToMySQL("recipe").query_db(query, data)
