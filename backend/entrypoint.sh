#!/bin/bash
export IMPERKA_SECRET_KEY=$(cat /opt/secret_key)
export IMPERKA_PASSWORD=$(cat /opt/password_hash)
export IMPERKA_USERNAME=$(cat /opt/username)

fastapi run app/main.py --port 8000 --reload