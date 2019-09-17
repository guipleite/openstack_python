import openstack
def create_connection():

    return openstack.connect(
        auth_url='http://192.168.0.22:5000/v3',
        project_name='admin',
        username='admin',
        password='eiva4shu7Egh7aig',
        region_name='RegionOne'
    )

def create_server(conn):
    print("Create Server:")

    image = conn.compute.find_image("bionic")
    flavor = conn.compute.find_flavor("m1.tiny")
    network = conn.network.find_network("internal")
    keypair = conn.compute.find_keypair("maas")

    server = conn.compute.create_server(
        name="instance_teste", image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name=keypair.name)

    server = conn.compute.wait_for_server(server)

conn = create_connection()

create_server(conn)