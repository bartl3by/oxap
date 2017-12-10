# Swagger server

This swagger-enabled middleware uses the [Connexion](https://github.com/zalando/connexion) library on top of Tornado.

## Requirements
Python 3.5.2+

## Installation
In order to be able to start the middleware, install the required python libraries:
```
pip3 install -r requirements.txt
```

## Usage
To run the server, please execute the following from the root directory:

```
python3 -m swagger_server
```

or use nodemon for automatic restarts when changing source code during development:

```
nodemon --watch swagger_server --ext py,yaml,yml --exec "python3 -m swagger_server"
```

After starting the middleware, the Swagger UI is available at:

```
http://localhost:8080/v2/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/v2/swagger.json
```

## Building
Use swagger-codegen to update the middleware controllers:
```
swagger-codegen generate -i api/oxap_api.yml -l python-flask -o middleware
```