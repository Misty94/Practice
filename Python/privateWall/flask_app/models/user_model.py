from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX, DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, password ) "
        query += "VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"

        result = connectToMySQL( DATABASE ).query_db(query, data)
        return result

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE email = %(email)s;"

        result = connectToMySQL( DATABASE ).query_db(query, data)
        if len(result) > 0:
            current_user = cls(result[0])
            return current_user
        else:
            return False

    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query += "FROM users;"

        results = connectToMySQL( DATABASE ).query_db(query)

        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE id = %(id)s;"

        results = connectToMySQL( DATABASE ).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash("Your first name needs to have at least 2 characters!", "error_registration_first_name")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Your last name needs to have at least 2 characters!", "error_registration_last_name")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email", "error_registration_email")
            is_valid = False
        if len(data['password']) < 8:
            flash("Your password must be at least 8 characters long!", "error_registration_password")
            is_valid = False
        if data['password'] != data['password_confirmation']:
            flash("Passwords do not match!", "error_registration_password_confirmation")
            is_valid = False
        
        return is_valid