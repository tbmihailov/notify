#!/usr/bin/env bash

script_name=$0
run_name=test
log_file=mylog.log

script_name=$0
. ~/tools/notify/script_started.sh

echo "Put your experiments script here!"

. ~/tools/notify/script_stopped.sh

