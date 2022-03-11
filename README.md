# Solution Overview

## Client

1. Client folder has a react app with a simple login page with email and password input text boxes.
2. React app invokes the python flask app in server folder to save the user email and password.

3. to build and push docker image

  ```bash
  $ cd client
  $ docker build -t meghanasrinivas98/client:latest .
  $ docker push meghanasrinivas98/client:latest
  ```

## Server

1. Server folder has a flask api with POST request to `/user` route that gets email and password ans saves it in postgres database.
2. flask bcrypt module is used to encrypt and store the password in the database.

3. to build and push docker image

  ```bash
  $ cd client
  $ docker build -t meghanasrinivas98/server:latest .
  $ docker push meghanasrinivas98/server:latest
  ```


## K8s

1. `client.yaml` has the kubernetes manifests to deploy the client app(frontend) with autoscaling and service.
2. `server.yaml` has the kubernetes manifests to deploy the server app(backend) with autoscaling and service.
3. `database.yaml` has the kubernetes manifests to deploy the postgres database with autoscaling and service.
4. To deploy

```bash
$ kubectl apply -f ./kube8/
```

5. To run query on postgres database running in kubernets pod.

```bash
$ kubectl exec postgres-deployment-5475bcdbbb-lclpm -- sh -c 'PGPASSWORD=postgres psql -U "postgres" -d "postgres" -c "select * from user"'
```
