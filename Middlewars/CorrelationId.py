import HttpContext
from flask import *
import uuid

def ExtractCorrelationId():
    correaltionIdHeaderFound = request.headers.__contains__("CorrelationId")
    if  correaltionIdHeaderFound:
        HttpContext.ActiveRequest.GetCurrentContext().correlationId = request.headers["CorrelationId"]
    else:
        HttpContext.ActiveRequest.GetCurrentContext().correlationId =  str(uuid.uuid4())