# Azure intro

**Intro to cloud computing and Azure**

<a href="https://youtu.be/g-wRTFf6zuM" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/azure/intro_cloud.png?raw=true" alt="intro to cloud computing" width="600">
</a>

<br/>

**Scaling and pricing**

<a href="https://youtu.be/Zwfguhx8Ufc" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/azure/scaling.png?raw=true" alt="scaling and pricing" width="600">
</a>

<br/>

**Azure fundamentals**

<a href="https://youtu.be/eVBC8DiR8N0" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/azure/architecture.png?raw=true" alt="fundamentals azure architecture" width="600">
</a>

<br/>


## On-premises vs cloud IT services

A company can hardly operate without various IT service components, which forms IT infrastructure of a company. Depending of the size of a company, the IT infrastructure can include various IT service components, and a data engineer can work with a smaller or larger part of the IT infrastructure. A data engineer should also understand basics of IT infrastructure as a datapipeline often involves integration of different components in a company's IT infrastructure.

Let's have a look at a simple example of a small e-commerce company. This company is selling clothes online and gather data such as warehouse stock levels, product prices and customer data etc from external data sources.

The company is renting a physical office. In one floor, it places two desktop computers to host the database server and web server. This floor needs physical security measures to prevent unauthorized access, and also air-conditioning to avoid overheat of the servers. This company employs a database administrator to manage the DB server and a web developer to develop its website. They work with laptops.

These laptops are connected to the two servers in a Local Area Network (LAN) so that these computers can communicate with each others. Apart from the LAN, additional networking setups are needed so that the DB server can receive inbound traffic from external data sources and consumers can access the website for online shopping.

The computers (hardware), applications for DB and web development installed on the computers (software), and networking devices connecting themselves and to the outside world form a simple example of IT infrastructure of this type of business.

  <img src="https://github.com/kokchun/assets/blob/main/azure/onprem_it.png?raw=true" alt="on premise IT" width="500">

## Why do we need cloud platform?

The on-premises IT infrastructure above requires an upfront cost to set up different computers and networking devices for the company to start operate. At the same time, the capacity of the two servers are relatively fixed and the company cannot react to varying inflow of data or customers browing its website. This results in downtimes as the company cannot scale up its IT infrastructure flexibly. These issues prompt companies to migrate to cloud IT infrastructure.

> [!Note]
> Cloud IT infrastructure is the delivery of IT services OVER THE INTERNET so that a company does not need to maintain physical hardwares and premisese as before

For example, the company can alternatively set up a cloud IT infrastructure as below. Instead of purchasing two server computers and placing them in a physical office, it can use cloud DB and web servers and pay for the actual usage of the servers. The DBA and web developer can connect to these cloud servers via internet. The benefits are:

- **cost efficiency** <br>
  the company now does not need to pay for the upfront cost to purchase the server computers, and extra cost to arrange a secure physical office to accomodate them.
- **scalability and availability** <br>
  cloud providers maintain many server computers behind the scenes and are able to scale up their IT services flexibly. In this case, the capacity of the cloud and web servers can be adjusted according to realtime needs. Downtimes of the company's website can thus be prevented, without the company purchasing more capable computers that are left idle during off-peak hours when less customers are browsing the website.

<img src="https://github.com/kokchun/assets/blob/main/azure/cloud_it.png?raw=true" alt="IT infrastructure on the cloud" width="500">

## What does Azure provide?

As a cloud platform provider with big market shares, Azure is providing a wide range of IT services via internet, including servers, storage and networking etc. Compared to on-premises IT infrastructure, companies now share some of the responsibilities to set up and maintain its IT infrastructure with cloud platform provider as Azure. How much of the responsibilities are shared depends on whether an IT service is offered as IaaS, PaaS or SaaS. This way of categorizing IT services is called shared responsibility model:

- **Infrastructure as Service (IaaS)** <br>
  If you create a virtual machine in Azure, you are using IaaS because you are responsible for everything apart from handling the physical hardware. For example, you need to choose the operation system, install and patch all softwares necessary for your work.
- **Platform as a Service (PaaS)** <br>
  With PaaS, developers can skip caring about the servers behind and focus on developing applications on Azure's servers behind the scenes. Azure App Service is a PaaS example, where developers can deploy apps without managing the infrastructure.
- **Software as a Service (SaaS)** <br>
  With SaaS, users can use Azure's softwares online. Azure AI services are examples of SaaS available on Azure.



## How does Azure provide services? 
Whenever you create an Azure resource, you often have to choose a region for this resource. So what are region and related geogrphical terms in Azure? And why are they related to how Azure is working as a cloud platform?

### Datacenters
The physical infrastructure of Azure are housed in buildings called datacenters. These datacenters store physical computer servers together with networking, power and cooling facilities. These facilities are arranged in racks. These physical infrastructure are providing IT services to Azure customers over internet.

**Datacenter racks**

<img src="https://github.com/kokchun/assets/blob/main/azure/rack.png?raw=true" alt="data center rack" width="300">


