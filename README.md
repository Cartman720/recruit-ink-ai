# Recruit-Ink AI

A modern FastAPI-based application for automated resume parsing and candidate screening using AI.

## Overview

Recruit-Ink AI is designed to streamline the recruitment process by providing tools to:

- Parse resumes from PDF files
- Screen applications against job descriptions
- Evaluate candidate responses to screening questions

The application leverages LLMs (particularly Grok-2) to analyze resumes and job descriptions, providing intelligent matching and screening capabilities.

## Features

- **PDF Resume Parsing**: Extract text from PDF resumes
- **Job-Resume Matching**: Compare resumes against job descriptions
- **Candidate Screening**: Evaluate candidate responses to screening questions
- **AI-Powered Analysis**: Leverage state-of-the-art language models for intelligent screening
- **Multi-Model Support**: Dynamic model selection between different providers (XAI, OpenAI) via query parameters
- **Model Flexibility**: Use the `get_model` helper to switch between AI providers and models at runtime

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.13
- **Package Management**: Poetry
- **AI Models**: LangChain integration with Grok-2 and other models
- **PDF Processing**: PyPDF2
- **Deployment**: Docker containerization
- **CI/CD**: GitHub Actions

## Getting Started

### Prerequisites

- Python 3.13+
- Poetry 2.1+
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cartman720/recruit-ink-ai.git
   cd recruit-ink-ai
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Set up environment variables by creating a `.env` file:
   ```
   XAI_API_KEY=your_xai_api_key
   PORT=8000
   ```

### Running Locally

1. Activate the Poetry environment:
   ```bash
   poetry shell
   ```

2. Start the FastAPI server:
   ```bash
   python -m api.main
   ```

3. The API will be available at `http://localhost:8000`

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t recruit-ink-ai .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 --env-file .env recruit-ink-ai
   ```

## API Endpoints

### Health Check
```
GET /health
```
Returns the service status.

### Parse Application
```
POST /applications/parse
```
Upload a PDF resume to extract its contents.

### Screen Application
```
POST /applications/screen
```
Screen a resume against a job description with optional screening questions.

#### Model Selection
All API endpoints support dynamic model selection via query parameters:
- `provider`: AI provider to use (default: "xai", options: "xai", "openai")
- `model`: Specific model to use (default: "grok-2-1212")

Example:
```
POST /applications/screen?provider=openai&model=gpt-4
```

## Development

### Project Structure

- `api/`: Main application package
  - `main.py`: Application entry point
  - `config.py`: Configuration management
  - `routers/`: API route definitions
  - `services/`: Business logic services
  - `models/`: Data models and schemas
  - `lib/`: Helper utilities
    - `helpers.py`: Contains utility functions including `get_model` for AI provider selection

### Testing

Run tests with:
```bash
poetry run pytest
```

## Author

- **Aren Hovsepyan** - *Project Creator and Maintainer*

## License

This project is licensed under the MIT License with Attribution.

Copyright (c) 2025 Aren Hovsepyan

Permission is granted to use this software under the condition that proper attribution to Aren Hovsepyan is included in any derivative works or implementations.

See the [LICENSE](LICENSE) file for full details.

## Contributors

- Aren Hovsepyan - Initial work
