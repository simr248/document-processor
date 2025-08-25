import PyPDF2
import docx
from PIL import Image
from PIL import Image
from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
client = genai.Client()

class TextExtractor:
    def __init__(self):
        pass

    
    async def extract_text(self,file_path: str) -> str:

        if file_path.endswith(".pdf"):
            text = ""
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""
            return text

        elif file_path.endswith(".docx"):
            doc_obj = docx.Document(file_path)
            return "\n".join([p.text for p in doc_obj.paragraphs])
        
        elif file_path.endswith(".txt"):
            with open(file_path,"r",encoding="utf-8") as f:
                text = f.read()
            return text 
        
        # elif file_path.endswith(".jpg"):
        #      with open(file_path,"r",encoding="utf-8") as f:
        #         text = f.read()
        #      return text 
        
        elif file_path.endswith(".png") or file_path.endswith(".jpg"):
            print("-----------------------------")
            image = Image.open(file_path)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[image, "Extract the complete text from this image and return in markdown format."]
            )
            
           
            return response.text
        else:
            return "Unsupported file format"