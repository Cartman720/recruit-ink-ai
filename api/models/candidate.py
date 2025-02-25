from pydantic import BaseModel, Field
from typing import List, Optional


class CandidateInfo(BaseModel):
    name: str = Field(..., description="Candidate's full name")
    title: Optional[str] = Field(
        None, description="Current professional title or headline"
    )
    location: Optional[str] = Field(None, description="Candidate's location")
    email: Optional[str] = Field(None, description="Candidate's email address")
    phone: Optional[str] = Field(None, description="Candidate's phone number")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")
    github: Optional[str] = Field(None, description="GitHub profile URL")
    website: Optional[str] = Field(
        None, description="Personal or portfolio website URL"
    )


class EmploymentEntry(BaseModel):
    position: str = Field(..., description="Job title or position held")
    company: Optional[str] = Field(None, description="Company or organization name")
    location: Optional[str] = Field(None, description="Job location, if mentioned")
    start_date: Optional[str] = Field(
        None, description="Start date (format can be flexible)"
    )
    end_date: Optional[str] = Field(
        None, description="End date or 'Present' if currently employed"
    )
    description: Optional[str] = Field(
        None, description="Summary of responsibilities, key projects, and achievements"
    )


class EducationEntry(BaseModel):
    degree: str = Field(..., description="Degree or certification achieved")
    institution: Optional[str] = Field(None, description="Name of the institution")
    start_date: Optional[str] = Field(None, description="Start date of the program")
    end_date: Optional[str] = Field(None, description="Graduation or completion date")
    description: Optional[str] = Field(None, description="Additional details or honors")


class CertificationEntry(BaseModel):
    name: str = Field(..., description="Certification or credential name")
    issuer: Optional[str] = Field(None, description="Issuing organization")
    date: Optional[str] = Field(
        None, description="Date when the certification was obtained"
    )


class SkillEntry(BaseModel):
    name: str = Field(..., description="Name of the skill")
    level: Optional[str] = Field(
        None,
        description="Optional proficiency level, e.g., Beginner, Intermediate, Advanced, Expert",
    )


class Candidate(BaseModel):
    candidate_info: CandidateInfo = Field(
        ..., description="Basic candidate information"
    )
    professional_summary: Optional[str] = Field(
        None, description="Candidate's professional summary or profile"
    )
    employment_history: List[EmploymentEntry] = Field(
        default_factory=list, description="List of past employment details"
    )
    education: List[EducationEntry] = Field(
        default_factory=list, description="Educational background details"
    )
    skills: List[SkillEntry] = Field(
        default_factory=list,
        description="List of technical and soft skills with optional proficiency levels",
    )
    certifications: List[CertificationEntry] = Field(
        default_factory=list, description="List of professional certifications"
    )
    languages: List[str] = Field(
        default_factory=list, description="Languages spoken or written"
    )
    additional_links: List[str] = Field(
        default_factory=list,
        description="Any additional links (portfolio, projects, publications, etc.)",
    )
