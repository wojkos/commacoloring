# connect to the database
import os
import psycopg2
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse('postgres://lwnowhnbiirony:5c51d45a0147b4fa774399eab8c4d1557391a086de54ae7981188680378e2fc5@ec2-54-247-89-181.eu-west-1.compute.amazonaws.com:5432/d79o3rondn8gpr')

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

