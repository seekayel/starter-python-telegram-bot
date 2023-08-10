# FastAPI Starter

This is the simplest possible python FastAPI app that responds with: 
```
{"message": "Hello World"}
```

## Deploy to Cyclic in seconds 

[![Deploy to Cyclic](https://deploy.cyclic.app/button.svg)](https://deploy.cyclic.app/)

Set `server.py` as your entry point.

## Run Locally

Prerequisites:
- pyenv
- python 3.10.11

Install: `bin/install`
- creates virtual env
- installs dependencies from `requirements.txt`

Run: `bin/dev`
- runs a `uvicorn` server in reload mode

Run: `bin/start`
- runs a `uvicorn` server


## Questions / Help

Join us on Discord: [https://discord.cyclic.sh](https://discord.cyclic.sh)

Enjoy!


curl -F "url=https://weak-red-toad.cyclic.app/webhook/sec_0103b52d06e2ba8f7e3782c86d3958d49217fdb1" https://api.telegram.org/bot6619820209:AAFlZu0vdfKtvMbm12Ueyiv5tHPXSMCelsI/setWebhook

curl -F "url=https://weak-red-toad.cyclic.app/webhook/" https://api.telegram.org/bot6619820209:AAFlZu0vdfKtvMbm12Ueyiv5tHPXSMCelsI/setWebhook
