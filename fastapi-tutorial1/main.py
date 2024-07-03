from fastapi import FastAPI

app = FastAPI()

@app.get('/', description= "This is our first rout.", deprecated = True)
async def base_get_route():
    return{"message": "hello world"}

@app.post("/")
async def post():
    return{"message": "Hello from the post route"}

@app.put("/")
async def put():
    return{"message": "Hello from the put route"}