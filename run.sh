#!/bin/bash

# Backend setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload &

# Frontend setup
cd ../frontend
npm install
npm run dev