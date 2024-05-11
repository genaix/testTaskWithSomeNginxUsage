from pathlib import Path
import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse

app = FastAPI()
favicon_path = Path(__file__).parent.absolute().joinpath("favicon.png")


@app.get("/")
async def read_root():
    await asyncio.sleep(1.0)
    return JSONResponse({"Hello": "World"}, status_code=200)


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path, media_type='image/vnd.microsoft')
