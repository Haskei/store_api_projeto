import pymongo
#mongodb+srv://<username>:<password>@cluster0.7hxbzld.mongodb.net/

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Projeto_Loja_Dio"]
mycol = mydb["Items"]

i=true
while i == true:
  print("1: insert",\n,"2: delete",\n,"3: update",\n,"4: end")
  x = input()
  if x == 1:
    print("nome: ")
    name = input()
    print("quantity: ")
    quan = input()
    print("status: ")
    stat = input()
    ins_dict[{"Name":name, "Quantity":quan, "Status":stat}]
    mycol.insert_one(ins_dict)
  if x == 2:
    print("name para deletar: ")
    name = input()
    query= {"Name":name}
    mycol.delete_one(query)
  if x == 3:
    print("name do produto a mudar:")
    query = { "Name": name }
    print("1 para mudar o nome",\n,"2 para mudar a quantidade",\n,"3 para mudar o status")
    men=input()
    if men == 1:
      print("novo name: ")
      new_name = input()
      newvalues = { "$set": { "Name": new_name } }
    if men == 2:
      print("nova quantidade:")
      new_quan = input()
      newvalues = { "$set": { "Quantity": new_quan } }
    if men == 3:
      print("novo status: ")
      new_stat = input()
      newvalues = { "$set": { "Status": new_stat } }
    mycol.update_one(myquery, newvalues)
  if x == 4:
    print("bye")
    i= false
  
  
    
