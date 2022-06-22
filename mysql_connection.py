import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.cx39lhwqkwwy.ap-northeast-2.rds.amazonaws.com',
        database = 'movie_api_db',
        user = 'movie_user',
        password = '123hello7',
    )
    return connection








