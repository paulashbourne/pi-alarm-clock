#!/usr/bin/env bash
set -e

APP_NAME="web_api"
docker build -t "$APP_NAME" .

APPDIR=/usr/src/"$APP_NAME"

EXTRA=""

if [ ! -z "$1" ]; then
  EXTRA="/bin/bash"
fi

docker run --rm \
  -v "$(pwd)":"$APPDIR" \
  -w "$APPDIR" \
  -p 8000:8000 \
  -it "$APP_NAME" $EXTRA
