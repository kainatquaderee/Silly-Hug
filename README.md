# silly-Hug (Silly-hug🤓🤗)
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
email password and assistentId (empty assisten provided bellow(or any you want)
`python server.py`
# sillytavern:
go to sillytavern --> connection-profile --> chat completion --> custom

in custom endpoint put http://127.0.0.1:5000/v1
make sure to turn off streaming in settings.

### empty assistent for all models in huggingface:
