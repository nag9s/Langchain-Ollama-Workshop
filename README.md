Ref https://visa.udemy.com/course/ollama-and-langchain/learn/lecture/46537661#questions
TBD Create ml environment - check video 01
and then click select kernel and selet python interpreter for each note book

Ensure to pull the following models
Ref https://ollama.com/library
ollama pull llama3.2:1b

for sheldon model  Ref Video 3 . 12
        ollama create scientist -f ./scientist.txt
            To verify ollama run scientist 
        ollama create sherlock -f ./sherlockHlomesModelfile.txt 



02 Done    Video 04 Works , need to see once
03 Done    Video 05 Works , need to see once
04 Done    Video 06 Works , need to see once
05 Done    Video 07 Works , need to see once
06 Done    Video 08 Works , need to see once
07 Ignore ( Own Chatbot application )    Video 09 Resume from here   ModuleNotFoundError: No module named 'streamlit'  
08 Ignore ( Loaders )    Video 10 , 11, 12, 13
09    Done         Video 14 Works
10    Done  Video 15 works




# Errors
05 Output Parsing
Getting the erorr with model llama3.2:1b - this is fixed by keeping different model
OutputParserException: Failed to parse Joke from completion [{"$schema": "https://json-schema.org/draft-07/schema#", "description": "Joke to tell user", "properties": {"setup": {"description": "The setup of the joke", "title": "Setup", "type": "string"}, "punchline": {"description": "The punchline of the joke", "title": "Punchline", "type": "string"}}, "required": ["setup", "punchline"], "title": "Dogs Joke"}]. Got: 1 validation error for Joke
  Input should be a valid dictionary or instance of Joke [type=model_type, input_value=[{'$schema': 'https://jso..., 'title': 'Dogs Joke'}], input_type=list]
    For further information visit https://errors.pydantic.dev/2.10/v/model_type
For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/OUTPUT_PARSING_FAILURE 
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...