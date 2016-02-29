#!/usr/bin/expect

spawn ./manage.py createsuperuser --email=alex@gatherhealth.com --first_name=Alex --last_name=Gao 
expect "Password:"
send "123456\r"
expect "(again)"
send "123456\r"
expect "successfully"
exit
