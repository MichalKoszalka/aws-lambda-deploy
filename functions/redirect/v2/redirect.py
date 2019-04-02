import json

def lambda_handler(event, context):   
    response = {}
    response["statusCode"]=302
    response["headers"]={'Location': 'https://res.cloudinary.com/teepublic/image/private/s--qdBkljDY--/t_Preview/b_rgb:ffffff,c_limit,f_jpg,h_630,q_90,w_630/v1516825854/production/designs/2305863_0.jpg'}
    data = {}
    response["body"]=json.dumps(data)
    return response