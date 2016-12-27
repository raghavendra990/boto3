import boto3
import conf
import threading 

data = conf.data

client = boto3.Session( aws_access_key_id="AKIAIQZYFWTIQYP5BDJQ",
    aws_secret_access_key="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"
    
    )

zone = client.get_available_regions(service_name='ec2'  )


def tag_volumes(j, client):

    ec2 =  client.resource("ec2" , region_name=j)

    instances = ec2.instances.all()

    

    for instance in instances:
        print instance.id
        volumes = instance.volumes.all()
        tag = instance.tags
        if tag != None:
            for v in volumes:
                v.create_tags(Tags=tag)




for j in zone:
    t  = threading.Thread(target= tag_volumes , args = (j,client))
    t.start()

# for j in zone:
#     ec2 =  client.resource("ec2" , region_name=j)

#     instances = ec2.instances.all()

#     for instance in instances:
#         print instance.id
#         volumes = instance.volumes.all()
#         tag = instance.tags
#         if tag != None:
#             for v in volumes:
#                 v.create_tags(Tags=tag)

