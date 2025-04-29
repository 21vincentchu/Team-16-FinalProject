from flask import Flask, render_template, request, flash
import requests
import os
import csv
import pygal
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
