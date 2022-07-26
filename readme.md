# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## Change Directory to Root
cd anythink
## Build from root directory
run docker-compose up from root directory
## Point Browser to local ping to confirm its working
http://localhost:3000/api/ping

## Test the user registration portal 
http://localhost:3001/register

**Also you can use docker exec to run commands on a running computer**


**[TODO 05/01/2018 @vanessa-cooper]:** _It's been a while since anyone ran a fresh copy of this repo. I think it's worth documenting the steps needed to install and run the repo on a new machine?