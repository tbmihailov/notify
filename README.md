# Setup
To install this script you need an e-mail account with username and password

== Get the files
Clone the project in:

~/tools/notify

```bash
cd ~/
mkdir tools
cd tools

git clone https://github.com/tbmihailov/notify.git

```

== Signup a new e-mail account at gmail.com

This is recommended as your password will be stored in free text in the ~/.profile ..

== On the server put the followin in ~/.profile

```bash
export notif_user_email=your.email@gmail.com
export notif_user_pass=yourpasssthatnooneknow
export notif_my_email=your-email-to-receive-the-notifications@yourdomain.com

```

== Use the scripts in your experiments script

```bash
script_name=$0  # this will save the name of the file where the notification is sent from
run_name=my-scripts-for-doing-something  # a friendly name that you can recognize what your run is about- this can be also the log file name
log_file=mylogfile.log  # the name of a log file that you want ot have in your e-mail.

script_name=$0
. ~/tools/notify/script_started.sh

echo "Put your experiments script here!"

. ~/tools/notify/script_stopped.sh
```

# The e-mail that you will get will contain

```
to:"${notif_my_email}"
subject="[${server_info}, screen:$STY] Script started"
msg="Check the script at: hostname: $(hostname); \n cuda_device:$CUDA_VISIBLE_DEVICES \n script_name:${script_name} \n run_name:${run_name} \n log file: ${log_file}"
```

