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
        self.username = data['username']
        self.about = data['about']
        self.grade_level = data['grade_level']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, password, username, about, grade_level ) "
        query += "VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, %(username)s, %(about)s, %(grade_level)s );"

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
            flash("Your first name must have at least 2 characters.", "error_registration_first_name")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Your last name must have at least 2 characters.", "error_registration_last_name")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!", "error_registration_email")
            is_valid = False
        if len(data['password']) < 8:
            flash("Your password must have at least 8 characters.", "error_registration_password")
            is_valid = False
        else:
            found_num = False
            found_cap = False
            for character in data['password']:
                if character.isdigit():
                    found_num = True
                elif character.isupper():
                    found_cap = True
            if not (found_num and found_cap):
                flash("Your password must contain at least 1 number and 1 uppercase letter.", "error_registration_password")
                is_valid = False
        if data['password'] != data['confirm_pw']:
            flash("Your passwords do not match!", "error_registration_confirm_pw")
            is_valid = False

        return is_valid