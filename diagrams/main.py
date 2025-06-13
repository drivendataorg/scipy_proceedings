from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod
from diagrams.generic.storage import Storage
from diagrams.programming.framework import Django
from diagrams.generic.place import Datacenter

graph_attr = {
    "rankdir": "LR",  # left-to-right layout
    "dpi": "300",     # print-quality resolution
}

with Diagram("", show=True, graph_attr=graph_attr):
    user = Storage("Video or Image Data")
    with Cluster("Zamba Cloud"):
        with Cluster("Web Server"):
            web = Django("Zamba Cloud\nWeb App")
        with Cluster("Cloud Storage"):
            storage = Datacenter("Object Storage")
        with Cluster("Kubernetes Cluster"):
            job = Pod("Inference or\nTraining Job")

    user >> web
    web >> storage
    storage >> job
