import os


from groq import Groq
from pydantic import BaseModel
from dotenv import load_dotenv


import json
load_dotenv()

client = Groq()

class Info(BaseModel):
    summary: str 

async def generate_summary(content):   
    response = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct",
        temperature = 0,
        messages=[
            {"role": "system", "content": "You are expert in summary generation"},
            {
                "role": "user",
                "content": content,
            },
        ],
        
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "Info",
                "schema": Info.model_json_schema()
            }
        }
    )
    review = Info.model_validate(json.loads(response.choices[0].message.content))
    return json.dumps(review.model_dump(), indent=2)