adhaar_prompt = """
From the provided Aadhaar card image or scanned copy, accurately extract all clearly visible important details and return them in a structured JSON format.
Maintain the exact spelling, capitalization, and formatting as they appear on the card.
Do not guess or infer missing information.
Mask sensitive data where appropriate unless explicitly instructed otherwise

"""
Pan_prompt = """
From the provided pan card image or scanned copy, accurately extract all clearly visible important details and return them in a structured JSON format.
Maintain the exact spelling, capitalization, and formatting as they appear on the card.
Do not guess or infer missing information.
Mask sensitive data where appropriate unless explicitly instructed otherwise
.
"""

Driving_license_prompt = """

From the provided driving license image or scanned copy, accurately extract all clearly visible important details and return them in a structured JSON format.
Maintain the exact spelling, capitalization, and formatting as they appear on the card.
Do not guess or infer missing information.
Mask sensitive data where appropriate unless explicitly instructed otherwise
.

"""
Electricity_bill_prompt="""
From the provided electricity bill image or scanned copy, accurately extract all clearly visible important details and return them in a structured JSON format.
Maintain the exact spelling, capitalization, and formatting as they appear on the card.
Do not guess or infer missing information.
Mask sensitive data where appropriate unless explicitly instructed otherwise
.
"""

Invoice_prompt = """
From the provided invoice image or scanned copy, accurately extract all clearly visible important details and return them in a structured JSON format.
Maintain the exact spelling, capitalization, and formatting as they appear on the card.
Do not guess or infer missing information.
Mask sensitive data where appropriate unless explicitly instructed otherwise
.
"""
Birth_certificate_prompt = """
From the provided birth certificate image or scanned copy, accurately extract all clearly visible important details and return them in a structured JSON format.
Maintain the exact spelling, capitalization, and formatting as they appear on the card.
Do not guess or infer missing information.
Mask sensitive data where appropriate unless explicitly instructed otherwise
.
"""

document_prompt = """You are an AI system that classifies uploaded documents into categories .
firstly read the data from document then,
Your task is to:  Identify the document type from the given categories:  
   - Government ID: Aadhaar, PAN, Passport, Driving License, Voter ID  
   - Education Document: Marksheet, Degree, Certificate  
   - Financial Document: Bank Statement, Pay Slip, Invoice, Tax Return  
   - Utility Bill: Electricity, Water, Gas, Mobile, Internet  
   - Medical Document: Prescription, Lab Report, Discharge Summary, Bill  
   - Legal Document: Property Deed, Rental Agreement, Court Order  
   - Personal Document: Resume, Birth Certificate, Marriage Certificate  

Also return the sub categories of the document and few words description(about the document)
"""
