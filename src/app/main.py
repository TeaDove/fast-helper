from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/ip")
async def response(request: Request):
    return Response(content = request.client.host)
