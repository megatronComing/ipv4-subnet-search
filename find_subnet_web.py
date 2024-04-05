'''
Searching for a minimum subnet for every host number required out of a give IPV4 network address.
Requirements:
    flask
    find_subnet.py
By Huafeng Yu, hfyu.hzcn@gmail.com
'''
import find_subnet
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

def parse_parameter(para:str) -> dict:
    '''
    URL example: 
        http://localhost:5000/findsubnets/net:192.168.0.1/masklen:24/hosts:30&5&28
    '''
    server_address = request.url_root
    sample = f'{server_address}findsubnets/net:192.168.0.1/masklen:24/hosts:30&5&28'
    para_list = para.split('/')
    result = {'status': True}
    if len(para_list) != 3:
        return {'status': False, 'message':f'Insufficient paramters, try:{sample}'}
    para_net = para_list[0].split(':')
    if len(para_net) != 2:
        return {'status': False, 'message':f'Invalid parameter:{para_list[0]}, try {sample}'}
    
    net = para_net[0].strip()
    if net.lower() != 'net':
        return {'status': False, 'message':f'Pparameter net missed, try:{sample}'}
    result['net'] = para_net[1].strip()

    para_masklen = para_list[1].split(':')
    if len(para_masklen) != 2:
        return {'status': False, 'message':f'Invalid parameter:{para_list[1]}, try {sample}'}
    net = para_masklen[0].strip()
    if net.lower() != 'masklen':
        return {'status': False, 'message':f'Pparameter masklen missed, try {sample}'}
    result['masklen'] = para_masklen[1].strip()

    para_host = para_list[2].split(':')
    if len(para_host) < 2:
        return {'status': False, 'message':f'Invalid parameter:{para_list[2]}, try {sample}'}
    net = para_host[0].strip()
    if net.lower() != 'hosts':
        return {'status': False, 'message':f'Pparameter hosts missed, try {sample}'}
    # check if there are only digits and & in the parameter
    pattern = re.compile("^[0-9&]+$")
    if not bool(pattern.match(para_host[1])):
        return {'status': False, 'message':f'Invalid hosts parameter, try {sample}'}
    hosts = para_host[1].split('&')

    result['hosts'] = [int(host_num.strip()) for host_num in hosts]
    result['message'] = 'SUCCESS'

    return result

    

# Create a route for handling GET method of /findsubnets/
@app.route('/findsubnets/<path:parameter>', methods=['GET'])
def find_subnets(parameter):
    paras = parse_parameter(parameter)
    
    if not paras['status']:
        return jsonify({"FAILED": paras['message']})
    else:
        myip = find_subnet.IPV4_SUBNET(f"{paras['net']}/{paras['masklen']}", paras['hosts'])
        return jsonify(myip.get_result())
    

@app.errorhandler(404)
def page_not_found(error):
    server_address = request.url_root
    errorMsg = f'OOPS! You inputed a wrong URL. Try {server_address}findsubnets/net:192.168.0.1/masklen:24/hosts:30&5&28'
    return errorMsg, 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
