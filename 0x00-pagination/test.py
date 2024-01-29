#!/usr/bin/env python3

import requests

url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240129%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240129T190603Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=80c4f8131ab4295abc73b2e01f133a6f8c6c2f2714d9144cc223963330d61588"
response = requests.get(url)

with open('Popular_Baby_Names.csv', 'wb') as f:
    f.write(response.content)
