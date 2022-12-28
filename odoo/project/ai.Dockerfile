FROM ubuntu:20.04

# install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    libldap2-dev \
    libsasl2-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-yaml \
    software-properties-common

# install postgresql client
RUN add-apt-repository -y "deb http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main" \
    && curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt-get update \
    && apt-get install -y postgresql-client-13

# install wkhtmltopdf
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.6/wkhtmltox_0.12.6-1.bionic_amd64.deb \
    && apt-get install -y ./wkhtmltox_0.12.6-1.bionic_amd64.deb

# install odoo
COPY . /opt/odoo
RUN pip3 install -r /opt/odoo/requirements.txt \
    && useradd -m odoo \
    && chown -R odoo /opt/odoo

# copy entrypoint script
COPY scripts/entrypoint.sh /
RUN chmod +x /entrypoint.sh

# set environment variables
ENV ODOO_DB_USER odoo
ENV ODOO_DB_PASSWORD odoo
ENV ODOO_DB_HOST db
ENV ODOO_DB_PORT 5432

# set default command
CMD ["/entrypoint.sh"]
