from pydantic import BaseModel, Field
from typing import List

class ScreeningEvaluationItem(BaseModel):
    expected_skills: List[str] = Field(
        default_factory=list,
        description="List of skills or knowledge areas expected to be mentioned in the answer"
    )
    evaluation: str = Field(
        ...,
        description="Overall evaluation of the answer (e.g., 'full match', 'partial match', or 'not match')"
    )
    notes: str = Field(
        ...,
        description="Detailed reasoning that explains how the candidate's answer compares with the expected skills and their CV"
    )

class ScreeningEvaluation(BaseModel):
    screening_evaluations: List[ScreeningEvaluationItem] = Field(
        default_factory=list,
        description="List of evaluations for each screening question"
    )