### Regions
A region is a geographical area that is composed of one or multiple datacenters that are close to each others. When creating an Azure resource, we often need to choose from which region we would like the resource to be created. Then Azure internally assigns workloads across datacenters in the region to ensure balanced workloads. 

🔍 [Checkout the map of all Azure regions](https://datacenters.microsoft.com/globe/explore?info=region_swedencentral)

### Availability zones
Some regions are divided into availability zones. Each availability zone contains one or multiple datacenters. These availability zones are isolated with each others in the sense that when one goes down, another can continue working. This prevents downtime faced by customers.    

>[!Note]
>Choice of region for an Azure resource is affected by many factors such as:
>- latency- Azure servers respond to end-users closer to a region
>- your availability target- regions with availability zones gurantee uptime to end-users

## How can you provision an IT service on Azure?

### Resource groups and resources
All IT services you pay for in Azure are called **resources**: virtual machines, databases, networking setups are all separate resources. Azure requires you to create a **resource group** to group created resources. With a good structure of resource groups and resources, one can manage resources more efficiently as one can, for example, grant access for or delete all resources within a resource group altogether.

### Subscriptions
Before creating resource groups and resources, you need to first create a **subscription** under your **account**. You can create multiple subscriptions under your accounts. Then, you can start creating resource groups and resources under different subscriptions. 

Subscription serves as a unit of billing and administration. A good structure of subscription facilitates billing and other administration tasks. For instance, if a company is working with development and production environments, which means that there is an IT infrastructure supporting each environment, it can create DEV and PROD subscription to host resources used in each environment separately. There is no rule on how to organize your subscriptions. Some companies may want to create separate subscriptions for different departments like sales, IT, logistics departments etc.

🔍 [More details on the hierarchy of account -> subscription -> resource group -> resource](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure?ns-enrollment-type=learningpath&ns-enrollment-id=learn.wwl.azure-fundamentals-describe-azure-architecture-services)

>[!Tip]
>Follow exercise 0.1 to create a subscription and resource group to include a VM as a resource


## Examples of Azure resources
One can build an IT infrastructure with different Azure resources, or combine them with IT services on-premises or provided by other cloud platforms. Below are some Azure resources serving different purposes in an IT infrastructure:

>[!Note]
>There are much more Azure resources serving other purposes, like networking. These will not be covered here. 

### Computing
- Virtual machine (VM) <br> 
  VM works similarly as a physical computer. You configure specifications like OS, CPU and RAM etc upon creating a VM resource. It can be used as a lift-and-shift cloud migration as a company does not need to change its existing IT infrastructure much if it only wants to move physical servers to virtual ones. 
- Azure Web App <br> 
  After you have locally developed a web application, you can deploy it to Azure App Service. Azure App Service provides the underlying servers to host your production web application as an Azure Web App, which is reachable by end-users online.
- Azure Functions <br>
  It's cost efficient to deploy your codes to Azure Functions if you would only like to run your codes when certain events triggers. For example, if you receive an email etc. It avoids provisioning resources when there is no need. 
- Azure Container Instances <br> 
  Azure Container Instances are used to spin up containerized applications. This is suitable when you have containerized applications requiring different operation systems. 

🔍 [More on Azure compute services](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/)


## Managing Azure resources
Image if you work alone and develop only locally on your laptop, your cost is the price of your laptop that you had paid. If your laptop is running scripts slowly, you can check things like the current usage of CPU and RAM to troubleshooting the performance issue. You do not need to worry about access control either as you are the only one who can open your laptop with your username and password. 

But if your are using IT services via Azure, how do you manage you Azure resources, for instances, regarding access control, monitoring cost and performance?


## Interacting with Azure 
You can create and manage Azure resources in different ways:

- GUI
  - [Azure portal](http://portal.azure.com): a web-based graphical user interface to interact with your Azure environments, as an alternative to command-line tools (i.e. writing commands)
- Command line tools
  - Azure CLI: uses Bash commands
  - Azure PowerShell: uses PowerShell commands
  - both can be installed locally and run in local shells,  or via Azure Cloud Shell, a web-based shell tool

>[!Note] 
>If you want to delete a resource group, then you can either use Azure CLI command:
>```
>az group delete -n RG01
>```
>or Azure PowerShell command:
>```
>Remove-AzResourceGroup -Name "RG01"
>```

- Infrastructure as Code (IaC) <br>
IaC refers to writing codes to define and deploy resources, making it possible to reproduce the same resources
  - Azure Resource Manager (ARM): Azure’s native service for deploying and managing resources using declarative syntax including:
    - ARM templates
    - Bicep files
  - Terraform: a popular third-party, multi-cloud CLI tool for IaC. Unlike ARM templates and Bicep files which are Azure-specific, Terraform can manage infrastructure across multiple cloud providers (Azure, AWS & GCP)



## Read more
- [pydantic docs](https://docs.pydantic.dev/latest/)

## Other videos