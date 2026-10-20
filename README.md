# JOB RADAR (ongoing)

As a target, the program will be downloading data from public APIs which provide job offers. The same data is used in popular websites with job offers for IT like NoFluffJobs, theprotocol.it, and BulldogJob. 
Downloaded raw data will be stored in a data lakehouse in an AWS S3 bucket. The transformation will be performed with pandas in Python. Picking the important columns, changing data types, and dropping everything 
that doesn't have any value. After cleansing, the clean data will be stored in PostgreSQL and automated by Apache Airflow, so the extraction phase will happen every day. The whole program will be containerized with 
Docker and every step will be tracked with Git / GitHub.



## Tech stack
- Python
- Pandas
- AWS S3
- Apache Airflow
- Docker
- Git / Github


## Progress
- [x] Initializing project structure and Docker environment
- [ ] Creating script that extracts data from APIs
- [ ] Loading raw data in AWS S3 bucket
- [ ] Transforming the data with pandas
- [ ] Loading clean data in PostgreSQL
- [ ] Automation with Apache Airflow
