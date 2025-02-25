from io import BytesIO
from PyPDF2 import PdfReader
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from langchain_xai import ChatXAI
from pydantic import BaseModel
import asyncio

from api.models.screening_question import ScreeningEvaluation
from api.services.base_service import BaseService
from api.services.jobs_service import JobsService
from api.services.resume_service import ResumeService


class ScreeningQuestion(BaseModel):
    question: str
    answer: str


class ApplicationsService(BaseService):
    async def extract_pdf_text(self, pdf_stream: BytesIO) -> str:
        """Extract text from a PDF file stream"""
        extracted_text = ""
        try:
            reader = PdfReader(pdf_stream)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text
            return extracted_text
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading PDF file: {e}")

    async def screen(
        self, description: str, resume: str, questions: list[ScreeningQuestion]
    ):
        """Screen a resume against a job description and return the results"""

        jobs_service = JobsService(self.model)
        resume_service = ResumeService(self.model)

        # Run both parsing operations concurrently
        job_analysis, resume_analysis = await asyncio.gather(
            jobs_service.parse_job_posting(description),
            resume_service.parse_resume(resume),
        )

        model_with_tools = self.model.with_structured_output(ScreeningEvaluation)

        json_job_analysis = jsonable_encoder(job_analysis)
        json_resume_analysis = jsonable_encoder(resume_analysis)

        answers = await model_with_tools.ainvoke(
            f"""
                **Detailed Reasoning:**  
                Provide a clear, concise explanation for your evaluation. 
                Mention which expected skills were present, which were missing, and any additional context that supports your conclusion.  

                Job description: {json_job_analysis}
                Resume: {json_resume_analysis}
                Questions: {questions}
            """
        )

        return {
            "answers": jsonable_encoder(answers),
        }
