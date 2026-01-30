from scanner.s3_checks import check_public_buckets
from scanner.iam_checks import check_iam_users
from scanner.sg_checks import check_open_security_groups
from scanner.report import generate_report

def run_scan():
    findings = {
        "s3": check_public_buckets(),
        "iam": check_iam_users(),
        "security_groups": check_open_security_groups()
    
    }

    report = generate_report(findings)
    print("Scan complete. Findings:")
    print(report)

if __name__ == "__main__":
    run_scan()