@echo off

set PG_DB=bhoomi_vivad
set PG_PASSWORD=sa123
set PG_SERVICE_NAME=postgres
set PG_USER=postgres
set SKEY=%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%%RANDOM%

Echo POSTGRES_DB=%PG_DB% > .docker-env
Echo POSTGRES_PASSWORD=%PG_PASSWORD% >> .docker-env
Echo POSTGRES_USER=%PG_USER% >> .docker-env
Echo DATABASE_URL=postgres://%PG_USER%:%PG_PASSWORD%@%PG_SERVICE_NAME%:5432/%PG_DB% >> .docker-env
Echo SECRET_KEY=%SKEY% >> .docker-env