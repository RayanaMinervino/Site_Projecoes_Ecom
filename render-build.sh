#!/usr/bin/env bash
# Atualiza o sistema e instala o ODBC Driver 18 para SQL Server

apt-get update && apt-get install -y curl gnupg
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql18
