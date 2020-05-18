#!/bin/sh
# determine development/production
# TODO edit depending on Vue-cli

if [ -z "$DEBUG" ]; then
    echo "Need to set \$DEBUG"
    exit 1
fi  

if [ "$DEBUG" = 1 ] ; then
    npm run-script dev
else
    npm run-script build && serve .
fi
