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
**make sure to turn off streaming in settings.**

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



# **philosophy**: 

I have my pc and I can use 12B models. But it is always great if we have atleast 1 free way to get cloud model service. As Hugging chat is free and opensource, I search A way to get It working.
First I searched For tools And then I Foud this wonderful tool https://github.com/Soulter/hugging-chat-api then I created A discussion On sillytavern Github https://github.com/SillyTavern/SillyTavern/discussions/3813  to request this feature.

@Cohee1207 said I can fork And add it myself If I want. 
so here we are now we have this tool. Please help me more to make it even better. 

## **Support and contribution**

I would appreciate your support and contribution to this project. No need to do extensive work; even small contributions can help:

- Share this project with others to reach more people who may benefit from a free alternative.
- Star and like this repository to show your support.
- Create pull requests and contribute code if you can.
- Contact me on [Discord](https://discordapp.com/users/631322774597533737) or GitHub for any questions or further collaboration.
