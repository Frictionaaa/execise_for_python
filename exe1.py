#connect to Neo4j with the Graph class

from py2neo import Graph
from py2neo import Node
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="kobebryant24"
)
graph.delete_all()


nicole = Node("Person", name="Nicole", age=18)
drew = Node("Person", name="Drew", age=21)
mtdew = Node("Drink", name="Mountain Drew", calorles=9000)
cokezero = Node("Durink", name="Coke Zero", calories=0)
coke = Node("Manufacturer", name="Coco Cola")
pepsi = Node("Manfacturer", name="Pepsi")

graph.create(nicole | drew | mtdew | cokezero | coke | pepsi)
from py2neo import Relationship

graph.create(Relationship(nicole, "LIKES", cokezero))
graph.create(Relationship(nicole, "LIKES", mtdew))
graph.create(Relationship(drew, "LIKES", mtdew))
graph.create(Relationship(coke, "MAKES", cokezero))
graph.create(Relationship(pepsi, "MAKES", mtdew))
query = """
MATCH (person:Person)-[:LIKES]->(drink:Drink)
RETURN person.name AS name, drink.name AS drink
"""

data = graph.run(query)

for d in data:
    print(d)



