<h1 align="center">
📖 EmbedChain-Streamlit-Docker App Template
</h1>

[![A Video Guide](ui.PNG?raw=true)](https://youtu.be/yJAWB13FhYQ)

[https://youtu.be/yJAWB13FhYQ](https://youtu.be/yJAWB13FhYQ)

## Disclaimer 

- Thank you to amjadraza for his original work. This repository try to update some dependencies and add more examples.
- Thank you to vicenteherrera for his contributions to the repository, poetry, makefile, and docker improvements.
- @alonso_isidoro

## 🔧 Features

- Basic Skeleton App configured with `openai` API
- A ChatBot using embedchain and Streamlit
- Docker Support with Optimisation Cache etc
- Deployment on Streamlit Public Cloud
- Updated to latest embedchain version, actual is 0.1.102
- Added hugginface_demo

This repo contains an `main.py` file which has a template for a chatbot implementation.

## Example Input Data:

Select the number of Data Sources from slider and enter the details.

| Source    | URL |
| -------- | ------- |
| youtube  | https://www.youtube.com/watch?v=3qHkcs3kG44   |
| pdf_file |https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf    |
| web    | https://nav.al/feedback  |
|qna_pair| "Who is Naval Ravikant?", "Naval Ravikant is an Indian-American entrepreneur and investor." |

**Question:** What unique capacity does Naval argue humans possess when it comes to understanding explanations or concepts?


## Adding your chain
To add your chain, you need to change the `load_chain` function in `main.py`.
Depending on the type of your chain, you may also need to change the inputs/outputs that occur later on.


## 💻 Running Locally

1. Clone the repository📂

```bash
git clone https://github.com/amjadraza/embedchain-streamlit-app.git
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment🔨

```bash
poetry install
poetry shell
```

3. Run the Streamlit server🚀

```bash
  streamlit run demo_app/main.py 
```
3.1 Run some scripts:

```bash
  python -m hugginface_demo
```

3.2 (optional) Run make:

```bash
    make all
```

possible errors
-------------------

It is possible that this exception happens:
    
    chromadb.errors.InvalidDimensionException: Embedding dimension 768 does not match collection dimensionality 1536. 
    This is commonly a side-effect when an embedding function, different from the one used to add the embeddings, 
    is used to retrieve an embedding from the database.

    Actually i dont know how to maintain both chromedb instances, so i have to some cleaning after and before running 
    hugginface script.

Run App using Docker
--------------------
This project includes `Dockerfile` to run the app in Docker container. In order to optimise the Docker Image
size and building time with cache techniques, I have follow tricks in below Article 
https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0

Build the docker container

``docker build . -t embedchain-streamlit-app:latest ``

To generate Image with `DOCKER_BUILDKIT`, follow below command

```DOCKER_BUILDKIT=1 docker build --target=runtime . -t embedchain-streamlit-app:latest```

1. Run the docker container directly 

``docker run -d --name embedchain-streamlit-app -p 8501:8501 embedchain-streamlit-app:latest ``

2. Run the docker container using docker-compose (Recommended)

``docker-compose up``


Deploy App on Streamlit Public Cloud
------------------------------------
This app can be deployed on Streamlit Public Cloud using GitHub. Below is the Link to 
Publicly deployed App

https://embedchain.streamlit.app/



## Report Feedbacks

As `embedchain-streamlit-app:latest` is a template project with minimal example. Report issues if you face any. 

## DISCLAIMER

This is a template App, when using with openai_api key, you will be charged a nominal fee depending
on number of prompts etc.

Rename .env.example to .env, add your environment keys, ask for permission in order to access mistral, create your
container with your credentials and run the app.

https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2