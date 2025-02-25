from api.models.jobs import JobPosting
from api.services.base_service import BaseService


class JobsService(BaseService):
    async def parse_job_posting(self, job_description: str) -> str:
        # Bind responseformatter schema as a tool to the model
        model_with_tools = self.model.with_structured_output(JobPosting)

        response = await model_with_tools.ainvoke(job_description)

        return response
