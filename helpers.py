import csv
import urllib.request
from flask import redirect, render_template, request, session
from functools import wraps
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask import request
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from sonm import *
import os

db = SQL("sqlite:///sonm.db")

def home():
    return render_template("/homepage.html", live_deals = live_deals, total_eth_hash = total_eth_hash, consumers = consumers, suppliers = suppliers, live_deals_ids = live_deals_ids, unique_consumers_amount = unique_consumers_amount, unique_suppliers_amount = unique_suppliers_amount, hourly_volume = round(hourly_volume, 2), total_deals = total_deals)