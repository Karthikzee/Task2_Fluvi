from beanie import init_beanie
import motor.motor_asyncio

from server.models.user import User


async def init_db():

    # using mongodb in local or container
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://mongodb:27017/user"
        # "mongodb://<user>:<password>@<host>:<port>/<dbname>"
    )

    # using mongodb atlas cluster url
    # client = motor.motor_asyncio.AsyncIOMotorClient(
    #    "mongodb+srv://user:adfdfdadf@cluster0.ccsgrxu.mongodb.net/?retryWrites=true&w=majority"
    # )

    await init_beanie(database=client.db_name, document_models=[User])
