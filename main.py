from fastapi import FastAPI # Import FastAPI from the fastapi module
from typing import Optional # Import Optional from typing for optional parameters
from pydantic import BaseModel # Import BaseModel from pydantic for data validation
import uvicorn # Import uvicorn for running the FastAPI application

app = FastAPI() # Create an instance of FastAPI

@app.get('/') # Define a home route for the root URL
def index():
    return {'data':{'name':'Kshitiz','last_name':'rao'}} # Return a JSON response with name and last name

@app.get('/blog')
def rao(limit = 10,published:bool = True, sort:Optional[str] = None):
    if published:
        return {'data': f'limit of published blogs is {limit} and is {published}'}
    else:
        return {'data': f'limit of blogs is {limit} and is {published}'}


@app.get('/blog/published')
def published():
    return {'data': 'unpublished blogs'}

@app.get('/blog/{id}')
def show(id):
    return {'data':{'blog_id':id}} # Define a route for showing a blog post by its ID


@app.get('/blog/{id}/comments')
def show_comment(id: int):
    return {'data':{'blog_id':id, 'comments':['comment1', 'comment2']}}

@app.get('/peter')
def cat():
    return {'cat_data':{'name':'jhongdu'}} # Define a route for the about page




class Blog(BaseModel): # Define a Pydantic model for blog data
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog') # Define a route for creating a new blog post
def create_blog(blog : Blog):
    return {'data': f'blog created and title is {blog.title} and body is {blog.body} and published is {blog.published}'}    

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8080) # Run the FastAPI application using uvicorn
