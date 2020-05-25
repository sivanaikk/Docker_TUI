import os
import webbrowser as wb

os.system("tput setaf 1")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
os.system("tput setaf 4")
name = "\"      DOCKER TUI\""
os.system("echo {0} | figlet -f smmono12 ".format(name))
os.system("tput setaf 118 ")
os.system("echo   DOCKER TERMINAL USER INTERFACE| figlet -f wideterm")
os.system("tput setaf 10")
print("\t\t\t\t\t\t\t\t...Do things of docker with a click")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")


def list(num):
    if(num==1):
        print("\n\nThese are all the active containers")
        os.system("sudo docker ps")
    elif(num==2):
        print("\n\nThese are all the containers")
        os.system("sudo docker ps -a")        
    elif(num==3):
        print("...These are all the Images you have...")
        return(os.system("sudo docker images"))
    elif(num==4):
        print("These are all the networks you have .....")
        os.system("sudo docker network ls")
    elif(num==5):
        print("These are all the bridge networks .... ")
        os.system("sudo docker network ls -f driver=bridge")
    elif(num==6):
        print("These are all the volumes ....")
        os.system("sudo docker volume ls")
    
    
        

#list(3)

def container(con,name):
    if(con==1):
        print("container attached")
        os.system("sudo docker attach {0}".format(name))
    elif(con==2):
        os.system("sudo docker stop {0}".format(name))
    elif(con==3):
        os.system("sudo docker start {0}".format(name))
    elif(con==4):
        os.system("sudo docker rm -f {0}".format(name))
    elif(con==5):
        os.system("sudo docker logs -f {0}".format(name))
    elif(con==6):
        command=input("Enter the complete command to execute : ")
        os.system("sudo docker exec {0} {1}".format(name,command))
    elif(con==7):
        os.system("sudo docker restart {0}".format(name))
    elif(con==8):
        os.system("sudo docker pause {0}".format(name))
    elif(con==9):
        os.system("sudo docker unpause {0}".format(name))
    elif(con==10):
        os.system("sudo docker wait {0}".format(name))
    elif(con==11):
        os.system("sudo docker kill {0}".format(name))
    elif(con==12):
        image_name = input("Enter the IMAGE NAME to create:")
        os.system("sudo docker commit {0} {1} ".format(name,image_name))
    elif(con==13):
        os.system("sudo docker inspect {0}".format(name))



def image_fun(img,name):
    if(img==1):
        os.system("vim Dockerfile")
    elif(img==2):
        pwd = os.system("pwd")
        print("YOU ARE HERE : {0}".format(pwd))
        path = input("Enter the absolute path to Dockerfile : ")
        os.system("sudo docker build -t {0} {1} ".format(name,path))
    elif(img==3):
        os.system("sudo docker history {0}".format(name))
    elif(img==4):
        os.system("sudo docker rmi {0}".format(name))
    elif(img==5):
        new_image_name = input("Enter the new image name : ")
        os.system("sudo docker tag {0} {1}".format(name,new_image_name))
    elif(img==6):
        tar_name = input("Enter the tar name you want to save as wit .tar extension : ")
        os.system("sudo docker save {0} -o {1}".format(name,tar_name))
    elif(img==7):
        os.system("sudo docker load -i {0}".format(name))
    elif(img==8):
        os.system("sudo docker pull {0} ".format(name))
        


def push_image():
    list(4)
    image = input("Enter the image name : ")
    os.system("sudo docker login")
    os.system("sudo docker push {0} ".format(image))


