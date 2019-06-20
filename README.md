# Installation
    pip install -r requirment.txt
    
# Generate Access Token
    Generate the access toke by https://ankit-fyle.herokuapp.com/api/token  with username ankit and password Ankit@123
 
# Urls
  https://ankit-fyle.herokuapp.com/api/banks/ -> for all bank detalis with filters
  
  https://ankit-fyle.herokuapp.com/api/banks/ABHY0065001/ -> bank details with ifsc
  
  https://ankit-fyle.herokuapp.com/api/token -> for jwt token
  
  https://ankit-fyle.herokuapp.com/api/token/refresh -> for refresh the access token

# Curl script
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFua2l0IiwiZXhwIjoxNTYxMDU0MzAxLCJlbWFpbCI6IiJ9.S3-z--VLPkeRaWfYabs_xY9Rz-2dbdIbRzpJFIO7FLE" https://ankit-fyle.herokuapp.com/api/banks/ABHY0065001/
