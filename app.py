from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS blog_posts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

@app.route('/blog', methods=['POST'])
def add_blog_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO blog_posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()

    return jsonify({"message": "Blog post created successfully!"}), 201

@app.route('/blog', methods=['GET'])
def get_blog_posts():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM blog_posts')
    rows = cursor.fetchall()
    conn.close()

    posts = [{"id": row[0], "title": row[1], "content": row[2]} for row in rows]
    return jsonify(posts)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
