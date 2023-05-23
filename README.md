# Page Tracker

###
This app is a simple page tracker using Flask that connects to a Redis store to track the number of visits a page has received.
The services are set up in docker containers and can be spun up using the [docker compose](docker-compose.yml) file. 

It also contains some basic tests (unit, integration, and end-to-end) as well as a Github Actions workflow that runs on the
creation of any pull request or merge back into the main branch.

This was created using the tutorial from [realpython](https://realpython.com/docker-continuous-integration/)
