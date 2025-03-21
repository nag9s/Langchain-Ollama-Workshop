Ref https://visa.udemy.com/course/ollama-and-langchain/learn/lecture/46537661#questions

TBD Create ml environment - check video 01 and then click select kernel and select python interpreter for each notebook

Ensure to pull the following models:
Ref https://ollama.com/library
```sh
ollama pull llama3.2:1b
```

for sheldon model  Ref Video 3 . 12
```sh
        ollama create scientist -f ./scientist.txt
```
            To verify 
```sh
ollama run scientist 
```
```sh        
ollama create sherlock -f ./sherlockHlomesModelfile.txt 
```



02 Done    Video 04 Works , need to see once
03 Done    Video 05 Works , need to see once
04 Done    Video 06 Works , need to see once
05 Done    Video 07 Works , need to see once
06 Done    Video 08 Works , need to see once
07 Ignore ( Own Chatbot application )    Video 09 Resume from here   ModuleNotFoundError: No module named 'streamlit'  
08   01 works   Video 10 
        , 11, 12, 13
09    Done         Video 14 Works
10    Done  Video 15 works

# Labs

Tools:
======
1. chrome
2. Firefox
3. PyCharm
4. Vscode
5. Anaconda python 3.12
6. langchain
7. Git
8. Java
9. Libreoffice
10. Docker 


# Errors
05 Output Parsing

Getting the erorr with model llama3.2:1b - this is fixed by keeping different model

OutputParserException: Failed to parse Joke from completion [{"$schema": "https://json-schema.org/draft-07/schema#", "description": "Joke to tell user", "properties": {"setup": {"description": "The setup of the joke", "title": "Setup", "type": "string"}, "punchline": {"description": "The punchline of the joke", "title": "Punchline", "type": "string"}}, "required": ["setup", "punchline"], "title": "Dogs Joke"}]. Got: 1 validation error for Joke
  Input should be a valid dictionary or instance of Joke [type=model_type, input_value=[{'$schema': 'https://jso..., 'title': 'Dogs Joke'}], input_type=list]
    For further information visit https://errors.pydantic.dev/2.10/v/model_type
For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/OUTPUT_PARSING_FAILURE 
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...

# Docker Container

docker run -it -v %cd%:/app quay.io/jupyter/datascience-notebook:latest /bin/bash       -- interactive mode

docker run -it -v %cd%:/app quay.io/jupyter/datascience-notebook:latest -- to run as notebook

## incase if facing issue with sudo while installing ollma

To install Ollama in an existing Docker container, follow these steps:

1. Find the container ID of your running container:
    ```sh
    docker ps
    ```

2. Attach to the running container as the root user:
    ```sh
    docker exec -it --user root <container_id> /bin/bash
    ```

3. Grant sudo privileges to the `jovyan` user:
    ```sh
    echo "jovyan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
    ```

4. Switch back to the `jovyan` user:
    ```sh
    su jovyan
    ```

5. Install Ollama:
    ```sh
    sudo curl -fsSL https://ollama.com/install.sh | sh

# Setting Up JupyterLab with Conda Kernel

# Setting Up JupyterLab with Conda Kernel

1. Create and activate your conda environment:
    ```sh
    conda create -n ml python=3.12.4 -y ( optional)
    conda activate ml
    pip install -r requirements.txt
    ```

2. Install `ipykernel` in your conda environment:
    ```sh
    pip install ipykernel
    ```

3. Create a new Jupyter kernel for your conda environment:
    ```sh
    python -m ipykernel install --user --name ml --display-name "Python (ml)"
    ```

4. Start JupyterLab:
    ```sh
    jupyter-lab --allow-root --ip=0.0.0.0 --no-browser --notebook-dir=/app
    OR 
    To run in background
    nohup jupyter-lab --allow-root --ip=0.0.0.0 --no-browser --notebook-dir=/app > jupyterlab.log 2>&1 &

    tail -f jupyterlab.log
    ```

5. Open JupyterLab in your browser and select the "Python (ml)" kernel.