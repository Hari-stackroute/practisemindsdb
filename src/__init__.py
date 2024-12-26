import mindsdb_sdk

# connects to the default port (47334) on localhost
server = mindsdb_sdk.connect()

# connects to the specified host and port
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

#Getting a specific project
mindsdb = server.get_project('mindsdb')

#Listing out data-handlers
data_handlers = mindsdb.query('SHOW HANDLERS WHERE type = \'data\'')
print(data_handlers.fetch())

#Listing out databases
print(server.list_databases())

#Listing out projects
print(server.list_projects())

#Listing out ml-handlers
ml_handlers = mindsdb.query('SHOW HANDLERS WHERE type = \'ml\'')
print(ml_handlers.fetch())

#Print out a specific project
project = server.get_project()
print("project:::",project.name)

#Listing out models
print(project.list_models())

#Working with AWS-Bedrock Agent Sample.
agentList = server.agents.list()
print(agentList)
#Enter the Agent i.e, already created else create one and use it
aws_agent1 = server.agents.get('aws_multi_skill_text_to_sql_agent2')
print("aws_agent details:",aws_agent1)
print('Agent ready to use.')
while True:
    print('Ask a question: ')
    question = input()
    if question.strip() == "":
        break
    answer = aws_agent1.completion([{'question': question, 'answer': None}])
    print(answer.content)
