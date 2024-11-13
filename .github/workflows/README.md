# CNAB Bundle Build 
This Github workflow automates the building and publishing of the azure-vote CNAB (Cloud Native Application Bundle). 

# Key Steps
1. Checkout Repository
- This step allows the workflow to access the code in the GitHub repository. The step uses actions/checkout@v3 to clone the code in the repository into the current workflow environment.

2. Build CNAB Bundle and Publish to ACR
- This step builds CNAB and publishes it to Azure Container Registry (ACR). The step uses the action addnab/docker-run-action@v3 to run a Docker container with the specified parameters:
```yaml
    image: mcr.microsoft.com/container-package-app:latest # provides the tools and environment to build the CNAB
    options: -v /var/run/docker.sock:/var/run/docker.sock -v ${{ github.workspace }}:/data --entrypoint "/bin/bash" # options to specify when running the docker container, entrypoint is set to "/bin/bash" and -v mounts the Docker socket and Github workspace into the docker container

    run: |
            cd /data/samples/k8s-offer-azure-vote 
            echo ${{ secrets.ACR_TOKEN}} | docker login ${{ secrets.ACR_USERNAME }} -u testToken --password-stdin
            cpa buildbundle
# After running the docker container ACR_USERNAME and ACR_TOKEN (which can be found in Github Secret Variables) are used to login to docker, after changing directories to the azure-vote sample. The "cpa buildbundle" builds the CNAB specified in cd /data/samples/k8s-offer-azure-vote. 
```

# Note
ISV is required to increment the CNAB version if the current specified CNAB has been published through partner center.
