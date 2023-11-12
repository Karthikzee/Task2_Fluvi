from fastapi.encoders import jsonable_encoder


def encode_input(data) -> dict:  # excluding fields not being updated to prevent overwriting existing field with None
    data = jsonable_encoder(data)
    data = {k: v for k, v in data.items() if v is not None}
    return data
