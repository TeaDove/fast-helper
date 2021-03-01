from fastapi import FastAPI, Request, Response


tags_metadata = [
    {
        "name": "root",
        "description": "return Hello World",
    },
    {
        "name": "ip",
        "description": "return your IPv4"
    },
]

app = FastAPI(title="Fast-helper",
    description="This is very small pet-project without normal description",
    version="0.0.1",
    openapi_tags=tags_metadata)



@app.get("/", tags=['root'])
async def read_root():
    return {"Hello": "World"}


@app.get("/ip", tags=['ip'])
async def read_ip(request: Request):
    return Response(content = request.client.host)
