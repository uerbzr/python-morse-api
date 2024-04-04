from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()

morse = {
         'A':". -",
         'B':"- . . .",
         'C':"- . - .",
         'D':"- . .",
         'E':".",
         'F':". . - .",
         'G':"- - .",
         'I':". .",
         'H':". . . .",
         'J':". - - -",
         'K':"- . -",
         'L':". - . .",
         'M':"- -",
         'N':"- .",
         'O':"- - -",
         'P':". - - .",
         'Q':"- - . -",
         'R':". - .",
         'S':". . .",
         'T':"-",
         'U':". . -",
         'V':". . . -",
         'W':". - -",
         'X':"- . . -",
         'Y':"- . - -",
         'Z':"- - . ."
}

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/morse/encode/{sentence}")
async def read_item(sentence: str, q: Union[str, None] = None):
    return {"encoded_message": await encode_string(sentence), "q": q}

@app.get("/morse/decipher/{key}")
async def read_morse_key(key: str):
    return morse[key]
@app.get("/morse")
async def read_morse():
    return morse


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

async def encode_string(message:str):
        result = ""
        for c in message.upper():
            if(c==" "):
                result = result + "       "
            else:                
                result = result + "   " + morse[c]
                                  
        return result
          