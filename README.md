02-05-2025
Joshua Davis

Allocation Proration Tool
Overview: The Allocation Proration Tool is designed to efficiently distribute a specified allocation among investors based on their historical average investments. It ensures fairness by following proration rules, such as distributing funds proportionally and ensuring no investor exceeds their requested amount. The tool is built using FastAPI for the backend and React with Vite for the frontend.

Features
Backend (Python + FastAPI):
Efficient allocation proration logic.
Exposes a REST API for proration requests and results.

Frontend (React + Vite):
Simple UI to input allocation data and view results.
Displays proration results in a user-friendly format.
Communicates with the FastAPI backend to perform proration calculations.

The proration logic follows these steps:
If the total requested amount is less than or equal to the allocation, all investors receive the requested amount.
If the total requested amount exceeds the allocation, the allocation is distributed proportionally based on each investor's historical average investment.
Ensure no investor receives more than their requested amount.
Any remaining allocation (after capping investors at their requested amounts) is redistributed among investors who are still eligible for more.

Implementation Plan (within timeframe provided)
1. Backend
Implement the core allocation proration function.
Expose the proration functionality via an API endpoint using FastAPI.
Write unit tests to ensure correctness.
2. Frontend
Develop a React-based user interface with a form to input data and a table to display results.
Integrate with the FastAPI backend to perform proration calculations.
Style with TailwindCSS or simple CSS.
3. Packaging
Provide a run.sh script to simplify the setup process, starting both the frontend and backend servers.

Step 1: Backend Setup
1. Install the required dependencies:
2. cd backend
3. pip install -r requirements.txt
4. start backend server: uvicorn main:app --reload

Step 2: Frontend Setup
1. cd frontend
2. npm install
3. start frontend server: npm run dev

React frontend will be available at **http://localhost:5173

Step 3: 
1. start front and backend with - bash run.sh

Step 4: 
1. Test backend: **python -m unittest backend/test_proration.py
