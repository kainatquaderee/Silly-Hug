# silly-Hug (Silly-hug😇🤗)
Huggingface models for sillytavern

### get started:
First you need a huggingface id
go here and create one if not have yet: https://huggingface.co/chat/
# clone 
```
git clone https://github.com/kainatquaderee/Silly-Hug.git
```
`cd ./Silly-Hug`
# install all python packages 
`pip install -r requerements.txt`


Fill all .env parameters
email password and modelid provided bellow

`python server.py`
# sillytavern:
go to sillytavern --> connection-profile --> chat completion --> custom

in custom endpoint put http://127.0.0.1:5000/v1
make sure to turn off streaming in settings.

# model list with id
note: put id in .env for using 
| Model ID | Model Name                                               |
|----------|-----------------------------------------------------------|
| 0        | meta-llama/Llama-3.3-70B-Instruct                         |
| 1        | Qwen/Qwen2.5-72B-Instruct                                 |
| 2        | CohereForAI/c4ai-command-r-plus-08-2024                   |
| 3        | deepseek-ai/DeepSeek-R1-Distill-Qwen-32B                  |
| 4        | nvidia/Llama-3.1-Nemotron-70B-Instruct-HF                 |
| 5        | Qwen/QwQ-32B                                              |
| 6        | Qwen/Qwen2.5-Coder-32B-Instruct                           |
| 7        | google/gemma-3-27b-it                                     |
| 8        | meta-llama/Llama-3.2-11B-Vision-Instruct                  |
| 9        | NousResearch/Hermes-3-Llama-3.1-8B                        |
| 10       | mistralai/Mistral-Nemo-Instruct-2407                      |
| 11       | microsoft/Phi-3.5-mini-instruct                           |


