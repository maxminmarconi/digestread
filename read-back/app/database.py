from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# 创建异步引擎，连接到 MySQL 数据库
DATABASE_URL = "mysql+aiomysql://user:password@localhost:3306/digestdemo"

engine = create_async_engine(DATABASE_URL, echo=True)

# 创建异步会话
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session():
    async with async_session() as session:
        yield session