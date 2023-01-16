#!/bin/bash

set -e

if [ -v PASSWORD_FILE ]; then
    PASSWORD="$(< $PASSWORD_FILE)"
fi
echo 'we here'
# set the postgres database host, port, user and password according to the environment
# and pass them as arguments to the odoo process if not present in the config file
: ${HOST:=${DB_PORT_5432_TCP_ADDR:='db'}}
: ${PORT:=${DB_PORT_5432_TCP_PORT:=5432}}
: ${USER:=${DB_ENV_POSTGRES_USER:=${POSTGRES_USER:='odoo'}}}
: ${PASSWORD:=${DB_ENV_POSTGRES_PASSWORD:=${POSTGRES_PASSWORD:='odoo'}}}

DB_ARGS=()
function check_config() {
    param="$1"
    value="$2"
    
    if grep -q -E "^\s*\b${param}\b\s*=" "$ODOO_RC" ; then
        value=$(grep -E "^\s*\b${param}\b\s*=" "$ODOO_RC" |cut -d "=" -f2|sed 's/^\s*//;s/\s*$//;s/["\n\r]//g')
       
    fi;

  
    DB_ARGS+=("--${param}")
    DB_ARGS+=("${value}")
}



check_config "db_host" "$HOST"
check_config "db_port" "$PORT"
check_config "db_user" "$USER"
check_config "db_password" "$PASSWORD"

# specify the database and modules to install
DATABASE="agol_db_1"
MODULES="sale,purchase,crm"

# specify the directory containing the custom addon
ADDON_DIR="/mnt/extra-addons/library_app"
# run the odoo server with the -d, -i, and -i options
# odoo -d "$DATABASE" -i "$MODULES" -i "$ADDON_DIR" "${DB_ARGS[@]}"
# odoo -d "$DATABASE" -i "$ADDON_DIR" "${DB_ARGS[@]}"

wait-for-psql.py ${DB_ARGS[@]} --timeout=30
        # exec odoo -d "$DATABASE" -u library_app "${DB_ARGS[@]}"
        # exec "$@" -d "$DATABASE" -u library_app --test-enable "${DB_ARGS[@]}"
        # exec "$@" -d "$DATABASE" -i library_member "${DB_ARGS[@]}"
        exec "$@" -d "$DATABASE" -i library_app --demo=all "${DB_ARGS[@]}"

exit 1