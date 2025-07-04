from tortoise import Tortoise
from core.settings import TORTOISE_ORM



async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas(safe=True)
