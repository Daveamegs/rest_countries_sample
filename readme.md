# REFERENCE / DOCUMENTATION

## Introduction

This is a sample rest api similar to restcountries. Just like restcountries, it is very easy to use. You just have to make a request to the api endpoind and receive a jsonified response.

## Getting Started

To get started?, make a valid request to an endpoint and receive a json data to consume.

### Base url

The base url for this api is `localhost:5000` or `http://127.0.0.1:5000`. Either way is the same. The base url currently only returns a string that tells you to make a request to the only endpoint available.

### Authentication / Api Key

This is an open api and therefore consuming it requires no authentication.

## Error Handling

Errors are returned as JSON Object.
Example using error 404

```
{
    "success": False,
    "error_code": 404,
    "error message": "resource not found"
}

```

## Endpoints

The only valid request that can be made to this endpoint at the moment is a GET resquest to retrieve all the available country names with their attributes.

### Get Request

#### GET /countries 200 OK

This is the only endpoint available at the moment beside the base url.

- sample `curl http://127.0.0.1:5000/countries`

```

```
