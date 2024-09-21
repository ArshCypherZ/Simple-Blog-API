# Simple Blogging API

This is a simple blogging API built using Flask and SQLite. It allows users to create and retrieve blog posts.

## Features

- **Create a new blog post**: Send a `POST` request to add a new blog entry with a title and content.
- **Retrieve all blog posts**: Send a `GET` request to fetch all stored blog entries.

## Requirements

- Python 3.x
- Flask

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install dependencies**:
   ```bash
   pip install Flask
   ```

3. **Run the API**:
   ```bash
   python app.py
   ```

   The server will start at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Create a New Blog Post

- **URL**: `/blog`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "title": "Your Blog Title",
    "content": "Your blog content here."
  }
  ```
- **Response** (201):
  ```json
  {
    "message": "Blog post created successfully!"
  }
  ```

### 2. Retrieve All Blog Posts

- **URL**: `/blog`
- **Method**: `GET`
- **Response** (200):
  ```json
  [
    {
      "id": 1,
      "title": "First Post",
      "content": "This is the content of the first post"
    },
    {
      "id": 2,
      "title": "Second Post",
      "content": "This is the content of the second post"
    }
  ]
  ```

## Testing the API

You can test the API using `curl` or Postman.

### Example with `curl`:

1. **Create a new blog post**:
   ```bash
   curl -X POST http://127.0.0.1:5000/blog -H "Content-Type: application/json" -d '{"title": "First Post", "content": "This is the content of the first post"}'
   ```

2. **Retrieve all blog posts**:
   ```bash
   curl http://127.0.0.1:5000/blog
   ```

## License

This project is licensed under the MIT License.
```
