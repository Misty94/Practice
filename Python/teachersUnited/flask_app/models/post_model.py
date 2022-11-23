from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
        query += "WHERE posts.user_id = users.id;"

        results = connectToMySQL( DATABASE ).query_db(query)
        print (results)
        
        posts = []
        for post in results:
            posts.append(cls(post))
        return posts