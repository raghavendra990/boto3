import boto3
import conf



data = conf.data


client = boto3.session.Session(aws_access_key_id="AKIAIQZYFWTIQYP5BDJQ",
    aws_secret_access_key="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",
    region_name="ap-southeast-1"
    )

ec2 = client.resource('ec2')

instances = ec2.instances.all()
print instances 
non_tag = []

for instance in instances:
    try:
        
        tag = {i["Key"]: i["Value"]  for i in instance.tags}
        
        try:
            tag["owner"]

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