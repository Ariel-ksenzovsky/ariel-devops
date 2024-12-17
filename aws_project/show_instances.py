import boto3

def list_all_instances():
    # יצירת session
    session = boto3.session.Session()
    
    # קבלת רשימת כל האזורים
    ec2_client = session.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    print(f"Found {len(regions)} regions. Listing instances in all regions...\n")
    
    for region in regions:
        print(f"--- Region: {region} ---")
        
        # יצירת לקוח EC2 לאזור הספציפי
        ec2 = session.client('ec2', region_name=region)
        
        # קבלת רשימת ה-instances
        response = ec2.describe_instances()
        
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    "InstanceId": instance['InstanceId'],
                    "State": instance['State']['Name'],
                    "InstanceType": instance['InstanceType'],
                    "PublicIpAddress": instance.get('PublicIpAddress', 'N/A'),
                    "PrivateIpAddress": instance.get('PrivateIpAddress', 'N/A')
                })
        
        if instances:
            for instance in instances:
                print(f"Instance ID: {instance['InstanceId']}, "
                      f"State: {instance['State']}, "
                      f"Type: {instance['InstanceType']}, "
                      f"Public IP: {instance['PublicIpAddress']}, "
                      f"Private IP: {instance['PrivateIpAddress']}")
        else:
            print("No instances found in this region.")
        
        print("\n")

if __name__ == "__main__":
    list_all_instances()
