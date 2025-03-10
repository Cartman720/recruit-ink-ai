from io import BytesIO
from PyPDF2 import PdfReader
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from api.models.screening_question import ScreeningEvaluation
from api.services.base_service import BaseService


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
        self,
        description: str,
        resume: str,
        questions: list[ScreeningQuestion] = None,
    ):
        """Screen a resume against a job description and return the results"""

        model_with_tools = self.model.with_structured_output(ScreeningEvaluation)

        answers = await model_with_tools.ainvoke(
            f"""
                You're tasked with evaluating a candidate's resume against the provided job description. Provide a clear and concise assessment, following these guidelines:

                ### Evaluation Instructions:
                1. **Relevance and Experience:**
                - Analyze the resume carefully against the job description.
                - Verify that experience aligns closely with required responsibilities and skills.
                - Ensure the years of experience meet the job's stated criteria.

                2. **Flag Analysis:**
                - Pay special attention to yellow or red flags, such as gaps, inconsistencies, frequent job changes, or unclear descriptions.
                - Highlight if the language or structure of the resume seems overly embellished, exaggerated, generic, or potentially AI-generated.

                3. **Candidate Fit Assessment:**
                - Clearly assess if the candidate's background matches the role based solely on provided information.

                3. **Screen for Authenticity:**
                - Be cautious of overly generic language or buzzwords that lack specificity.
                - Highlight any sections that seem suspiciously inflated or vague, as these may indicate exaggerated experience.

                ### Decision Guidelines:
                - **Accept** if the candidate meets:
                - Required years of relevant experience
                - Possesses necessary skills clearly outlined in the job description.
                
                - **Reject** if:
                - Skills explicitly required are missing.
                - Insufficient years of relevant experience.
                - Resume appears significantly exaggerated or suspiciously misaligned with typical industry standards.

                ### Detailed Reasoning:
                Provide a concise and specific rationale including:
                - Exact skills and experiences that match the job.
                - Clearly state missing or inadequate skills or experiences.
                - Explicitly mention any concerning or misleading statements.
                - Clearly conclude by recommending acceptance or rejection, explicitly explaining your reasoning.

                This will ensure a thorough, precise, and authentic evaluation aligned with your hiring standards.
                
                Job description: {description}
                Resume: {resume}
                Questions: {questions if questions else "No questions provided"}
            """
        )

        return jsonable_encoder(answers)
