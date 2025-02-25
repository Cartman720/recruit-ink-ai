from pydantic import BaseModel, Field
from typing import List, Optional


class JobDetail(BaseModel):
    title: Optional[str] = Field(None, description="The job title, if available.")
    company: Optional[str] = Field(None, description="The company name, if mentioned.")
    location: Optional[str] = Field(None, description="The job location, if mentioned.")
    employment_type: Optional[str] = Field(
        None, description="Employment type (e.g., full-time, part-time)."
    )
    description: Optional[str] = Field(
        None, description="A brief summary of the job description."
    )


class Requirement(BaseModel):
    requirement: str = Field(
        ..., description="A key requirement or qualification from the job description."
    )
    level: str = Field(
        ...,
        description="Level of the requirement, e.g., 'Experienced', 'Familiarity', 'Certifications'.",
    )


class JobPosting(BaseModel):
    """
    Always use this tool to structure your response to the user.
    Do not deviate from this schema.
    """

    job_details: JobDetail = Field(
        ..., description="General details extracted from the job description."
    )
    key_requirements: List[Requirement] = Field(
        ..., description="List of key requirements (experienced, familairty, etc)."
    )
    nice_to_haves: List[str] = Field(
        ..., description="List of additional nice-to-have qualifications."
    )
    special_considerations: List[str] = Field(
        ...,
        description="Special aspects or red flags to pay attention to during the screening process.",
    )
