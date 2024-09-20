# BentoML Tutorial

Files for working through the Bento ML tutorial. In this version, I used Docker and downloaded the Huggingface model to do a local and fully containerized app


## To Run
- First run ```python create_local_model.py``` to save a local model 
- Then follow the steps for building the docker container and running it on the [Tutorial](https://docs.bentoml.com/en/latest/guides/containerization.html)
    - Run ```bentoml build```
    - Run ```bentoml containerize summarization:latest```
    - Finally, run ```docker run --gpus all --rm -p 3000:3000 summarization:<tag>```
- Finall, you can run ```python test.py``` to test that the service is working