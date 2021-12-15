# Power Calculator API

Power Calculator API is a REST API which uses
[abhi-kr-2100/power-calculator](https://github.com/abhi-kr-2100/power-calculator)
to evaluate mathematical expressions.

## Usage

All requests come in the form of POST requests to `API_BASE_URL/api/evaluate`.
Power Calculator API doesn't store any state on the server. As a result, you
must include all the variable definitions in your request.
