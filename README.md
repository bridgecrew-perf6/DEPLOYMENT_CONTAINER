# VS_DEPLOYMENT_CONTAINER
- This project is structured to run in a Visual Studio Code Remote Container.
- Clone the repository.
- The root folder structure will look like this.  
```shell
.
├── buildingimage
│   ├── Dockerfile
│   ├── main.py
│   ├── model_config.py
│   └── requirements.txt
├── docker-compose.yml
├── training
│   ├── training_fashionmnist.ipynb
│   └── training_mnist.ipynb
└── volume
    ├── data
    │   ├── fashionmnist-mapping.json
    │   ├── images
    │   │   ├── image (1).jpg
    │   │   ├── image (2).jpg
    │   │   ├── image.jpg
    │   │   ├── images.jpeg
    │   │   ├── img_13.jpg
    │   │   ├── img_1.jpg
    │   │   ├── img_4.jpg
    │   │   ├── img_5.jpg
    │   │   ├── img_6.jpg
    │   │   └── Screenshot from 2022-04-02 17-28-15.png
    │   └── mnist-mapping.json
    └── model
        ├── fashionmnist
        │   └── 1
        │       ├── assets
        │       ├── saved_model.pb
        │       └── variables
        │           ├── variables.data-00000-of-00001
        │           └── variables.index
        ├── mnist
        │   └── 2
        │       ├── assets
        │       ├── saved_model.pb
        │       └── variables
        │           ├── variables.data-00000-of-00001
        │           └── variables.index
        └── models.config

```

- Before opening this folder please make sure that you have docker running on your system.
- Once docker is there and running open the folder in VS code.
- The moment you open this folder one extension of development remote container will automatically be given to install.
- Make sure you install and then click to rebuild the container.
- The project will now be running inside a remote container.  

## Building Image [OPTIONAL STEP]
- The image of flask application is already build and pushed to docker hub.  
- [Image on docker hub](https://hub.docker.com/r/trv30/flaskapp)
- This image is build with running the following commands

```shell
docker build -t trv30/flaskapp:latest buildingimage
```
- It is an optional step to rebuild the image on local.
- Again it is not required as the images will be pulled while running the other step.

## Application Running and Testing Steps
- Open a new terminal in vs code and run this command
```shell
docker-compose up
```
- The services named modelservice (tensorflow serving) and flaskapi will start running.
- You can test the service through Command line or postman.
## API Hit With Comandline  
```shell
curl -d '{"model_name": "mnist", "image": "img_1.jpg"}'     -H 'Content-Type: application/json'     -X POST http://0.0.0.0:5000/prediction
```
- Once hitting this request you will get response like this

```shell
{"Final Prediction":{"class":"two","confidence":1.0}}
```
- As it was test on mnist with images stored inside
```shell
volume/data/images/
```
- More images tested like this provided it should be present inside this folder
- This application supports multiple model similar hit to fashionmnist can also be given like this  

```shell
curl -d '{"model_name": "fashionmnist", "image": "image (2).jpg"}'     -H 'Content-Type: application/json'     -X POST http://0.0.0.0:5000/prediction
```
- Response as this  
```shell
{"Final Prediction":{"class":"Shirt","confidence":1.0}}
```
## POSTMAN SNAPSHOT
![alt text](https://raw.githubusercontent.com/Trajvoid/VS_DEPLOYMENT_CONTAINER/main/postman_snapshot.png)
