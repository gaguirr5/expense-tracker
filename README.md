# Expense Tracker

A budgeting and forecasting API with income/expense tracking, CSV import, and spending analytics.

---

## Features

- **Authentication** — JWT-based sessions, bcrypt password hashing
- **Income & Expense Tracking** — full CRUD, with support for recurring items
- **CSV Import** — bulk-import transactions from bank statement exports
- **Spending Summaries** — aggregated by category and time period
- **Forecasting** — 12-month balance projection based on recurring income/expenses
- **Interactive Dashboard** — charts and data entry via Streamlit

## Tech Stack

**Backend:** FastAPI (Python)
**Database:** PostgreSQL + SQLAlchemy
**Auth:** JWT + passlib (bcrypt)
**Data processing:** pandas
**Dashboard:** Streamlit
**Testing:** pytest
**Infrastructure:** Docker · GitHub Actions · Render

## Architecture

The backend follows a layered API → Service → Repository structure, with the service layer depending on repositories via dependency injection — making business logic fully unit-testable in isolation, without a real database connection.

## Getting Started

### Prerequisites
- Python 3.12+
- PostgreSQL (local or hosted)

### Installation

```bash
git clone https://github.com/gaguirr5/expense-tracker.git
cd expense-tracker
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
# source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

Create a `.env` file:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/expense_tracker
JWT_SECRET=a_long_random_string
```

### Running

```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` for interactive API documentation.

## Testing

```bash
pytest
```

## Docker

```bash
docker build -t expense-tracker .
docker run -p 8000:8000 --env-file .env expense-tracker
```