#!/usr/bin/env bash
docker stop todoapp_mongo
docker stop todoapp_be
docker rm todoapp_mongo
docker rm todoapp_be
