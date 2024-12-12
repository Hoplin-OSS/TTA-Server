from sqlmodel import Session
import repositories.health as health_repository

async def database_health(session:Session):
    return health_repository.database_health(session)