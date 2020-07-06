#!/bin/bash


export PROJECT_ROOT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd ${PROJECT_ROOT_PATH}


CREDENTIALS_DIR="${PROJECT_ROOT_PATH}/credentials"
BOT_DIR="${PROJECT_ROOT_PATH}/bot"

export CONSUMER_KEY="$(jq --raw-output '.consumer_key' ${CREDENTIALS_DIR}/keys.json)"
export CONSUMER_SECRET="$(jq --raw-output '.consumer_secret' ${CREDENTIALS_DIR}/keys.json)"
export ACCESS_TOKEN="$(jq --raw-output '.access_token' ${CREDENTIALS_DIR}/keys.json)"
export ACCESS_TOKEN_SECRET="$(jq --raw-output '.access_token_secret' ${CREDENTIALS_DIR}/keys.json)"


python gadutor/main.py mention_replier
