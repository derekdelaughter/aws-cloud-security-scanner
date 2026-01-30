import json
from datetime import datetime

def generate_report(findings):
    report = {
        "scan_time": datetime.utcnow().isoformat(),
        "findings": findings
    }

    with open("output/report.json", "w") as f:
        json.dump(report, f, indent=4)

        return report