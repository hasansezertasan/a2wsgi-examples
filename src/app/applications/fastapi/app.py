from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get(path="/")
async def index() -> dict[str, str]:
    return {
        "message": "Hello FastAPI",
    }


@app.post(path="/cookie")
async def set_cookie(req: Request, res: Response) -> dict[str, str]:
    res.set_cookie(key="application", value="fastapi")
    return {"message": "Cookie set"}


@app.get(path="/cookie")
async def get_cookie(req: Request, res: Response) -> dict[str, str | None]:
    return {"message": req.cookies.get("application")}


@app.delete(path="/cookie")
async def delete_cookie(req: Request, res: Response) -> dict[str, str]:
    res.delete_cookie(key="application")
    return {"message": "Cookie deleted"}
