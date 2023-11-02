from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/xml")
async def get_xml():
    content = """<?xml version="1.0" encoding="UTF-8"?>
        <Hello>World</Hello>
    """
    return Response(content=content, media_type="application/xml")

if __name__  == "__main__":
    import uvicorn
    uvicorn.run("custom_response_5:app", host="0.0.0.0", port=5000, reload=True)