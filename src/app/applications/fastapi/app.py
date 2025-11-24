from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get("/")
async def index():
    return {
        "message": "Hello FastAPI",
    }


@app.post("/cookie")
async def set_cookie(req: Request, res: Response):
    res.set_cookie(key="application", value="fastapi")
    return {"message": "Cookie set"}


@app.get("/cookie")
async def get_cookie(req: Request, res: Response):
    return {"message": req.cookies.get("application")}


@app.delete("/cookie")
async def delete_cookie(req: Request, res: Response):
    res.delete_cookie(key="application")
    return {"message": "Cookie deleted"}
