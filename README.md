# CDC Crawler

### Quick Start
1. Clone the Repository
```
$ git clone https://github.optum.com/catalyst/cdc.git
$ cd cdc
```

2. Initialise and activate a virtualenv
```
$ python3 venv venv
$ venv\Scripts\activate
```
On a unix machine:
```
$ python3 venv venv
$ source venv\bin\activate
```

3. Install requirements
```
$ pip install -r requirements.txt
```

4. Set environment variables
```
state=state_name
elastic_server_host=server_address
elastic_username=username
elastic_password=password
elastic_port=host_port
elastic_azure_host=azure_elastic_address
elastic_azure_username=username
elastic_azure_password=password
elastic_azure_port=azure_port
ocr_subscription_key=your_subscription_key
ocr_endpoint=your_ocr_endpoint
```

5. Run the crawler
```
$ python code/changes.py
```
