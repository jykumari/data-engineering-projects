#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/level_up")
def level_up():
    level_Up_event = {'event_type': 'level_up'}
    log_to_kafka('events', level_Up_event)
    return "You have moved up a level!\n"



@app.route("/add_coins")
def add_coins():
    add_coins_event = {'event_type': 'add_coins'}
    log_to_kafka('events', add_coins_event)
    return "You earned coins!\n"


@app.route("/destroy_base")
def destroy_base():
    destroy_base_event = {'event_type': 'destroy_base'}
    log_to_kafka('events', destroy_base_event)
    return "Base is destroyed!\n"