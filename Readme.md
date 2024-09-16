# 🤖 ChatBot Using Google Gemini Model

The application allows users to interact with a chatbot through a user-friendly interface built with Streamlit. The backend service is implemented using FastAPI, which handles the generation of responses using the Google Gemini model via the `google.generativeai` Python library.

## Features

- **Interactive Chat Interface**: Users can input messages and receive intelligent responses from the chatbot.
- **Google Gemini Model**: The chatbot leverages the capabilities of the Google Gemini model to generate accurate and contextually relevant replies.
- **Session Management**: Conversation history is maintained throughout the session, allowing for a coherent and continuous conversation experience.
- **Responsive UI**: The interface is styled for better user experience, with customized buttons and message layout.

## Project Structure

The project consists of three main files:

1. **app.py**: Contains the Streamlit application code, which is responsible for the frontend interface and interaction logic.
2. **chatbot.py**: Implements the `BotService` class, which manages the interaction with the Google Gemini model and handles API key configuration.
3. **Dockerfile**: Defines the Docker container configuration to run the application, including setting up the environment and exposing the necessary port.

### `Dockerfile`
The Dockerfile sets up a Docker container to run the chatbot application. Key steps include:

- **Python Base Image**: Uses a lightweight Python image as the base.
- **Working Directory**: Sets the working directory inside the container.
- **Dependencies Installation**: Installs required Python libraries.
- **Code Copying**: Copies the application code into the container.
- **Port Exposure**: Exposes port `8080` for accessing the application.
- **Streamlit Run Command**: Configures the container to run the Streamlit app.

## Installation and Setup

### Prerequisites

- Docker installed on your machine.
- Google API Key for accessing the Google Gemini model.

### Steps to Run Locally

- **Create a .env file: Create a .env file in the root directory with your Google API Key**: GOOGLE_API_KEY="your_google_api_key_here"

### STEP 1

1. **Build and Run Individual Dockerfiles**

    ### FIRST-CONTAINER
   - Build the Streamlit  Docker Image:
    ```bash
        docker build -f Dockerfilefrontend -t streamlit .    
    ```
   - Run the Streamlit  Container:
   ```bash
        docker run -d --name streamlit_containers -p 8501:8501 streamlit
     ```

    ### SECOND-CONTAINER
    - Build the FastAPI Docker Image:
    ```bash
        docker build -f Dockerfilebackend -t fastapi .    
    ```
   - Run the FastAPI Container:
   ```bash
        docker run -d --name fastapi_containers -p 8000:8000 fastapi 
    ```

2. **Access Your Applications:**

    ### FastAPI:
         Visit http://localhost:8000 in your browser.
    
    ### Streamlit:
         Visit http://localhost:8501 in your browser.

### STEP 2: Combine with Docker Compose

    1. Run Docker Compose:
        ```bash
        docker-compose up --build
     ```


### STEP3.  Use Docker Commands
1.    List Containers:
     ```bash
        docker ps
     ```
2.   Start, Stop, Remove Containers:
     ```bash
        docker stop <container_id>
        docker start <container_id>
        docker rm <container_id>
     ```
3.   Inspect Containers and View Logs:
     ```bash
        docker inspect <container_id>
        docker logs <container_id>
     ```

### STEP4.Create a Docker Registry
    Using Docker Hub:

    Create a Docker Hub account.
    Tag your image:
  ```   bash
    docker tag my-flask-app <your-dockerhub-username>/fastapi
 ```
### STEP5.Push the Image:
  ```   bash
    docker push <your-dockerhub-username>/fastapi
 ```
### STEP6. Pull and Run the Images Locally
    Pull the Image:
 ``` bash
    docker pull <your-dockerhub-username>/fastapi
 ```
    Run the Image:
 ``` bash
    docker run -d -p 8000:8000 <your-dockerhub-username>/fastapi

 ```

 https://github.com/Sahil-Kushwaha224/Docker-chatbot-sample.git