# JOB RADAR

The program is a fully automated Data Engineering pipeline that downloads job offer data from public APIs. Currently, the pipeline extracts IT job offers from platforms like NoFluffJobs.

Downloaded raw data is stored in a data lakehouse in an AWS S3 bucket. The transformation is performed using pandas in Python, which includes picking the important columns, standardizing data types, and dropping everything that doesn't have business value. After cleansing, the clean data is loaded into a local PostgreSQL database. The entire ETL process is orchestrated and automated by Apache Airflow, scheduling the extraction phase to happen every day. The whole program is containerized with Docker, and every step is tracked with Git and GitHub.

**Tech stack**
- Python (Pandas, Requests, SQLAlchemy)
- AWS S3
- PostgreSQL
- Apache Airflow
- Docker & Docker Compose
- Git / GitHub

**Progress**
- [x] Initializing project structure and Docker environment
- [x] Creating script that extracts data from APIs
- [x] Loading raw data in AWS S3 bucket
- [x] Transforming the data with pandas
- [x] Loading clean data in PostgreSQL
- [x] Automation with Apache Airflow

**Roadmap (Next Steps)**
- **Scaling Data Sources:** Integrating additional job board APIs (e.g., JustJoin.it, theprotocol.it) and unifying their distinct JSON structures into a single, cohesive database schema.
- **Data Quality Control:** Implementing automated data validation steps within the pipeline to detect API structural changes or missing values before loading them into the database.
- **Data Visualization (BI):** Deploying a Business Intelligence tool connected to the PostgreSQL database to create interactive dashboards tracking salary ranges, technology trends, and market demands.
