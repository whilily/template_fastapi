from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi import FastAPI

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return '''
    <!DOCTYPE html>
    
    <head>
    <title>Hello World!</title>
    </head>

    <body>
    <h2>Wonderful Website!</h2>
    </body>
    
    </html>
    '''

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}
