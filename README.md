# golden-ratio-beauty-calculator
___
## Docker setup
### Build the docker image  
`docker build -t goldenratioimage .`  

### Start the Docker Container
`docker run -d --name goldenratiocontainer -p 80:80 goldenratioimage`  
If the container was started successfully, go to the default [swagger page](http://127.0.0.1/docs)