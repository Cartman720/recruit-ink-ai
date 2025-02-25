from io import BytesIO
from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile
from api.lib.helpers import get_model
from api.services.applications_service import ApplicationsService, ScreeningQuestion

router = APIRouter(prefix="/applications", tags=["applications"])


def get_applications_service(provider: str = 'xai', model: str = "grok-2-1212"):
    model = get_model(provider, model)

    return ApplicationsService(model)


@router.post("/parse")
async def parse_application(
    file: UploadFile,
    applications_service: ApplicationsService = Depends(get_applications_service),
):
    """Parse a PDF application and return the content"""

    # Check if the uploaded file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400, detail="Invalid file type. Please upload a PDF file."
        )

    # Read the uploaded PDF file into memory
    try:
        contents = await file.read()
        pdf_stream = BytesIO(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading PDF file: {e}")

    content = await applications_service.extract_pdf_text(pdf_stream)

    return {"content": content}


@router.post("/screen")
async def screen_application(
    description: Annotated[str, Body(embed=True)],
    resume: Annotated[str, Body(embed=True)],
    questions: Annotated[list[ScreeningQuestion], Body(embed=True)],
    applications_service: ApplicationsService = Depends(get_applications_service),
):
    """Screen a PDF application and return the content"""

    res = await applications_service.screen(description, resume, questions)

    return res
