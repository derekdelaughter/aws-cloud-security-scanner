import boto3

def check_iam_users():
    iam = boto3.client("iam")
    findings = []

    users = iam.list_users()["Users"]

    for user in users:
        policies = iam.list_attached_user_policies(
            UserName=user["UserName"]
        )["AttachedPolicies"]

        for policy in policies:
            if policy["PolicyName"].lower().startswith("admin"):
                findings.append({
                    "user": user["UserName"],
                    "issue": "Admin-level policy attached"
                })

    return findings