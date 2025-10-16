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
