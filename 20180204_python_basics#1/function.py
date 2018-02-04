#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check(height):
    if height >= 160:
        return "John"
    else:
        return "Michel"

name = "who"
print(name)
h = 170
name = check(h)
print(name)


curl -X POST -H 'Authorization: Bearer xoxp-184717347331-189088339746-243930928130-2f2e7d9eacb6b3eaae75b3146f14f6db' \
-H 'Content-type: application/json' \
--data '{"channel":"C94L04EDV","text":"nya","attachments": []}' \
https://slack.com/api/chat.postMessage
