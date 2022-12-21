from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models.post_model import Post

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments ( content, user_id, post_id ) "
        query += "VALUES ( %(content)s, %(user_id)s, %(post_id)s );"

        return connectToMySQL( DATABASE ).query_db(query, data)

    @classmethod
    def get_all_with_posts(cls): # keep working on this in MySQL - Left Join? Probably move to posts?
        query = "SELECT * "
        query += "FROM comments "
        query += "JOIN posts "
        query += "WHERE comments.post_id = posts.id;"

        results = connectToMySQL( DATABASE ).query_db(query)
        comments = []
        for row in results:
            current_comment = cls(row)
            post_data = {
                **row,
                "created_at": row['posts.created_at'],
                "updated_at": row['posts.updated_at'],
                "id": row['posts.id']
            }
            current_post = Post(post_data)
            current_comment.post = current_post
            comments.append(current_comment)
        return comments

    @staticmethod
    def validate_comment(data):
        is_valid = True

        if len(data['content']) < 1:
            flash("Please leave a comment.", "error_comment_content")
            is_valid = False

        return is_valid