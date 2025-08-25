import os


from groq import Groq
from pydantic import BaseModel
import json
from services.prompt import document_prompt
from typing import List
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()
class document_classify(BaseModel):
   category:str =Field(...,description= "This is the category of document")
   sub_category:List =Field(...,description="This is the sub category of the document")
   about:str =Field(...,description="This is about the document")
   
   
class document_classification:
    def __init__(self):
        self.client = Groq()

    async def document_classify(self,content):  
            response = self.client.chat.completions.create(
                model="moonshotai/kimi-k2-instruct",
                temperature = 0,
                messages=[
                    {"role": "system", "content": document_prompt},
                    {
                        "role": "user",
                        "content": content,
                    },
                ],
                
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Info",
                        "schema": document_classify.model_json_schema()
                    }
                }
            )
            review = document_classify.model_validate(json.loads(response.choices[0].message.content))
          
            return json.dumps(review.model_dump(), indent=2)

