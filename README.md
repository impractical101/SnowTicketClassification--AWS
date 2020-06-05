#Automating the traditional/manual ticket categorization in ServiceNow with use of Machine Learning and AWS. Things to know about repository includes:
Please Note: SNOW has various plugin to do the same task like Agent Intelligence. But they dont provide you the kind of optimizability and code viewing as everything is abstracted. So its always better to code and deploy your own solutions. Feel free to reach out.

1. Process uses generic model using MUltinimialNB for classification of ServiceNow Incident Data. Download it from UCI repository.
2. Using a pipeline to categorize every new input. Finally storing the classifier to pickel file.
3. A lambda funtion to handle the Rest GET and  POST call from SNOW and using the S3 bucket to query the model. 
4. The pickel file needs to be uploaded to s3 along with the model and the lambda function.
5. Keep in mind to give all the necessary access rights while creating lambda and S3.
6. ec2 computing instance with minimum specifications can handle the query. But the response time will be around 15-20 seconds. Use higher specs for good processing and low latency

->> Process flow
1. Create a Snow Instance. Design a workflow for new ticket generation. (Use Snow Documentation)
2. Create a Rest Message response on ticket generation. Use the endpoint from AWS adn configure.
3. On ticket generatioS the ticket description will be sent via a Rest call to lambda funtion which will inturn process the request and return the response in JSON object to SNOW.
4. Catch the response and and use JSON.parse to get parse the JSON object.
5. After parsing populate the category field on the ticket category field.

#UPDATES:
1. Use AWS queue to keep a count on the no of incoming and classified tickets.
2. Reinforcement learning to give feedback to aws model on every classsification done. (Weekly Training)
3. Deploying the API to the model to reduce the hassle.

#################################################################################################
WILL BE UPDATING THE REPOSITORY FOR THE NEW DATASETS, OPTIMIZATIONS AND REINFORCEMENT LEARNING.
Credits to Pankaj Kishore and Jitender Phogat whose repos and blogs helped me implementing the project. If I missed out on anything check their repos. Thank You.
