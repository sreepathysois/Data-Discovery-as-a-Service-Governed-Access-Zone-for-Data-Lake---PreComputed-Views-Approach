FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD Msois@123
#ENV MYSQL_DATABASE database
COPY updated_database_38.sql  /docker-entrypoint-initdb.d/
EXPOSE 3306
