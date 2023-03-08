#!/bin/bash

# Login credentials
username="<USERNAME>"
password="<PASSWORD>"

# URL to send the POST request to
url="<URL>"

dst="http%3A%2F%[2Fdetectportal.firefox.com](http://2fdetectportal.firefox.com/)%2Fcanonical.html"
popup="true"

body="username=$username&password=$password&dst=$dst&popup=$popup"

response=$(curl -s -d "$body" -X POST $url)

echo $response
