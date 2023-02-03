import pandas as pd
import logging


def hello():
    print("Hello, World!")


def make_df():
    data = [ { "Hello": "World", "Hey": "There" }]
    df = pd.DataFrame(data)
    return(df)


if __name__ == "__main__":
    hello()
    df = make_df()
    print(df)