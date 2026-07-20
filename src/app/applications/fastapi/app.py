"""FastAPI example application."""

from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get(path="/")
async def index() -> dict[str, str]:
    """Handle FastAPI request.

    Returns:
        dict[str, str]: The response to be sent back.
    """
    return {
        "message": "Hello fastapi",
    }


@app.post(path="/cookie")
async def set_cookie(req: Request, res: Response) -> dict[str, str]:
    """Set a cookie and return a confirmation message.

    Returns:
        dict[str, str]: The response to be sent back.
    """
    res.set_cookie(key="application", value="fastapi")
    return {"message": "Cookie set"}


@app.get(path="/cookie")
async def get_cookie(req: Request, res: Response) -> dict[str, str | None]:
    """Return the value of the ``application`` cookie.

    Returns:
        dict[str, str | None]: The response to be sent back.
    """
    return {"message": req.cookies.get("application")}


@app.delete(path="/cookie")
async def delete_cookie(req: Request, res: Response) -> dict[str, str]:
    """Delete the cookie and return a confirmation message.

    Returns:
        dict[str, str]: The response to be sent back.
    """
    res.delete_cookie(key="application")
    return {"message": "Cookie deleted"}
