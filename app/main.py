import uvicorn
from fastapi import FastAPI, File, UploadFile
import uuid
import os


IMAGEDIR = "cache"
os.makedirs(IMAGEDIR, exist_ok=True)

app = FastAPI()


@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!
    save_path = os.path.join(IMAGEDIR, file.filename)
    # example of how you can save the file
    with open(save_path, "wb") as f:
        f.write(contents)

    return {"filename": file.filename}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)