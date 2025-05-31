with open('info.txt','w') as f:
    data='''Hello team,

Please reach out to the following contacts for your queries:

- Alice Johnson: alice.johnson@example.com
- Bob Smith (HR): bob_smith123@company.co.uk
- Support Desk: support@service.io
- Marketing Lead: marketing-team@business.org
- For urgent matters, contact urgent.help@emergency.net or admin@company.com.

Thanks,
John Doe
john.doe@workplace.edu
'''
    f.write(data)
import re
pattern=r'[a-zA-Z0-9./+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
with open('info.txt','r') as f:
    data=f.read()
all_emails=re.findall(pattern,data)
print(all_emails)
