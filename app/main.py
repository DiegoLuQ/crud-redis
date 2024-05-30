from fastapi import FastAPI, HTTPException
import redis
import json
from config import settings as sett
app = FastAPI()
redis_client = redis.Redis(host=str(sett.HOST), port=int(sett.PORT), decode_responses=True, db=0)

@app.get('/')
def home():
    print(2380)
    return {"Hola":"REDIS"}

@app.get('/show')
def show_data():
    data = []
    for key in redis_client.keys():
        value = redis_client.get(key)
        data.append((key, json.loads(value)))

    return data

@app.delete('/delete')
async def delete_data(data:str):
    redis_client.delete(data)
    return True


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8081)
