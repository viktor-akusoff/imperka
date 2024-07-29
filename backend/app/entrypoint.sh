#!/bin/bash
export IMPERKA_SECRET_KEY=$(cat /opt/secret_key)
export IMPERKA_PASSWORD=$(cat /opt/password)
export IMPERKA_USERNAME=$(cat /opt/username)

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --forwarded-allow-ips '*'