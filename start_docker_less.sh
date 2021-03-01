#!/bin/bash

cd src/app
uvicorn main:app --host localhost --reload --port 8000
