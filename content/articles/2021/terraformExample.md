Title: How to deploy an Apache Server in a VPC cluster on AWS using Terraform
Date: 2021-10-28 13:42
Modified: 2021-10-28 13:42
Category: Infrastructure
Tags: AWS, terraform, deployment, IAAC


This post shows how to create an live running Apache webserver on [AWS](https://aws.amazon.com) using [terraform](https://terraform.io). The advantage of this method is to be able to use a repeatable method to spin up infrastructure for software deployment as the business grows. It also creates a clear, detailed  and easily transferrable information about the deployment architecture and the infrastructure in use at each point in time for any interested developer in the organization.


##Setup AWS credentials
Please follow this [link](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html) to set AWS credentials and access keys. A json file is provided at the end, download this file to a path called to a path called **TF_DATA_DIR** as **/TF_DATA_DIR/key.json** on your computer and put this directory in the system enviroment variables. .

## Create terraform file and load AWS credentials
Create a file called **main.tf** in your favorite text editor, and save it to a path on your computer. This file contains all terraform commands and is to be wrriten in Hashicorp's language format. The first step is to load the AWS credentials created in the previous step. This path must be in directory different from  **TF_DATA_DIR** which could contain sensitive credentials that we dont want to expose for example with a ``` git push ```

```
locals {
  json_data = jsondecode(file("${TF_DATA_DIR}/key.json"))
}
```

Terraform provides a [jsondecode](https://www.terraform.io/docs/language/functions/jsondecode.html) function that is useful for loading json files to the variable local, which can then me accessed during execution.

# Create a provider
The next step is to declare [AWS](aws.amazon.com) as the provider. The AWS credentials provided below will be used for authentication when accessing the aws api to create the needed remote resources.

```
provider "aws" {
  region = "us-east-1"
  access_key = local.json_data.aws_key
  secret_key = local.json_data.aws_secret
}
```

# Create a VPC
Here we create a virtual private cloud, a sort of virtual network that is private though sitting on the cloud, it helps us to define a range of static ip addresses that we can assign to remote resources.

```
resource "aws_vpc" "office_network" {
  cidr_block = "10.0.1.0/28"
  tags = {
    Name = "OfficeNetwork"
  }
}
```

# Create an Internet gateway
We create an Internet gateway to reserve a public ip address that we can use to send and recieve traffic to the internet. This is attached to the previously created VPC.

```
resource "aws_internet_gateway" "company_public_gateway" {
  vpc_id = aws_vpc.office_network.id
  tags = {
    Name = "CompanyPublicGateway"
  }
}
```

# Create a custom route table
Each VPC must have a route table attached to it to define where hosts send ip packets (routing). There is a default main route table but we can choose to explicitly define a route table as we wish and add routes. [Each subnet in the VPC must be associated to a single route table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html).

```
resource "aws_route_table" "company_route_table" {
  vpc_id = aws_vpc.office_network.id   
      #send all traffic from this subnet to the internet gateway
  route  {
      cidr_block = "10.0.1.0/24"
      gateway_id = aws_internet_gateway.company_public_gateway.id
    }
      #send all IPV6 traffic to the internet gateway
  route {
      ipv6_cidr_block        = "::/0"
      gateway_id = aws_internet_gateway.company_public_gateway.id
    }
  tags = {
    Name = "CompanyRouteTable"
  }
}
```

# Create a subnet
Next is to create a subnet within which the host running the apache server will sit, this assumes a private network that isolates server traffic that can be internet facing and other devices local to the network, a good practice for security reasons :) We indicate the availability zone when this option exists to make sure all devices are deployed in the same availability zone. We need to have all devices to be deployed in the same availability zone.

```
resource "aws_subnet" "office_subnet_pcs" {
  vpc_id     = aws_vpc.office_network.id
  cidr_block = "10.0.1.0/28"
  availability_zone = "us-east-1a" 
  tags = {
    Name = "OfficeSubNetPCS"
  }
}
```

# Associate subnet with route table
Here we associate the newly created subnet with the previously created route table. we refrence directly the **subnet.id** and **route_table.id** respectively.


```
resource "aws_route_table_association" "officesubnet_routetable_association" {
  subnet_id      = aws_subnet.office_subnet_pcs.id
  route_table_id = aws_route_table.company_route_table.id
}
```
# Create security group and allow only ports 22, 443, 80
The next syntax is to create an AWS security group to allow specific ports to communicate with hosts on the internet. This security group applies to all hosts on our VPC and allows them to communicate with any host on the internet. Note that we can allow only a specific list of specific ipv4 addresses in the **cidr_blocks** or ipv6 addresses  in the **ipv6_cidr_blocks** for more security.


```
resource "aws_security_group" "allow_web_traffic" {
  name        = "allow_web_traffic"
  description = "Allow web traffic for ssh http and tls"
  vpc_id      = aws_vpc.office_network.id
 
  #specifies a range of ports to be allowed and in this case Tcp 443:447
  # allows all ip addresses to access into this port since it is a web server
  # any internet address can access into this port

  ingress = [
    {
      description      = "HTTPS Traffic"
      from_port        = 443
      to_port          = 443
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
      prefix_list_ids = []
      security_groups = []
      self = false
    },
    {
      description      = "HTTP Traffic"
      from_port        = 80
      to_port          = 80
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
      prefix_list_ids = []
      security_groups = []
      self = false
    },
    {
      description      = "SSH Traffic"
      from_port        = 22
      to_port          = 22
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
      prefix_list_ids = []
      security_groups = []
      self = false
    }
  ]
  
  #allow all ports in the egress direction for any protocol -1
  egress = [
    {
     description      = "for all outgoing traffics"
      from_port        = 0
      to_port          = 0
      protocol         = "-1"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
      prefix_list_ids = []
      security_groups = []
      self = false
    }
  ]

  tags = {
    Name = "Allow_Web-HTTPS_HTTP_SSH"
  }
}
```
# Create a Network Interface
We create a network interface for a one of the local ipv4 addresses in the subnet. This interface will be used to the host that will run the apache server and contains the security group previously created that allows traffic to reach it. 
```
resource "aws_network_interface" "office_webserver_nic" {
  subnet_id       = aws_subnet.office_subnet_pcs.id
  private_ips     = ["10.0.1.11"]
  security_groups = [aws_security_group.allow_web_traffic.id]
}
```
# Assign an elastic ip to the network interface
We will assign an [Amazon elastic ip](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html.office_webserver_nic.id)to the previously created network interface. Th Eip relies on the previously created internet gateway and must be assigned on a device in a subnet or vpc that has an internet gateway.

```
resource "aws_eip" "webserver_nic_elastic_ip" {
  vpc                       = true
  network_interface         = 
  associate_with_private_ip = "10.0.1.11"
  depends_on = [aws_internet_gateway.company_public_gateway]
}
```

# Create an ubuntu server on an aws instance and install enable apache on this server

This step relies on [pre-built Ubuntu images](https://cloud-images.ubuntu.com/locator/ec2/) on AWS called **AMI**. You can [choose another AMI from AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) on which to deploy your apache server, you should also choose an instance-type to act as the host. The **instance-type** will differ in the properties such as CPU, memory, GPU etc. As a general rule the more powerful the instance the more expensive your installation. A very important step here is the creation of a key that is used to access the instance by terraform. **"rootkey"** is a **.ppk** file that is created on AWS using this [method](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair). Save this file somewhere in  the same path set in the enviromental variable **TF_DATA_DIR** with name **rootkey.ppk**. The rest of the code is used to initialize the Ubuntu OS, install apache and use **Systemctl** to start the apache service.


```
resource "aws_instance" "web_server_1" {
  ami           = "ami-0747bdcabd34c712a"
  instance_type = "t2.micro"
  availability_zone = "us-east-1a" 
  key_name = "rootkey"
  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.office_webserver_nic.id
  }
  #Tell terraform on the deployment of this server to run commands to install Apache on this server
  #Update ubuntu OS
  #Install apache
  #Start apache service
  #You can install other packages here by command line
  #end with EOF
  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install apache2 -y
              sudo systemctl start apache2
              sudo bash -c 'echo This is a web server > /var/www/html/index.html'
              EOF

  tags = {
    Name = "Webserver1"
  }
}
```

# Run everything 
We use init to start execution and get provider (in this case AWS) api plugins.

```
terraform init
```
We can get current state of resources with a plan command or to see what a change in the infrastructure could look like before making changes permanent.

```
terraform plan
```
To make apply changes to resources permanent.

```
terraform apply
```
Last but not least we can  destroy resources if we do not want to leave the infrastructure running forever to save cost. **Be careful with this command, it could delete all instances in your infrastructure and you should use it at the end of this tutorial to save costs if you do not want to incure running costs.** 

```
terraform destroy
```
# Conclusion

We have seen how we can use Terraform to create infrastructure on AWS using a [declerative syntax](https://www.terraform.io/docs/language/index.html). This makes infrastructure creation, management and replacement easy, fun and painless. The code used is available on [github.](https://github.com/yang2lalang/terraform_examples)

References:

[Terraform](https://learn.hashicorp.com/tutorials/terraform/aws-build)
[AWS](aws.amazon.com)
[FreeCodeCamp.org](https://youtu.be/SLB_c_ayRMo)
