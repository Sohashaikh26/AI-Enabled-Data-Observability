from sqlalchemy import create_engine


def get_connection():

    username = "postgres"
    password = "nuhasoha"
    host = "localhost"
    port = "5432"
    database = "data_observability"

    connection_string = (
        f"postgresql://{username}:{password}"
        f"@{host}:{port}/{database}"
    )

    engine = create_engine(connection_string)

    return engine