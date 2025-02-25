from api.models.candidate import Candidate
from api.services.base_service import BaseService


class ResumeService(BaseService):
    async def parse_resume(self, resume: str) -> str:
        # Bind responseformatter schema as a tool to the model
        model_with_tools = self.model.with_structured_output(Candidate)

        response = await model_with_tools.ainvoke(resume)

        return response
