#!/bin/bash

echo "Creating NPA API user ..."
mongosh admin -u ${MONGO_INITDB_ROOT_USERNAME} -p ${MONGO_INITDB_ROOT_PASSWORD} --authenticationDatabase admin <<EOF
use $MONGO_INITDB_DATABASE
db.createUser({
    user: "$MONGO_API_USER",
    pwd: "$MONGO_API_PWD",
    roles: [
        {
            role: "readWrite",
            db: "$MONGO_INITDB_DATABASE"
        }
    ]
})
EOF