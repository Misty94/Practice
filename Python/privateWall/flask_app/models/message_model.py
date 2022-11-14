from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user_model import User
from datetime import datetime
import math

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user_id = data['user_id']
        self.user = data['user']
        self.friend_id = data['friend_id']
        self.friend = data['friend']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60 )) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60) / 60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages ( content, user_id, friend_id ) "
        query += "VALUES ( %(content)s, %(user_id)s, %(friend_id)s );"

        return connectToMySQL( DATABASE ).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM messages "
        query += "WHERE id = %(id)s;"

        return connectToMySQL( DATABASE ).query_db(query, data)

    @classmethod
    def get_my_messages(cls, data):
        query = "SELECT users.first_name AS user, users2.first_name AS friend, messages.* "
        query += "FROM users LEFT JOIN messages ON users.id = messages.user_id "
        query += "LEFT JOIN users AS users2 ON users2.id = messages.friend_id "
        query += "WHERE users2.id = %(id)s;"

        results = connectToMySQL( DATABASE ).query_db(query, data)
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages

    @staticmethod
    def validate_message(data):
        is_valid = True

        if len(data['content']) < 5:
            flash("Your message should be at least 5 characters long.", "error_message_content")
            is_valid = False

        return is_valid