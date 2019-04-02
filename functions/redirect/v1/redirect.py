import json

def lambda_handler(event, context):   
    response = {}
    response["statusCode"]=302
    response["headers"]={'Location': 'https://res.cloudinary.com/teepublic/image/private/s--sqd2KCzb--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1484078711/production/designs/1096211_1.jpg'}
    data = {}
    response["body"]=json.dumps(data)
    return response