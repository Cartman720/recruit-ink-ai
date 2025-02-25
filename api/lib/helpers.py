import importlib
import pkgutil

from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_xai import ChatXAI


# Auto-discover routers dynamically
def register_routers(app: FastAPI):
    package = "api.routers"
    for _, module_name, _ in pkgutil.iter_modules([package.replace(".", "/")]):
        module = importlib.import_module(f"{package}.{module_name}")
        if hasattr(module, "router"):  # Ensure module has a `router` object
            app.include_router(module.router)
            
def get_model(provider: str, model: str = "grok-2-1212"):
    """Get a model based on the provider and model"""
    
    if provider == "openai":
        return ChatOpenAI(model=model) 
    elif provider == "xai":
        return ChatXAI(model=model)
    
    return ChatOpenAI(model=model) 
