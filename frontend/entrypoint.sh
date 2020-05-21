#!/bin/sh
# determine development/production

if [ -z "$DEBUG" ]; then
    echo "Need to set \$DEBUG"
    exit 1
fi  

if [ "$DEBUG" = 1 ] ; then
    npm run-script dev
else
    npm run-script build && npm run-script serve
fi
