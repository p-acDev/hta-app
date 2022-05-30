import MySQLdb
import sshtunnel
import json

with open('.env', 'r') as f:
    env_data = json.load(f)

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

def get_data():

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username=env_data['ssh_username'], ssh_password=env_data['ssh_password'],
        remote_bind_address=('pacourbet.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user=env_data['ssh_username'],
            passwd=env_data['ssh_password'],
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=env_data['dbName'],
        )
        # Do stuff
        with connection as con:
            with con.cursor() as c:
                c.execute("SELECT systolic, diastolic, username FROM mesures INNER JOIN users ON mesures.userid=users.idusers;")
                res = c.fetchall()
    return res