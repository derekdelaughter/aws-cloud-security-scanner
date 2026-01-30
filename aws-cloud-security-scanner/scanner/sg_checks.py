import boto3

def check_open_security_groups():
    ec2 = boto3.client("ec2")
    findings = []

    sgs = ec2.describe_security_groups()["SecurityGroups"]

    for sg in sgs:
        for perm in sg.get("InPermissions", []):
            for ip_range in perm.get("IpRanges", []):
                if ip_range.get("CidrIp") == "0.0.0.0/0":
                    findings.append({
                        "security_group": sg["GroupName"],
                        "issue": "Open to the world",
                        "port": perm.get("FromPort")
                    })

    return findings