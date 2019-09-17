import openstack
  
def create_connection():

    return openstack.connect(
        auth_url='http://192.168.0.22:5000/v3',
        project_name='admin',
        username='admin',
        password='eiva4shu7Egh7aig',
        region_name='RegionOne',
    )

conn = create_connection()
server = conn.compute.find_server("instance_teste")
conn.compute.delete_server(server)