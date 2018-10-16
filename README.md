### Intro

In this small demo, I assumed two basic requirments:

1. The user needs to fetch results in an existed database, which is predicted by the ML model with offered data in advance.

2. The user needs to get fresh results in real time by providing new input data.

### Usage

### Proposed future imrpovements:

- Increasing the input forms of data.

  - The input should can be data stream. For example, if the ML model is for image processing or audio signal processing, the input data can be video stream or signal stream.

  - The input should can be the URL of a database. The backend should also be able to retrive data from an URL and train or test model on it.

- Accelarating by adding cache architetcure.

  This improvement aims at decreasing the time of real-time prediction (the second requirment above). Sometimes, the user has to wait a long time when they try to get a result from offered data if the ML model is so complex that costs much time.

  To improve the performance, we can add every predicted result to the database when it is from new offered data. Thus every time the user requests for predicting, we seek for the offered data in the database first and run the ML model only if there is no corresponding answer.
