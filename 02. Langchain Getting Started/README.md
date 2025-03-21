start ollama if it is not
ollama serve

To check status : curl http://127.0.0.1:11434

ollama pull llama3.2:1b

# Run Ollama in the Background

To run Ollama in the background, use the following command:

```sh
nohup ollama serve > ollama.log 2>&1 &
```