**--Overview--**                
This project is a simple Crop Management System implemented in Python. The system allows users to manage and track crop data, including crop names, soil types, diseases, and observation dates. It provides functionalities to add crop data, recommend crops based on soil type, and list all recorded crops.

**Features**                
Data Management: Users can add crop data, specifying the crop name, soil type, disease (if any), and observation date. The system stores this information in a JSON file, enabling easy data management and retrieval.

Crop Recommendations: Users can get crop recommendations based on the soil type they specify. The system filters and displays crops that are suitable for the given soil type.

Data Retrieval: Users can list all crops stored in the database along with their details, including soil type, disease, and observation date.

Persistent Storage: Crop data is saved and loaded from a JSON file located within the CODE directory. The system ensures that the file is initialized if it does not exist, and data is preserved across different sessions.

**Technologies Used**                
Programming Language: Python                  
Data Storage: JSON