def network_fun(net,name):
    if net==1:
        os.system("sudo docker network create {0}".format(name))
    elif net==2:
        os.system("sudo docker network create --driver bridge {0}".format(name))
    elif net==3:
        os.system("sudo docker network inspect {0}".format(name))
    elif net==4:
        list(3)
        image=input("Docker image you need to run : ")
        con_name=input("Container Name : ")
        os.system("sudo docker run -dit --network {0} --name {1} {2}".format(name,con_name,image))
        print("Your container is running in detached mode :")
        fg = int(input("Enter 22 :To attach container\nEnter 11:To continue ... : "))
        if(fg==22):
            container(1,name)
        elif(fg==11):
            print("Running as detached..") 
    elif net==5:
        con_name=input("Enter the container name : ")
        os.system("sudo docker network connect {0} {1}".format(name,con_name))
    elif net==6:
        con_name=input("Enter the container name : ")
        os.system("sudo docker network disconnect {0} {1}".format(name,con_name))
    elif net==7:
        list(3)
        image=input("Docker image you need to run : ")
        port = int(input("Enter the port to expose : "))
        os.system("sudo docker run -dit -p {0}:80 --name {1} {2}".format(port,name,image))
        print("Your container is running in detached mode :")
        fg = int(input("Enter 22 :To attach container\nEnter 11:To continue ... : "))
        if(fg==22):
            container(1,con_name)
        elif(fg==11):
            print("Running as detached..") 
    elif net==8:
        con_name = input("Enter the container name :")
        list(3)
        image=input("Docker image you need to run : ")
        port = int(input("Enter the port to expose : "))
        os.system("sudo docker run -dit -p {0}:80  --name {1} --network {2} {3}".format(port,con_name,name,image))
        print("Your container is running in detached mode :")
        fg = int(input("Enter 22 :To attach container\nEnter 11:To continue ... : "))
        if(fg==22):
            container(1,con_name)
        elif(fg==11):
            print("Running as detached..")
    elif net==9:
        con_name = input("Enter the container name to create :")
        list(3)
        image=input("Docker image you need to run : ")
        os.system("sudo docker run -dit --link {0} --name {1} {2}".format(name,con_name,image))
    elif net==10:
        command = "\"{{.NetworkSettings.IPAddress}}\""
        os.system("sudo docker container inspect --format {1} {0}".format(name,command))
    elif net==11:
        os.system("sudo docker network rm {0}".format(name))

    
def volume_fun(vol,name):
    if vol==1:
        os.system("sudo docker volume create {0}".format(name))
    elif vol==2:
        os.system("sudo docker volume inspect {0}".format(name))
    elif vol==3:
        list(3)
        image=input("Docker image you need to run : ")
        con_name=input("Container Name : ")
        mount_path=input("Enter the path where to mount : ")
        os.system("sudo docker run -dit -v {0}:{1} --name {2} {3}".format(name,mount_path,con_name,image))
        print("Your container is running in detached mode :")
        fg = int(input("Enter 22 :To attach container\nEnter 11:To continue ... : "))
        if(fg==22):
            container(1,con_name)
        elif(fg==11):
            print("Running as detached..")
    elif vol==4:
        list(3)
        image=input("Docker image you need to run : ")
        con_name=input("Container Name : ")
        mount_path=input("Enter the path where to mount : ")
        port=input("Enter the port : ")
        os.system("sudo docker run -dit -v {0}:{1} -p {4}:80  --name {2} {3}".format(name,mount_path,con_name,image,port))
        print("Your container is running in detached mode :")
        fg = int(input("Enter 22 :To attach container\nEnter 11:To continue ... : "))
        if(fg==22):
            container(1,con_name)
        elif(fg==11):
            print("Running as detached..")
    elif vol==5:
        list(3)
        image=input("Docker image you need to run : ")
        con_name=input("Container Name : ")
        mount_path=input("Enter the path where to mount : ")
        os.system("sudo docker run -dit -v {0}:{1} --name {2} {3}".format(name,mount_path,con_name,image))
        print("Your container is running in detached mode :")
        fg = int(input("Enter 22 :To attach container\nEnter 11:To continue ... : "))
        if(fg==22):
            container(1,con_name)
        elif(fg==11):
            print("Running as detached..")
    elif vol==6:
        list(3)
        image=input("Docker image you need to run : ")
        con_name=input("Container Name : ")
        mount_path=input("Enter the path where to mount : ")
        port=input("Enter the port : ")
        os.system("sudo docker run -dit -v {0}:{1} -p {4}:80  --name {2} {3}".format(name,mount_path,con_name,image,port))
        print("Your container is running in detached mode :")
        fg = int(input("Enter 22 :To attach container\nEnter 11:To continue ... : "))
        if(fg==22):
            container(1,con_name)
        elif(fg==11):
            print("Running as detached..")
    elif vol==7:
        os.system("sudo docker volume rm {0}".format(name))

