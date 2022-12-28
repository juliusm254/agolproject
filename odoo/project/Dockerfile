FROM odoo:15.0

USER root

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8



RUN apt-get update 
#     && apt-get install --no-install-recommends -y python-passlib  python3-wheel \
#      openssl build-essential libssl-dev libxrender-dev git-core libx11-dev libxext-dev \
#      libfontconfig1-dev libfreetype6-dev fontconfig  \
#     && apt-get install python3.7-dev -y\
#     && rm -f /var/lib/apt/lists/*.*

COPY requirements.txt ./

RUN pip3 install -r  requirements.txt

# Copy entrypoint script and Odoo configuration file
COPY ./entrypoint.sh /
COPY ./config/odoo.conf /etc/odoo/

# Set permissions and Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN chown odoo /etc/odoo/odoo.conf \
    && mkdir -p /mnt/extra-addons \
    && chown -R odoo /mnt/extra-addons
# VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# USER odoo

# WORKDIR /mnt/extra-addons



# COPY . .

# Expose Odoo services
EXPOSE 8069 8071 8072

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo.conf

COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py

# Set default user when running the container
USER odoo

# WORKDIR /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]