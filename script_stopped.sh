#!/usr/bin/env bash

# set environment variables
# export notif_user_email=your.email@gmail.com
# export notif_user_pass=yourpasssthatnooneknow

server_info="$(hostname)_dev_${CUDA_VISIBLE_DEVICES}"

to=${notif_my_email}
subject="[${server_info}, screen:$STY] Script has ended"
msg="Check the script at: hostname: $(hostname); \n cuda_device:$CUDA_VISIBLE_DEVICES \n script_name:${script_name} \n run_name:${run_name} \n log file: ${log_file}"

python ~/tools/notify/send_email.py ${to} "${subject}" "${msg}"