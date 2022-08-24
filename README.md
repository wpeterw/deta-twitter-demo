# deta-twitter-demo



## Getting started

Clone this repostory and install the deta-cli

On Mac/Linux: install the deta-cli with the following command:

curl -fsSL https://get.deta.dev/cli.sh | sh

## deploy the code on Deta

Create the micro in the root of your project: deta new --project <your-project> 

Create a .env that holds your secrets (see settings.py)

Set these secrets as environment variables on Deta: deta update -e <env_file_name>

Create a cron job to run the micro every 15 minutes: deta cron set "15 minutes"


Or just:

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/wpeterw/deta-twitter-demo)

