# HHA504_assignment_serverless
Deploy a Serverless Function, Create a Cron Job, and Explore Functions as a Service (FaaS)

**Note: I changed the name of the Repository from github-actions-schedule-email to HHA504_assignment_serverless after I posted the screenshots**
## 1. Deploy a Serverless Function

### GCP

1. Access the Google Cloud Console and create a Google Cloud Function.![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Access%20GCP%20Console%20and%20create%20a%20Google%20Cloud%20Function%20part%201.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Access%20GCP%20Console%20and%20create%20a%20Google%20Cloud%20Function%20part%202.png)
3. Deploy a similar function with an HTTP trigger in GCP.
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Deploy%20a%20similar%20function%20with%20an%20HTTP%20trigger%20in%20GCP%20part%200.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Deploy%20a%20similar%20function%20with%20an%20HTTP%20trigger%20in%20GCP%20Part%201.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Deploy%20a%20similar%20function%20with%20an%20HTTP%20trigger%20in%20GCP%20Part%202.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Deploy%20a%20similar%20function%20with%20an%20HTTP%20trigger%20in%20GCP%20Part%203.png)

### Azure

1. Azure Navigate to the Azure portal and create an Azure Function.
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Azure%20Navigate%20to%20the%20Azure%20portal%20and%20create%20an%20Azure%20Function%20Part%201.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Azure%20Navigate%20to%20the%20Azure%20portal%20and%20create%20an%20Azure%20Function%20Part%202.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Azure%20Navigate%20to%20the%20Azure%20portal%20and%20create%20an%20Azure%20Function%20Part%203.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Azure%20Navigate%20to%20the%20Azure%20portal%20and%20create%20an%20Azure%20Function%20Part%204.png)

3. Choose a simple trigger (e.g., HTTP trigger) and deploy a basic function (e.g., "Hello, World").
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Choose%20a%20simple%20trigger%20(e.g.%2C%20HTTP%20trigger)%20and%20deploy%20a%20basic%20function%20Part%201.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Choose%20a%20simple%20trigger%20(e.g.%2C%20HTTP%20trigger)%20and%20deploy%20a%20basic%20function%20Part%202.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Choose%20a%20simple%20trigger%20(e.g.%2C%20HTTP%20trigger)%20and%20deploy%20a%20basic%20function%20Part%203.png)

## 2. Create a Cron Job

GitHub Actions:
1. Create a new GitHub repository (or use an existing one).
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Create%20a%20new%20Github%20repo%20part%201.png)

2. Set up a GitHub Action workflow that runs a script on a schedule (e.g., daily at midnight). You can use a simple script that logs "Scheduled task executed" to the console.
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Github%20actions%20requirements%20txt.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Github%20actions%20yaml%20script.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Github%20actions%20python%20script.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Github%20action%20secrets%20env%20API%20Key.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Github%20Action%20workflow%20that%20runs%20script%20on%20schedule.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/Github%20Action%20workflow%20email%20recieved%20schedule%20task%20executed.png)

## 3. Screenshots of GCP Cloud Scheduler setup

![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/GCP%20Cloud%20Scheduler%20setup%20part%201.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/GCP%20Cloud%20Scheduler%20setup%20part%202.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/GCP%20Cloud%20Scheduler%20setup%20part%203.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/GCP%20Cloud%20Scheduler%20setup%20part%204.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/GCP%20Cloud%20Scheduler%20setup%20part%205.png)
![](https://github.com/adetayoadekunle/HHA504_assignment_serverless/blob/4b048f86b914ea3867765c2162ae4f60637a70a5/GCP%20Cloud%20Scheduler%20setup%20part%206.png)

## 4. Reflect on the use cases for serverless functions in cloud environments. Consider the benefits and limitations of using Functions as a Service (FaaS) in both Azure and GCP.

The use cases for serverless functions in cloud environments are important because they can be triggered by events like a scheduled timer or automated workflows that can deal with sending emails. I think the benefits of using Functions as a Service in both Azure and GCP are that they provide a pay as you go model so you are paying for the function executed which saves costs. The only thing that a person needs to focus on is creating the function and the code. In terms of limitations, there might be huge tasks or workloads that cannot be done efficiently because of the finite resources being used. I also found the design of GCP to be  easier to use because of the design than Azure which looked more difficult to use with its complicated design features.



