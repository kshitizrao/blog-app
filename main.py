from fastapi import FastAPI

app = FastAPI() # Create an instance of FastAPI

@app.get('/') # Define a home route for the root URL
def index():
    return {'data':{'name':'Kshitiz','last_name':'rao'}} # Return a JSON response with name and last name

@app.get('/peter')
def cat():
    return {'cat_data':{'name':'jhongdu'}} # Define a route for the about page