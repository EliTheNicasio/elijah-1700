# elijah-1700
API-Service and UI to showcase Named Entity Recognition.

Creates an API-Service and UI that user can connect to in a browser. User can input a text into the UI, which will send text to API-Service to process Named Entity Recognition (NER). Result is then shown to user in UI.

Uses docker and docker-compose to bundle everything. Fastapi is used for the API-Service, and the NER was tested with spaCy. H2o Wave was used to make UI.

# How to run
Use `docker-compose up` to start all services. Then, in a browser, go to `http://localhost:10101/`.
