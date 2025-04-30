# {{cookiecutter.project_name}}

A FastAPI application template with machine learning capabilities.

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize and update submodules:
```bash
git submodule init
git submodule update
```

## Running the Application

To run the application, use the following command:

```bash
uvicorn {{cookiecutter.project_slug}}.main:app --reload
```

The application will be available at:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative API Documentation: http://localhost:8000/redoc

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint

## Development

This is a FastAPI application with the following features:
- CORS middleware enabled
- Automatic API documentation
- Basic health check endpoint
- Integrated machine learning capabilities through the glowing-giggle submodule 