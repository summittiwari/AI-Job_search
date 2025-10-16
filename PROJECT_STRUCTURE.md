# AI Powered Job Search Engine - Project Structure

This document provides an overview of the project structure, explaining the purpose of each folder and file in the AI Powered Job Search Engine application.

## Root Level Files

### docker-compose.yml
- **Purpose**: Defines and orchestrates the multi-container Docker application.
- **Functionality**: Sets up three services:
  - `backend`: Flask API server running on port 5000.
  - `frontend`: React application running on port 5173.
  - `db`: PostgreSQL database running on port 5432.
- **Volumes**: Mounts local directories for development hot-reloading.
- **Environment**: Configures development environment variables.

## Backend/
Contains the Flask-based backend API for the job search engine.

### app.py
- **Purpose**: Main entry point for the Flask application.
- **Functionality**: Initializes the Flask app and defines a basic home route that returns a status message indicating the backend is running.

### ai/
- **Purpose**: Directory for AI-related functionality.
- **Functionality**: Likely contains modules for AI-powered job matching, recommendations, or natural language processing features.

### models/
- **Purpose**: Database models and possibly machine learning models.
- **Functionality**: Defines data structures for jobs, users, and other entities. May also include trained ML models for job analysis.

### routes/
- **Purpose**: API route definitions.
- **Functionality**: Contains Flask blueprints or route handlers for various API endpoints like job search, user management, etc.

### scrapers/
- **Purpose**: Web scraping modules.
- **Functionality**: Scripts to scrape job listings from various job boards, company websites, and other sources to populate the job database.

### vectors/
- **Purpose**: Vector-related functionality.
- **Functionality**: Likely handles vector embeddings for jobs and user profiles, enabling semantic search and AI-powered matching.

## database/
Contains database-related files and configurations.

### schema.sql
- **Purpose**: Database schema definition.
- **Functionality**: Defines the structure of the database, including tables like `jobs` with fields for title, description, company, location, and posted date.

### migrations/
- **Purpose**: Database migration scripts.
- **Functionality**: Contains SQL scripts for evolving the database schema over time. Currently empty, indicating the project is in early stages.

## Frontend/
Contains the React-based frontend application built with Vite.

### package.json
- **Purpose**: Node.js project configuration and dependencies.
- **Functionality**: Defines scripts for development (`dev`), building (`build`), linting (`lint`), and previewing (`preview`). Lists React and Vite as main dependencies, along with development tools like ESLint.

### vite.config.js
- **Purpose**: Vite build tool configuration.
- **Functionality**: Configures the Vite development server and build process, including the React plugin for fast refresh.

### index.html
- **Purpose**: Main HTML template.
- **Functionality**: The entry point HTML file that loads the React application. Includes meta tags, title, and script tag for the main JavaScript bundle.

### README.md
- **Purpose**: Documentation for the frontend.
- **Functionality**: Provides information about the Vite + React template, including available plugins and configuration options.

### public/
- **Purpose**: Static assets served directly.
- **Functionality**: Contains public files like `vite.svg` that can be accessed via URL.

### src/
Contains the source code for the React application.

#### main.jsx
- **Purpose**: Application entry point.
- **Functionality**: Renders the React app into the DOM, wrapping it in StrictMode for development warnings.

#### App.jsx
- **Purpose**: Main React component.
- **Functionality**: The root component of the application. Currently contains a basic Vite + React template with logos and a counter example.

#### App.css
- **Purpose**: Styles for the main App component.
- **Functionality**: CSS styles specific to the App component.

#### index.css
- **Purpose**: Global styles.
- **Functionality**: Global CSS styles applied to the entire application.

#### assets/
- **Purpose**: Static assets like images and icons.
- **Functionality**: Contains `react.svg` logo used in the application.

### .gitignore
- **Purpose**: Git ignore rules.
- **Functionality**: Specifies files and directories to exclude from version control, such as node_modules and build outputs.

### eslint.config.js
- **Purpose**: ESLint configuration.
- **Functionality**: Configures linting rules for JavaScript and React code to maintain code quality.







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
