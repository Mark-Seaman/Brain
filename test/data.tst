#!/bin/bash
# Test the data management commands

json-save | range 360 400
json-save-company srs

json-load-company srs
json-load


echo impact JSON file
json-show impact | lc

echo impact-srs JSON file
json-show impact-srs | lc
