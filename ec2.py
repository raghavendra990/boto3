import boto3
import conf
import Queue
import threading

data = conf.data
data_keys = conf.keys

client = boto3.Session( aws_access_key_id="AKIAIQZYFWTIQYP5BDJQ",
    aws_secret_access_key="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"
    
    )

zone = client.get_available_regions('ec2')

non_tag = []

def non_tagged(j, client, q):
    ec2 =  client.resource("ec2" , region_name=j)

    instances = ec2.instances.all() 
    for instance in instances:
        try:
            
            tag = {i["Key"]: i["Value"]  for i in instance.tags}
            
            try:
                [tag[i] for i in data_keys]


                keys = data.keys()

                for i in keys:
                    if tag[i] in data[i]:
                        pass
                    else:
                        q.put({"instance_id":instance.id , "region":j})
                        break
                
            except KeyError as e:
                q.put({"instance_id":instance.id , "region":j})

        except TypeError:
            q.put({"instance_id":instance.id , "region":j})

q = Queue.Queue()

threads= []

for j in zone:
    t = threading.Thread(target=non_tagged, args = (j, client, q))
    threads.append(t)
    t.start()

for x in threads:
    x.join()

while(True):
    try:
        non_tag.append(q.get(block=False))
    except Queue.Empty:
        break
print non_tag
