#!/bin/bash

APP_ENV="${APP_ENV:-dev}"

if [ "$APP_ENV" = "dev" ]; then
    uv run flask --app pps.app:APP run --debug --port=5050
elif [ "$APP_ENV" = "prod" ]; then
    uv run waitress-serve --port=5050 pps.app:APP
else
    echo "Error: Invalid APP_ENV value. Must be 'dev' or 'prod'"
    exit 1
fi