from flask import Flask, current_app
import os
# tag::import[]
from neo4j import GraphDatabase
# end::import[]

connectionString = os.getenv('NEO4J_URI')
username = os.getenv('NEO4J_USERNAME')
password = os.getenv('NEO4J_PASSWORD')

"""
Initiate the Neo4j Driver
"""
# tag::initDriver[]
def init_driver(connectionString, username, password):
    # TODO: Create an instance of the driver here
    current_app.driver = GraphDatabase.driver(
                                            connectionString, 
                                            auth=(username, password), 
                                            #   **configuration 
                                        )
    current_app.driver.verify_connectivity()
    return None
# end::initDriver[]


"""
Get the instance of the Neo4j Driver created in the `initDriver` function
"""
# tag::getDriver[]
def get_driver():
    return current_app.driver

# end::getDriver[]

"""
If the driver has been instantiated, close it and all remaining open sessions
"""

# tag::closeDriver[]
def close_driver():
    if current_app.driver != None:
        current_app.driver.close()
        current_app.driver = None

        return current_app.driver
# end::closeDriver[]
