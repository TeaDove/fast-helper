#!/bin/bash

cd src/app
uvicorn main:app --host tesseract.club --reload --port 8000 --ssl-keyfile /etc/letsencrypt/live/tesseract.club/privkey.pem --ssl-certfile /etc/letsencrypt/live/tesseract.club/cert.pem
