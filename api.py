import graphene
import requests
import json

#Define Scema
class Car(graphene.ObjectType):
    ProdID = graphene.ID()
    Name = graphene.String()
    Price = graphene.Float()
    Stock = graphene.Float()
    Desc = graphene.String()

# Mapping Values to Products
class Query(graphene.ObjectType):
    car = graphene.Field(Car)
    
    def resolve_student(root, info):
        data = requests.get('http://127.0.0.1:27017')

        print(data.text)

        #parse JSON
        json_content = json.loads(data.text)
        print(json_content)

        #extract id from JSON
        extractedID = json_content['ProductID']
        extractedName = json_content['Name']
        extractedUnitPrice = json_content['UnitPrice']
        extractedStockQuantity = json_content['StockQuantity']
        extractedDescription = json_content['Description']

        print(extractedName)
        #send the extracted id to the Product
        return Car(ProdID= extractedID, Name=extractedName, Price=extractedUnitPrice, Stock=extractedStockQuantity, Desc=extractedDescription)

    
# Runnig the Query
schema = graphene.Schema(query=Query)
query = """
    {
        car{
            ProdID
            Name
            Price
            Stock
            Desc
        }
    }
"""

result = schema.execute(query)
print(result)
