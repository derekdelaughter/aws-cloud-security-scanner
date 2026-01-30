import boto3

def check_public_buckets():
    s3 = boto3.client("s3")
    findings = []

    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        name = bucket["Name"]
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            for grant in acl["Grants"]:
                grantee = grant.get("Grantee", {})
                findings.append({
                    "bucket": name,
                    "issue": "Public S3 bucket"
                })

        except Exception as e:
            findings.append({
                "Bucket": name,
                "error": str(e)
            })

    return findings