#!/bin/bash

airflow initdb
airflow scheduler &
exec airflow webserver