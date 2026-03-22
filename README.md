# Cloud Engineer Intern Coding Challenge 

**Author:** Cole Parsons

## Overview

This is a small containerized web service built for the Cloud Engineer Intern Coding Challenge. It demonstrates basic cloud engineering fundamentals such as:    
* Minimal Flask Application with three routes ('/', '/health', '/info')  
* HTTPS enabled using a self signed certificate  
* Containerized with Docker and Docker Compose  

---

## Application Routes  

Route: '/'       Method: GET - Description: Returns a home page message  
Route: '/health' Method: GET - Description: Returns a JSON indicating health status  
Route: '/info'   Method: GET - Description: Returns a JSON with app metadata (name, version, author)  

## Requirements  

* Docker & Docker Compose installed  
* HTTPS access via self signed certificate  

---

## How to Run  

1. ### Without Git installed  
(1.1) Download the contents of this repository into a parent folder  
(1.2) Ensure your working Directory is the parent folder  

1. ### With Git installed  
Run  
(1.1) `git clone https://github.com/Cole-Parsons/Coding-Challenge.git`  
(1.2) `cd Coding-Challenge`  

2. Build and start the service with Docker Compose `docker compose up --build`  

3. Access services:  
* Home page: https://localhost:8000  
* Health: https://localhost:8000/health  
* Info: https://localhost:8000/info  

4. Stop the service: `Ctrl + c` in your terminal  

## Design Choices  
* Flask: Simple lightweight Python framework for minimal webservice  
* Containerization: Docker makes it easy to run locally or deploy to the cloud without worrying about local dependencies  
* HTTPS: Self signed certificate included for demonstration  
* Minimal Routes: Only what is needed to demonstrate cloud engineering fundamantals  

## Improvements with more time  
* Add logging to track requests  
* Automatically generate self signed certificates at build time  
* Make /info route more dynamic (e.g., include container ID or uptime)  

## Cloud Deployment  

This service could be deployed to the cloud, for example using AWS ECS (Elastic Container Service).    
In the cloud, we could run the container and expose it via a load balancer to handle HTTPS traffic.  
SSL certificates and sensitive keys should be stored securely rather than in the repository.  

Secrets such as SSL Keys should **NEVER** be stored in a repository. Use cloud secret managers for example, AWS Secret Manager.  

## HTTPS & Security  
* HTTPS is enabled using a self signed certificate located in `certs/`  
* Storing a private SSL key locally in a repository is bad practice because:  
-It exposes the private key to anyone with repo access  
-Compromised keys allow attackers to decrypt traffic or impersonate the service  
-In production, keys should be managed securely  
