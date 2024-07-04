from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/", description = "This is our first route.", deprecated = True)
async def base_get_route():
    return{"message": "hello world"}

@app.post("/")
async def post():
    return{"message": "Hello from the post route"}

@app.put("/")
async def put():
    return{"message": "hello from the put route"}

@app.get("/users")
async def list_items():
    return{"message":"list users route"}

@app.get("/users/{user_id}")
async def get_item(user_id: str):
    return{"user_id": user_id}

@app.get("/users/me")
async def get_current_user():
    return{"Message": "this is the current user"}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return{"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return{"food_name": food_name,
               "message": "you are still healthy, but like sweet things"}
    return {"food_name": food_name, "message": "I like chocolate milk"}

fake_items_db = [{"item_name":"foo"}, {"item_name":"Bar"}, {"item_name":"Baz"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id:str, sample_query_param:str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "insert some text from the internet"})
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id:int, item_id:str, q:str|None = None, short:bool = False):
    item = {"item_id": item_id, "owner_id":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {
                "description": "insert something from the internet"
            }
        )
    return item

