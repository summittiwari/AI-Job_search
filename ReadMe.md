# AI Job Platform

This project is a full-stack AI-powered job search portal with a React (Vite) frontend, Flask backend, and PostgreSQL database. It is fully containerized using Docker Compose.

## Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop) and Docker Compose installed
- (Optional) Node.js and Python for local development

## Project Structure
```
Backend/        # Flask backend
Frontend/       # React frontend (Vite)
database/       # SQL schema and migrations
docker-compose.yml
.env            # Environment variables
```

## Quick Start (Docker Compose)
1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd <project-folder>
   ```
2. Set up your `.env` file in the root directory:
   ```
   DATABASE_URL=postgresql://postgres:postgres@db:5432/ai_job_platform
   ```
3. Build and start all services:
   ```
   docker-compose up --build
   ```
4. Access the app:
   - Frontend: http://localhost:5173/
   - Backend:  http://localhost:5000/
   - Database: 5432 (PostgreSQL)

## Local Development (Optional)
### Backend
```
cd Backend
pip install -r requirements.txt  # (create this file as needed)
python app.py
```

### Frontend
```
cd Frontend
npm install
npm run dev
```

## Database
- The database schema is in `database/schema.sql`.
- You can manage the database using pgAdmin or psql.

## Notes
- Make sure ports 5173 (frontend), 5000 (backend), and 5432 (db) are free.
- Update environment variables as needed for production.

---

Feel free to open issues or contribute!
