# Knowledge Transfer Partnership (RGU and Partners)

- API loads data from github raw path in json into a list
- API provides GET endpoint to retrieve data
- API provides POST endpoint to store data
- API provides DELETE endpoint to remove data
- Client side has a refresh and pre-load button


## Pre-requisites

- `python 3.10`, `Flask 2.1.2`, `requests 2.27.1`
- Optionally Install Python IDE e.g Pycharm

## Project Structure

- client side located at `ktpAPI/templates/index.html`
- server side located at `ktpAPI/itemList.py`

## How to Clone

Clone the repositogy on the local machine
- `$ git clone https://github.com/danimalik090/ktpAPI.git`
- OR alternatively you can click on the `download zip` from the top right `code` button dropdown menu.

## How to Deploy

- Load the project in Pycharm
- Navigate to `ktpAPI/itemList.py` and right on the itemList.py and select `run itemList.py`
- Project will be deployed on `127.0.0.1:5000`
- Alternatively you can access the API using Postman

## API endpoint

- `GET` 
- `POST`
- `DELETE`

## Interface of API

![API Homepage](https://github.com/danimalik090/ktpAPI/blob/main/Image1.PNG)
----
![API Additem](https://github.com/danimalik090/ktpAPI/blob/main/image2.PNG)



