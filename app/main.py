import uvicorn
from fastapi import FastAPI, File, UploadFile
import uuid
import numpy as np
from io import BytesIO
from PIL import Image
import os


IMAGEDIR = "cache"

app = FastAPI()


@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!
    #save_path = os.path.join(IMAGEDIR, file.filename)
    im = Image.open(BytesIO(contents))
    # calculate the golden face ration
    ratio = 0.5
    return {"ratio": ratio}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    uvicorn.run(app, host="0.0.0.0", port=port)