def dockerfile_fun(df,path):
    if df==1:
        image_name = input("Enter the image name : ")
        os.system("sudo docker build -t {0} {1} ".format(image_name,path))

def dockercompose_fun(dc,path):
    if dc==1:
        os.system("cd ./Dockercompose/{0} && sudo docker-compose up".format(path))

while True : 
    os.system("tput setaf 11")
    print("....MAIN MENU.....")
    print("1.Docker Container\n2.Docker Images\n3.Docker Network\n4.Docker Volume\n5.Some Dockerfiles\n6.Some Docker Compose files\n\n\n")
    print("Enter 0 to terminate ")
    os.system("tput setaf 4")
    choice = int (input("Select the Option : "))
    os.system("tput setaf 7")
    if(choice==0):
        exit()

    elif(choice==1):
        while True :
            os.system("tput setaf 51")
            os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Docker Container.")
            os.system("tput setaf 120")
            print("..... DOCKER CONTAINER MENU  .....")
            print("Enter 1:To run a container\nEnter 2:To stop running container\nEnter 3:To start the stopped container\nEnter 4:To remove container\nEnter 5:To list all active containers")
            print("Enter 6:To list all containers\nEnter 7:To attach a container\nEnter 8:To show logs of container\nEnter 9:Execute a new process in an existing container\nEnter 10:To restart a container")
            print("Enter 11:To pause a container\nEnter 12:To unpause a container\nEnter 13:To make container to wait\nEnter 14:To kill a container\nEnter 15:To create a image(commit) from container\nEnter 16:To inspect a container\n\n\nEnter 0:To return to main menu\nEnter 1234: to terminate program\n")
            os.system("tput setaf 9")
            print("Check the DOCKER VOLUME Menu To see docker run command with more ..options.. \n")
            os.system("tput setaf 7")
            run = int (input("Select the option from the CONTAINER MENU :"))
            if(run==1):
                list(3)
                image=input("Docker image you need to run : ")
                name=input("Container Name : ")
                os.system("sudo docker run -dit --name {0} {1}".format(name,image))
                print("Your container is running in detached mode :")
                fg = int(input("Enter 22 :To attach container\nEnter 11:To continue ... : "))
                if(fg==22):
                    container(1,name)
                elif(fg==11):
                    print("Running as detached..")         
            elif(run==2):
                list(1)
                name=input("Enter CONTAINER NAME : ")
                container(2,name)
            elif(run==3):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(3,name)
            elif(run==4):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(4,name)
            elif(run==5):
                list(1)      
            elif(run==6):
                list(2)
            elif(run==7):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(1,name)
            elif(run==8):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(5,name)
            elif(run==9):
                list(1)
                name=input("Enter CONTAINER NAME : ")
                container(6,name)
            elif(run==10):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(7,name)
            elif(run==11):
                list(1)
                name=input("Enter CONTAINER NAME : ")
                container(8,name)
            elif(run==12):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(9,name)
            elif(run==13):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(10,name)
            elif(run==14):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(11,name)
            elif(run==15):
                list(2)
                name=input("Enter CONTAINER NAME : ")
                container(12,name)
            elif(run==16):
                list(2)
                name = input("Enter the CONTAINER NAME : ")
                container(13,name)

            elif(run==0):
                print("Returning to main menu ......")
                break
            elif(run==1234):
                exit()
            else : 
                print("Enter the correct option..")
            enter = input("\n\nPress ENTER to clear output and continue with docker container menu ....")
            os.system("clear")

    elif(choice==2):
        while True :
            os.system("tput setaf 51")
            os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Docker Image.")
            os.system("tput setaf 120")
            print("..... Docker IMAGE MENU .....")
            print("Enter 1:To Create a Dockerfile\nEnter 2:To build from Dockerfile\nEnter 3:To list all Images\nEnter 4:To check history of image \nEnter 5:Remove an image")
            print("Enter 6:To rename a Image\nEnter 7:To Export the image to a local storage\nEnter 8:To Import the image from local storage\nEnter 9:To Pull an image from Docker Hub\nEnter 10:To push a image to Docker Hub\nEnter 11:To remove dangling images\n\n\nEnter 0:To return to main menu\nEnter 1234: to terminate program\n")
            os.system("tput setaf 7")
            image = int (input("Enter the option from IMAGE MENU :"))
            if(image==1):
                os.system("pwd")
                print("YOU ARE HERE")
                path = input("Enter the absolute path where you want to create Dockerfile : ")
                image_fun(1,path)
            elif(image==2):
                image_name = input("Enter the name for image : ")
                image_fun(2,image_name)
            elif(image==3):
                list(3)
            elif(image==4):
                list(3)
                image_name = input("Enter the image name : ")
                image_fun(3,image_name)
            elif(image==5):
                list(3)
                image_name = input("Enter the image name : ")
                image_fun(4,image_name)
            elif(image==6):
                list(3)
                image_name = input("Enter the image name to rename : ")
                image_fun(5,image_name)
            elif(image==7):
                list(3)
                image_name = input("Enter the name of image you want to export : ")
                image_fun(6,image_name)
            elif(image==8):
                print("The file must be in this directory .. ")
                os.system("pwd")
                saved_file = input("Enter the file name")
                image_fun(7,saved_file)
            elif(image==9):
                list(3)
                image_name = input("Enter complete name of the image with tag : ")
                image_fun(8,image_name)
            elif(image==10):
                print("You must have docker hub repo\nYour name of the image must be in the format of <docker id>/<image_name>")
                push=int(input("Enter 1:To create a docker hub account\nEnter 2:To change the name of the image :\nEnter 3: If the two requirements not satisfy to push : "))
                if(push==1):                
                    wb.open("https://hub.docker.com/")
                    print("Create the account at hub.docker.com")
                    #push_image()
                elif(push==2):
                    list(3)
                    image_name = input("Enter the image name to rename : ")
                    image_fun(5,image_name)
                    push_image()
                elif(push==3):
                    print("Create a Docker Hub Repository  : ")
                    wb.open("https://hub.docker.com/")
                    print("Create the account at hub.docker.com")
                    print("Rename tha image : ")
                    list(3)
                    image_name = input("Enter the image name to rename : ")
                    image_fun(5,image_name)
                    push_image()
            elif(image==11):
                list(3)
                confirm=input("Enter 1:To Confirm\nEnter 0:To Cancel : " )
                if confirm==1:
                    os.system("docker rmi $(docker images -q -f dangling=true)")
                elif confirm==0:
                    print("Returning ....")
            elif(image==0):
                print("Returning to Main Menu ....")
                break
            elif(image==1234):
                exit()
            else:
                print("Enter the correct option : ")
            enter = input("\n\nPress ENTER to clear output and continue with docker image menu ....")
            os.system("clear")            

    elif(choice==3):
        while True:
            os.system("tput setaf 51")
            os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Docker Network.")
            os.system("tput setaf 120")
            print("..... Docker Network Menu.....")
            print("Enter 1:To see all the networks\nEnter 2:To create a network(host)\nEnter 3:To create a bridge network\nEnter 4:To inspect a network\nEnter 5:To run a container with a network")
            print("Enter 6:To connect to a network\nEnter 7:To disconnect from network\nEnter 8:To run a container by expose\nEnter 9:To run a container with network and expose\nEnter 10:To run a container and link with other container")
            print("Enter 11:To get the IP Address of container\nEnter 12:To remove a network\n\n\nEnter 0:To return to main menu\nEnter 1234:To terminate the program")
            os.system("tput setaf 7")
            network = int(input("Enter the option from NEWORK VOLUME : "))
            if(network == 1):
                list(4)
            elif(network == 2):
                list(4)
                network_name = input("Enter the network name :")
                network_fun(1,network_name)
            elif(network == 3):
                list(4)
                network_name = input("Enter the network name :")
                network_fun(2,network_name)
            elif(network==4):
                list(4)
                network_name = input("Enter the network name :")
                network_fun(3,network_name)
            elif(network==5):
                list(4)
                network_name = input("Enter the network name :")
                network_fun(4,network_name)
            elif(network==6):
                list(4)
                network_name = input("Enter the network name :")
                network_fun(5,network_name)    
            elif(network==7):
                list(4)
                network_name = input("Enter the network name :")
                network_fun(6,network_name) 
            elif(network==8):
                con_name = input("Enter the container name :")
                network_fun(7,con_name) 
            elif(network==9):
                list(4)
                network_name = input("Enter the network name :")
                network_fun(8,network_name)
            elif(network==10):
                list(1)
                other_con = input("Enter the name of existing container :")
                network_fun(9,other_con)
            elif(network==11):
                list(2)
                con_name = input("Enter the container name to get IP Address :")
                network_fun(10,con_name)
            elif(network==12):
                list(4)
                network_name=input("Enter the network name : ")
                network_fun(11,network_name)                
                
            elif(network==0):
                print("Returning to Main Menu ....")
                break
            elif(network==1234):
                exit()

            else:
                print("Enter the correct option : ")
            enter = input("\n\nPress ENTER to clear output and continue with docker network menu ....")
            os.system("clear")
       
    elif(choice==4):
        while True:
            os.system("tput setaf 51")
            os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Docker Volume.")
            os.system("tput setaf 120")
            print("Docker Volume Menu ...")
            print("Enter 1:To list all Volumes\nEnter 2:To create a Volume\nEnter 3:To inspect a volume\nEnter 4:To run a container with a volume\nEnter 5:To run a container with a volume and expose")
            print("Enter 6:To mount the local directory and launch a container\nEnter 7:To mount a local directory and launch a container and expose\nEnter 8:To remove a volume\n\n\nEnter 0:To return to main menu\nEnter 1234: to terminate program\n")
            os.system("tput setaf 7")
            
            volume=int(input("Enter the option from VOLUME MENU : "))
            if(volume==1):
                list(6)
            elif(volume==2):
                vol_name = input("Enter the Volume Name :")
                volume_fun(1,vol_name)
            elif(volume==3):
                list(6)
                vol_name = input("Enter the Volume Name : ")
                volume_fun(2,vol_name)
            elif(volume==4):
                list(6)
                vol_name = input("Enter the Volume Name : ")
                volume_fun(3,vol_name)
            elif(volume==5):
                list(6)
                vol_name = input("Enter the Volume Name : ")
                volume_fun(4,vol_name)
            elif(volume==6):
                dir_path = input("Enter the absolute path of directory : ")
                volume_fun(5,dir_path)
            elif(volume==7):
                dir_path = input("Enter the absolute path of directory : ")
                volume_fun(6,dir_path)
            elif(volume==8):
                list(6)
                vol_name=input("Enter the volume name : ")
                volume_fun(7,vol_name)

            elif(volume==0):
                print("Returning to main menu ......")
                break
            elif(volume==1234):
                exit()
            else : 
                print("Enter the correct option..")
            enter = input("\n\nPress ENTER to clear output and continue with docker Volume Menu ....")
            os.system("clear")

    elif(choice==5):
        while True:
            os.system("tput setaf 51")
            os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Dockerfiles.")
            os.system("tput setaf 120")
            print("Dockerfiles Menu ...")
            print("Enter 1:To view some Dockerfile\nEnter 2:To build from Dockerfile\n\n\nEnter 0:To return to main menu\nEnter 1234: to terminate program\n")
            os.system("tput setaf 7")
            dockerfile=int(input("Enter the option :"))
            if dockerfile==1:
                while True:
                    os.system("tput setaf 51")
                    os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Dockerfiles View.")
                    os.system("tput setaf 120")
                    print("Dockerfile View menu")
                    print("Enter 1:python3\nEnter 2:Deep Learning\n\n")
                    os.system("tput setaf 7")
                    file = int(input("Select the dockerfile :"))
                    if file == 1:
                        os.system("cat ./Dockerfiles/python3/Dockerfile")
                    elif file == 2:
                        os.system("cat ./Dockerfiles/Deep_Learning/Dockerfile")
                    elif file == 0:
                        print("Returning...")
                        break
                    else :
                        print("Enter correct option ")
                    enter = input("\n\nPress ENTER to clear output and continue with Dockerfile View Menu ....")
                    os.system("clear")        
            elif dockerfile==2:
                while True:
                    os.system("tput setaf 51")
                    os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Dockerfiles Build.")
                    os.system("tput setaf 120")
                    print("Dockerfile build menu")
                    print("Enter 1:To build python3 Image\nEnter 2:To build Deep Learning Image\n\n\nEnter 0:To return to main menu\nEnter 1234: to terminate program\n")
                    os.system("tput setaf 7")
                    file = int(input("Select the dockerfile to build :"))
                    if file == 1:
                        path="./Dockerfiles/python3/"
                        dockerfile_fun(1,path)
                    elif file == 2:
                        path="./Dockerfiles/Deep_Learning/"
                        dockerfile_fun(1,path)
                    elif file == 0:
                        print("Returning...")
                        break
                    elif file==1234:
                        exit()
                    else :
                        print("Enter correct option ")
                    enter = input("\n\nPress ENTER to clear output and continue with Dockerfile View Menu ....")
                    os.system("clear") 
            #elif dockerfile==3:
            elif(dockerfile==0):
                print("Returning to main menu ......")
                break
            elif(dockerfile==1234):
                exit()
            else : 
                print("Enter the correct option..")
            enter = input("\n\nPress ENTER to clear output and continue with Dockerfile Menu ....")
            os.system("clear") 

    elif(choice==6):
        while True:
            os.system("tput setaf 51")
            os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Docker Compose.")
            os.system("tput setaf 120")
            print("DockerComposes Menu ...")
            print("Enter 1:To view some Dockercompose files\nEnter 2:To setup from Dockercompose\n\n\nEnter 0:To return to main menu\nEnter 1234: to terminate program\n")
            os.system("tput setaf 7")
            Dockercompose=int(input("Enter the option :"))
            if Dockercompose==1:
                while True:
                    os.system("tput setaf 51")
                    os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Compose view")
                    os.system("tput setaf 120")
                    print("Dockercompose View menu")
                    print("Enter 1:Ghost Blogger Site\nEnter 2:Drupla\nEnter 3:Wordpress\nEnter 4:lamp server\n\n\nEnter 0:To return to docker compose view menu\nEnter 1234:To Terminate")
                    os.system("tput setaf 7")
                    file = int(input("Select the Dockercompose :"))
                    if file == 1:
                        os.system("cat ./Dockercompose/ghost/docker-compose.yml")
                    elif file == 2:
                        os.system("cat ./Dockercompose/drupal/docker-compose.yml")
                    elif file == 3:
                        os.system("cat ./Dockercompose/wordpress/docker-compose.yml")
                    elif file == 4:
                        os.system("cat ./Dockercompose/lamp/docker-compose.yml")
                    elif file == 0:
                        print("Returning...")
                        break
                    elif file == 1234:
                        exit()
                    else :
                        print("Enter correct option ")
                    enter = input("\n\nPress ENTER to clear output and continue with Dockercompose View Menu ....")
                    os.system("clear")        
            elif Dockercompose==2:
                while True:
                    os.system("tput setaf 51")
                    os.system("figlet -f cybermedium -d ./figletfonts40/fonts/ Dockercompose up.")
                    os.system("tput setaf 120")
                    print("Dockercompose build menu")
                    print("Enter 1:To setup ghost Blogging site\nEnter 2:To setup drupal\nEnter 3:To setup wordpress\nEnter 4:To setup lamp server\n\nEnter 0:To return to menu\nEnter 1234:To terminate\n")
                    os.system("tput setaf 7")
                    file = int(input("Select option to setup Dockercompose :"))
                    if file == 1:
                        path="ghost"
                        dockercompose_fun(1,path)
                    elif file == 2:
                        path="drupal"
                        dockercompose_fun(1,path)
                    elif file == 3:
                        path="wordpress"
                        dockercompose_fun(1,path)
                    elif file == 4:
                        path="lamp"
                        dockercompose_fun(1,path)
                    elif file == 0:
                        print("Returning...")
                        break
                    elif file == 1234:
                        exit()
                    else :
                        print("Enter correct option ")
                    enter = input("\n\nPress ENTER to clear output and continue with Dockercompose View Menu ....")
                    os.system("clear") 
            #elif Dockercompose==3:
            elif(Dockercompose==0):
                print("Returning to main menu ......")
                break
            elif(Dockercompose==1234):
                exit()
            else : 
                print("Enter the correct option..")
            enter = input("\n\nPress ENTER to clear output and continue with Dockercompose Menu ....")
            os.system("clear")  