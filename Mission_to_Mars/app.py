from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import mars_scrape

trial = mars_scrape()
test = trial.scrape()
print(test)
