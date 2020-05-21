#!/bin/sh
# determine development/production

if [ -z "$DEBUG" ]; then
    echo "Need to set \$DEBUG"
    exit 1
fi  

if [ "$DEBUG" = 1 ] ; then
    uvicorn --host 0.0.0.0 --port 5000 main:app --log-level debug --reload
else
    uvicorn --host 0.0.0.0 --port 5000 --workers 4 --log-level info main:app
fi
