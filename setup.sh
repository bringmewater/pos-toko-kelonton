#!/bin/bash

# Create project directories
mkdir -p ./src
mkdir -p ./config
mkdir -p ./logs

# Copy .env.example to .env
if [ -f ./.env.example ]; then
    cp ./.env.example ./.env
else
    echo ".env.example file not found!";
fi

echo "Setup completed successfully!"