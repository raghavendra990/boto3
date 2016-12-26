import boto3
import conf


data = conf.data
data_keys = conf.keys

client = boto3.Session( aws_access_key_id="AKIAIQZYFWTIQYP5BDJQ",
    aws_secret_access_key="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"
    
    )

zone = client.get_available_regions('ec2')

non_tag = []

for j in zone:
    instances =  client.resource("ec2" , region_name=j).instances.all() 
    # instances = instances.append( client.resource("ec2" , region_name=j).instances.all() 

    for instance in instances:
        print instance.id
        try:
            
            tag = {i["Key"]: i["Value"]  for i in instance.tags}
            
            try:
                [tag[i] for i in data_keys]


                keys = data.keys()

                for i in keys:
                    if tag[i] in data[i]:
                        pass
                    else:
                        non_tag.append(instance.id)
                        break
                
            except KeyError as e:
                non_tag.append(instance.id)

        except TypeError:
            non_tag.append(instance.id)

print non_tag



