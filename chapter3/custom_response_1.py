from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()

@app.get('/html', response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>FastAPI HTML</title>
            </head>
            <body>
                <h1>Hello World!!!</h1>
            </body>
        </html>
    """

@app.get("/text", response_class=PlainTextResponse)
async def get_plain_text():
    return "Hello World!!!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("custom_response_1:app", host="0.0.0.0", port=5000, reload=True)