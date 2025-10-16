-- SQL schema for AI Job Platform

-- Example table
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    company TEXT,
    location TEXT,
    posted_date DATE
);
