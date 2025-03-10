from pydantic import BaseModel, Field, model_validator
from typing import List, Optional, Union, Any


class ScreeningEvaluationItem(BaseModel):
    expected_skills: List[str] = Field(
        default_factory=list,
        description="List of skills or knowledge areas expected to be mentioned in the answer",
    )
    evaluation: str = Field(
        ...,
        description="Overall evaluation of the answer (e.g., 'full match', 'partial match', or 'not match')",
    )
    notes: str = Field(
        ...,
        description="Detailed reasoning that explains how the candidate's answer compares with the expected skills and their CV",
    )


class ScreeningEvaluation(BaseModel):
    screening_evaluations: Union[List[ScreeningEvaluationItem], List[dict], str, Any] = Field(
        default_factory=list,
        description="List of evaluations for each screening question",
    )
    years_of_experience: int = Field(
        default=0,
        description="Years of experience of the candidate",
    )
    summary: str = Field(
        default="",
        description="Summary of the screening evaluation, mention why the candidate was rejected or accepted",
    )
