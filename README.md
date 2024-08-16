# Monorepo: FastAPI Backend and React Frontend

This monorepo contains both the backend and frontend components of a web application. The backend is built using FastAPI and Python, while the frontend is built using React and JavaScript. Docker is used for containerization, and Poetry and Yarn are used for dependency management.

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your system.
- **Poetry**: Used for Python dependency management.
- **Yarn**: Used for managing frontend dependencies.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/pandey-vaibhav/fastapi-demo.git
   cd fastapi-demo
   ```

2. **Set up the backend**:

   - Navigate to the backend directory:
     ```bash
     cd backend
     ```
   - Install dependencies:
     ```bash
     poetry install
     ```

3. **Set up the frontend**:
   - Navigate to the frontend directory:
     ```bash
     cd ../frontend
     ```
   - Install dependencies:
     ```bash
     yarn install
     ```

### Running the Application

#### Using Docker Compose

You can run the entire application (both frontend and backend) using Docker Compose.

1. **Start the services**:

   ```bash
   docker-compose up --build
   ```

2. **Access the application**:
   - The React frontend will be available at `http://localhost:3000`.
   - The FastAPI backend will be available at `http://localhost:8000`.

#### Running Locally

If you prefer to run the frontend and backend separately without Docker:

1. **Backend**:

   - Navigate to the `backend` directory:
     ```bash
     cd backend
     ```
   - Run the FastAPI application:
     ```bash
     poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
     ```

2. **Frontend**:
   - Navigate to the `frontend` directory:
     ```bash
     cd ../frontend
     ```
   - Start the React application:
     ```bash
     yarn start
     ```

### Testing

#### Backend

- To run backend tests:
  ```bash
  cd backend
  poetry run pytest
  ```
