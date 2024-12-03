# HHA504_assignment_serverless
Deploy a Serverless Function, Create a Cron Job, and Explore Functions as a Service (FaaS)

**Note: I changed the name of the Repository from github-actions-schedule-email to HHA504_assignment_serverless after I posted the screenshots**
## 1. Deploy a Serverless Function

### GCP

1. Access the Google Cloud Console and create a Google Cloud Function.
<img width="1511" alt="Screenshot 2024-11-17 at 11 53 29 AM" src="https://github.com/user-attachments/assets/bc01bc47-e44f-4817-9974-18e7cedec480">
<img width="1501" alt="Screenshot 2024-11-17 at 11 53 52 AM" src="https://github.com/user-attachments/assets/2482741b-608d-471e-b193-676e17b98368">
2. Deploy a similar function with an HTTP trigger in GCP.
<img width="1509" alt="Screenshot 2024-11-17 at 12 02 04 PM" src="https://github.com/user-attachments/assets/bb0ae989-c146-4058-8a4d-1e7b663a89f8">
<img width="1512" alt="Screenshot 2024-11-17 at 12 04 54 PM" src="https://github.com/user-attachments/assets/f6606060-3fa1-45d6-9abf-d3d0c5373b10">
<img width="1512" alt="Screenshot 2024-11-17 at 12 23 23 PM" src="https://github.com/user-attachments/assets/f4c11fd6-cb91-402b-826c-2945cc8d0d25">

### Azure

1. Azure Navigate to the Azure portal and create an Azure Function.
<img width="1511" alt="Screenshot 2024-11-17 at 12 53 05 PM" src="https://github.com/user-attachments/assets/911c0a74-81fa-49d0-b690-7d26f04800de">
<img width="1511" alt="Screenshot 2024-11-17 at 1 50 26 PM" src="https://github.com/user-attachments/assets/1f1c6fec-0707-46f5-a520-4fb1a5813259">
<img width="1488" alt="Screenshot 2024-11-17 at 1 52 51 PM" src="https://github.com/user-attachments/assets/4bb9477e-9f19-4bd0-a6e4-b4968913827a">
<img width="1511" alt="Screenshot 2024-11-17 at 2 37 25 PM" src="https://github.com/user-attachments/assets/14d5bfbf-5d4e-4b30-a396-c9abcb9849b6">
2. Choose a simple trigger (e.g., HTTP trigger) and deploy a basic function (e.g., "Hello, World").
<img width="1506" alt="Screenshot 2024-11-17 at 2 38 34 PM" src="https://github.com/user-attachments/assets/da309ae5-4ce9-4150-9103-9c38d0852b6f">
<img width="1510" alt="Screenshot 2024-11-17 at 2 40 58 PM" src="https://github.com/user-attachments/assets/ab1397a6-5899-4b05-954b-ab1ffd272ffc">
<img width="1512" alt="Screenshot 2024-11-17 at 7 02 04 PM" src="https://github.com/user-attachments/assets/51f112de-0658-4e27-a224-2587f47e02b6">

## 2. Create a Cron Job
GitHub Actions:
1. Create a new GitHub repository (or use an existing one).
<img width="1512" alt="Screenshot 2024-12-02 at 3 33 49 PM" src="https://github.com/user-attachments/assets/dbefc9f7-1dd6-4723-a527-9e4f6469e771">
<img width="1512" alt="Screenshot 2024-12-02 at 3 32 34 PM" src="https://github.com/user-attachments/assets/93b1e4f5-d84c-4061-b651-36da8689add4">
<img width="1494" alt="Screenshot 2024-12-02 at 3 32 50 PM" src="https://github.com/user-attachments/assets/885c9994-3a30-4d99-b668-9ed52c7765ec">

2. Set up a GitHub Action workflow that runs a script on a schedule (e.g., daily at midnight). You can use a simple script that logs "Scheduled task executed" to the console.
<img width="1435" alt="Screenshot 2024-12-02 at 6 58 46 PM" src="https://github.com/user-attachments/assets/b20eca2e-e2db-4cd5-b4fb-8530b7f8cf1d">
<img width="835" alt="Screenshot 2024-12-02 at 3 40 55 PM" src="https://github.com/user-attachments/assets/96ac85b7-2eab-4ff4-84ba-785304cc98aa">
<img width="1504" alt="Screenshot 2024-12-02 at 3 41 28 PM" src="https://github.com/user-attachments/assets/f4fdbc12-72ca-43fa-90e0-b32a21e677ac">
<img width="1031" alt="Screenshot 2024-12-02 at 3 42 47 PM" src="https://github.com/user-attachments/assets/ad117da6-317e-4f3a-bf2d-a01af7fd1149">

## 3. Screenshots of GCP Cloud Scheduler setup
<img width="1100" alt="Screenshot 2024-12-02 at 11 31 32 AM" src="https://github.com/user-attachments/assets/5c29b61f-1c37-44f8-abc0-4c8d8d427bfd">
<img width="1509" alt="Screenshot 2024-12-02 at 3 35 53 PM" src="https://github.com/user-attachments/assets/0f45981c-aef7-400c-a217-38fdcf55565f">
<img width="1506" alt="Screenshot 2024-12-02 at 3 36 01 PM" src="https://github.com/user-attachments/assets/90bb9413-0fce-44c3-b6e5-17ddbbf36d5c">
<img width="1512" alt="Screenshot 2024-12-02 at 3 36 09 PM" src="https://github.com/user-attachments/assets/80f96c4e-ac10-419a-ba84-2e8680acdeed">
<img width="1512" alt="Screenshot 2024-12-02 at 3 36 42 PM" src="https://github.com/user-attachments/assets/cb59c315-907a-424d-8dbc-de72a1cb22f1">
<img width="759" alt="Screenshot 2024-12-02 at 3 36 59 PM" src="https://github.com/user-attachments/assets/304c17e9-83a8-4e77-8068-c5e02100d418">

## 4. Reflect on the use cases for serverless functions in cloud environments. Consider the benefits and limitations of using Functions as a Service (FaaS) in both Azure and GCP.
The use cases for serverless functions in cloud environments are important because they can be triggered by events like a scheduled timer or automated workflows that can deal with sending emails. I think the benefits of using Functions as a Service in both Azure and GCP are that they provide a pay as you go model so you are paying for the function executed which saves costs. The only thing that a person needs to focus on is creating the function and the code. In terms of limitations, there might be huge tasks or workloads that cannot get done efficiently because of the limit of resources being used. I also found the design of GCP to be  easier to use because of the design than Azure which looked more difficult complicated to use with its features.



