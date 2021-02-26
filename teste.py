# import docker
# client = docker.from_env()
# print(client.containers.run("alpine", ["echo", "hello", "world"]))

# import docker
# client = docker.from_env()
# container = client.containers.run("bfirsh/reticulate-splines", detach=True)
# print(container.id)

# import docker
# client = docker.from_env()
# for container in client.containers.list():
#   print(container.id)

# import docker
# client = docker.from_env()
# container = client.containers.get('f2b02bdd189de25e64cd1aea75986165fc4e4751db110824e1cb0762cc340826')
# print(container.logs())

# import docker
# client = docker.from_env()
# for image in client.images.list():
#   print(image.id)


import docker
client = docker.from_env()
#image = client.images.dockerfile(dockerfile="Dockerfile_ROS")

my_network = client.networks.create(
    "my_network",
    driver="bridge"
)

# volume = client.volumes.create(name='teste')


print ("Imagem Listener:")
# container_listener = client.images.build(path="./", dockerfile="Dockerfile_ROS", tag="original_listener", squash=True)
container_listener = client.images.build(path="./", dockerfile="Dockerfile_ROS", tag="original_listener")
# listener:
#     container_name: listener
#     build:
#       context: "./"
#       dockerfile: Dockerfile_ROS
#     environment:
#       - "PYTHONUNBUFFERED=1"
#     command: ros2 run codigo_gustavo listener
#     networks:
#       - my_network
print ("Run Listener:")
# client.containers.run("original_listener", name="listener", detach=True, environment=["PYTHONUNBUFFERED=1"], command="ros2 run codigo_gustavo original_listener", volumes={"C:\\Users\\Gustavo\\Dropbox\\Doutorado_Gustavo\\Quinto Semestre\\Backup Docker Containers\\QUENTE\\pós_segunda_reuniao\\teste": {'bind': '/teste', 'mode': 'rw'}})
client.containers.run("original_listener", name="listener", hostname="listener", detach=True, environment=["PYTHONUNBUFFERED=1"], command="ros2 run codigo_gustavo listener")
my_network.connect("listener")
print(container_listener)

for i in range (1):
    # tag = "talker_"+str(i)
    tag = "talker"
    print ("Imagem: "+tag)
    container_talker = client.images.build(path="./", dockerfile="Dockerfile_ROS", tag=tag)
    print ("Run: "+tag)
    client.containers.run(tag, name=tag, detach=True, environment=["PYTHONUNBUFFERED=1"], command="ros2 run codigo_gustavo talker")
    my_network.connect("talker")
    print(container_talker)


print ("Imagem Modelo:")
# container_listener = client.images.build(path="./", dockerfile="Dockerfile_ROS", tag="original_listener", squash=True)
container_modelo = client.images.build(path="./", dockerfile="Dockerfile_NETLOGO", tag="modelo")
# listener:
#     container_name: listener
#     build:
#       context: "./"
#       dockerfile: Dockerfile_ROS
#     environment:
#       - "PYTHONUNBUFFERED=1"
#     command: ros2 run codigo_gustavo listener
#     networks:
#       - my_network
print ("Run Modelo:")
client.containers.run("modelo", name="modelo", detach=True, environment=["PYTHONUNBUFFERED=1"], volumes={"C:\\Users\\Gustavo\\Dropbox\\Doutorado_Gustavo\\Quinto Semestre\\Backup Docker Containers\\QUENTE\\pós_segunda_reuniao\\teste": {'bind': '/teste', 'mode': 'rw'}}, command="python /teste/11ga_netlogo.py")
# client.containers.run("modelo", name="modelo", detach=True, environment=["PYTHONUNBUFFERED=1"], volumes={"C:\\Users\\Gustavo\\Dropbox\\Doutorado_Gustavo\\Quinto Semestre\\Backup Docker Containers\\QUENTE\\pós_segunda_reuniao\\teste": {'bind': '/teste', 'mode': 'rw'}}, command="tail -f /dev/null")
my_network.connect("modelo")
print(container_modelo)