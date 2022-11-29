from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.user_model import User
from flask import flash
# from datetime import datetime
# import math

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # def time_span(self):
    #     now = datetime.now()
    #     delta 

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts ( title, content, user_id ) "
        query += "VALUES ( %(title)s, %(content)s, %(user_id)s );"

        return connectToMySQL( DATABASE ).query_db(query, data)

    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * "
        query += "FROM posts "
        query += "JOIN users "
        query += "WHERE posts.user_id = users.id "
        query += "ORDER BY posts.created_at DESC;"

        results = connectToMySQL( DATABASE ).query_db(query)
        # print (results)
        posts = []
        for row in results:
            current_post = cls(row)
            user_data = {
                **row,
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at'],
                "id": row['users.id']
            }
            current_user = User(user_data)
            current_post.user = current_user
            posts.append(current_post)
        return posts

    @staticmethod
    def validate_post(data):
        is_valid = True

        if len(data['title']) < 2:
            flash("You must have a title with at least 2 characters.", "error_post_title")
            is_valid = False
        if len(data['content']) < 5:
            flash("Your post must contain at least 5 characters.", "error_post_content")
            is_valid = False
        
        return is_valid