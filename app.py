from fastapi import FastAPI , Form , UploadFile , File
import uvicorn
from services.text_extraction import TextExtractor
from pathlib import Path
from services.summary import generate_summary
from services.extraction import Extraction
from services.document_classification import document_classification
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()


# (Optional) keep CORS permissive in dev if you later open the HTML elsewhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5500", ...] if you run a separate dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)  # create folder if not exists

text_extractor = TextExtractor()
extract_documents = Extraction()
document_classify = document_classification()
@app.get("/health")
async def health():
    return {
        "message": "API is running",
        "version": "0.0.1"
    }



#  Upload file and get summary
@app.post("/upload_file")
async def upload_and_summarize(file: UploadFile = File(...)):
    file_location = UPLOAD_DIR / file.filename

    with open(file_location, "wb") as f:
        contents = await file.read()
        f.write(contents)

    text = await text_extractor.extract_text(str(file_location))
    summary = await generate_summary(text)

    return {
        "filename": file.filename,
        "summary": summary
    }






# Upload document/image and get information
@app.post("/extract")
async def extract_details(file: UploadFile = File(...),document_type:str =Form()):
    file_location = UPLOAD_DIR / file.filename

    with open(file_location, "wb") as f:
        contents = await file.read()
        f.write(contents)

    text = await text_extractor.extract_text(str(file_location))
    if document_type=="adhaar":
        response =await  extract_documents.extract_adhaarcard(text)
        import json
        return json.loads(response)
        
    elif document_type=="pan":
        response =await  extract_documents.extract_pancard(text)
        return json.loads(response)
    
    elif document_type=="marksheet":
        response =await  extract_documents.extract_marksheet(text)
        return json.loads(response)
    
    elif document_type=="electricitybill":
         response =await  extract_documents.extract_electricitybill(text)
         return json.loads(response)
     
    elif document_type=="Invoice":
        response =await  extract_documents.extract_Invoice(text)
        return json.loads(response)
    
    elif document_type=="drivinglicence":
        response =await  extract_documents.extract_drivinglicence(text)
        return json.loads(response)
    
    elif document_type=="passport":
        pass
    else: 
     return response

@app.post("/document_classification")
async def extract_details(file: UploadFile = File(...)):
    file_location = UPLOAD_DIR / file.filename

    with open(file_location, "wb") as f:
        contents = await file.read()
        f.write(contents)
        
    text = await text_extractor.extract_text(str(file_location))
    response = await document_classify.document_classify(text)
    return json.loads(response)
if __name__ == "__main__":
    uvicorn.run("your_script_name:app", host="127.0.0.1", port=8000, reload=True)
    
