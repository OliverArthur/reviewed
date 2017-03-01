#!/usr/bin/env bash

set -e

echo "Doing 'npm install'..."
# Install NPM dependencies
npm install
echo

# Start the server
echo "Starting the server..."
npm run server

exec "$@"
