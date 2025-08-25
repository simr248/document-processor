import os


from groq import Groq
from pydantic import BaseModel

import json
from services.prompt import adhaar_prompt
from services.prompt import Pan_prompt
from services.prompt import Invoice_prompt
from services.prompt import Driving_license_prompt
from services.prompt import Electricity_bill_prompt
from services.prompt import Birth_certificate_prompt
from dotenv import load_dotenv

load_dotenv()
class DocumentRequest(BaseModel):
    document_type: str

class AdhaarInfo(BaseModel):
    name: str 
    dob:str 
    gender:str 
    adhaar_no:str 
    address:str

class panInfo(BaseModel):
    name: str 
    dob:str 
    pan_no:str 
    father_name:str

class drivinglicenceInfo(BaseModel):
    name: str 
    address: str
    issued_date: str
    vehicle_code: str
    dob:str 
    pan_no:str 
    father_name:str

class InvoiceInfo(BaseModel):
    receiver_name: str 
    address: str
    location: str
    pst_code: str
    email:str 
    invoice_no:str 
    order_no:str
    amount: str
    discount: str
    total: str

class electricitybillInfo(BaseModel):
    name: str 
    meter_no: str
    bill_no: str
    connection_details: str
    bill_issued_date:str 
    total_bill:str 
    payment_status:str
    receipt_no: str
    total_units: str
    address: str

class marksheetInfo(BaseModel):
    name: str 
    father_name: str
    dob: str
    name_of_school: str
    marks_obtained:str 
    total_marks:str 
    minimum_marks:str
    grade_point: str
    grade: str
    date: str

class Extraction:
    def __init__(self):
        self.client = Groq()

    async def extract_adhaarcard(self,content):  
            response = self.client.chat.completions.create(
                model="moonshotai/kimi-k2-instruct",
                temperature = 0,
                messages=[
                    {"role": "system", "content": adhaar_prompt},
                    {
                        "role": "user",
                        "content": content,
                    },
                ],
                
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Info",
                        "schema": AdhaarInfo.model_json_schema()
                    }
                }
            )
            review = AdhaarInfo.model_validate(json.loads(response.choices[0].message.content))
          
            return json.dumps(review.model_dump(), indent=2)

    async def extract_pancard(self,content):   
            response = self.client.chat.completions.create(
                model="moonshotai/kimi-k2-instruct",
                temperature = 0,
                messages=[
                    {"role": "system", "content": Pan_prompt},
                    {
                        "role": "user",
                        "content": content,
                    },
                ],
                
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Info",
                        "schema": panInfo.model_json_schema()
                    }
                }
            )
            review = panInfo.model_validate(json.loads(response.choices[0].message.content))
            return json.dumps(review.model_dump(), indent=2)
        
    async def extract_drivinglicence(self,content):   
            response = self.client.chat.completions.create(
                model="moonshotai/kimi-k2-instruct",
                temperature = 0,
                messages=[
                    {"role": "system", "content": Driving_license_prompt},
                    {
                        "role": "user",
                        "content": content,
                    },
                ],
                
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Info",
                        "schema": drivinglicenceInfo.model_json_schema()
                    }
                }
            )
            review = drivinglicenceInfo.model_validate(json.loads(response.choices[0].message.content))
            return json.dumps(review.model_dump(), indent=2)
        
    async def extract_Invoice(self,content):   
            response = self.client.chat.completions.create(
                model="moonshotai/kimi-k2-instruct",
                temperature = 0,
                messages=[
                    {"role": "system", "content": Invoice_prompt},
                    {
                        "role": "user",
                        "content": content,
                    },
                ],
                
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Info",
                        "schema": InvoiceInfo.model_json_schema()
                    }
                }
            )
            review = InvoiceInfo.model_validate(json.loads(response.choices[0].message.content))
            return json.dumps(review.model_dump(), indent=2)

    async def extract_electricitybill(self,content):   
            response = self.client.chat.completions.create(
                model="moonshotai/kimi-k2-instruct",
                temperature = 0,
                messages=[
                    {"role": "system", "content": Electricity_bill_prompt},
                    {
                        "role": "user",
                        "content": content,
                    },
                ],
                
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Info",
                        "schema": electricitybillInfo.model_json_schema()
                    }
                }
            )
            review = electricitybillInfo.model_validate(json.loads(response.choices[0].message.content))
            return json.dumps(review.model_dump(), indent=2)

    async def extract_marksheet(self,content):   
            response = self.client.chat.completions.create(
                model="moonshotai/kimi-k2-instruct",
                temperature = 0,
                messages=[
                    {"role": "system", "content": Birth_certificate_prompt},
                    {
                        "role": "user",
                        "content": content,
                    },
                ],
                
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Info",
                        "schema": marksheetInfo.model_json_schema()
                    }
                }
            )
            review = marksheetInfo.model_validate(json.loads(response.choices[0].message.content))
            return json.dumps(review.model_dump(), indent=2)
    
  