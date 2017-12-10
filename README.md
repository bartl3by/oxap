# oxap
Open-Xchange Admin Panel

middleware:
  Build: swagger-codegen generate -i api/oxap_api.yml -l python-flask -o middleware 
  Execute: nodemon --watch swagger_server --ext py,yaml,yml --exec "python3 -m swagger_server"
