# AI-Job_search

## Overview
An AI-powered job search engine that helps users find relevant job opportunities using advanced matching algorithms and web scraping technologies.

## How to Run the Application

### Prerequisites
- Docker and Docker Compose installed on your system
- Git (for cloning the repository)

### Quick Start with Docker Compose
1. Clone the repository:
   ```bash
   git clone https://github.com/summittiwari/AI-Job_search.git
   cd AI-Job_search
   ```

2. Start the application:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Frontend: http://localhost:80
   - Backend API: http://localhost:5000
   - Database: localhost:5432 (PostgreSQL)

### Manual Setup (Alternative)

#### Backend Setup
1. Navigate to the Backend directory:
   ```bash
   cd Backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables (create a `.env` file):
   ```
   FLASK_ENV=development
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ai_job_platform
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

#### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

#### Database Setup
1. Install PostgreSQL locally or use Docker:
   ```bash
   docker run --name postgres-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=ai_job_platform -p 5432:5432 -d postgres:15
   ```

2. Run the schema:
   ```bash
   psql -h localhost -U postgres -d ai_job_platform -f database/schema.sql
   ```

## Project Structure
See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed information about the codebase organization.

## Contributing

This repository is **public** and open for contributions! Anyone can view, fork, and contribute to the project.

### How to Contribute
1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your commit message"
   ```
4. Push to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request (PR) on the main repository with a clear description of your changes.

### Guidelines
- Follow the existing code style and project structure.
- Test your changes thoroughly.
- Update documentation if necessary.
- Be respectful and collaborative in discussions.

For major changes, please open an issue first to discuss what you would like to change.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: React (with Vite)
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **AI/ML**: Vector embeddings for job matching
