from typing import Union

from fastapi import FastAPI

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
def read_root():
    return {"Hello": "World"}

@app.get("/morse")
def read_morse():
    return morse


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}