from transform_nfj import tranform_json_to_db
from sqlalchemy import create_engine
import dotenv
import os

dotenv.load_dotenv()


def load_data_to_db():
    clean_data = tranform_json_to_db()

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    db_engine = create_engine(
        f"postgresql://{db_user}:{db_password}@host.docker.internal:5432/{db_name}"
    )
    clean_data.to_sql(
        name="nfj_job_offers", index=False, con=db_engine, if_exists="replace"
    )


if __name__ == "__main__":
    load_data_to_db()
