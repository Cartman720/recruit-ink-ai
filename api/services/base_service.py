from langchain_xai import ChatXAI


class BaseService:
    def __init__(self, model: ChatXAI | None = None):
        if model is None:
            self.model = ChatXAI(model="grok-2-1212")
        else:
            self.model = model
