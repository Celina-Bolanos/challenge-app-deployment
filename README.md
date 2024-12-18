# challenge-app-deployment

#### Description
This repository corresponds to the last stage of a larger project: immo-eliza. <br>
In this part of the project, the objective is to deploy an already built machine learning model <br>
to make it available for client's usage. <br>

#### Installation
No installation is required. <br>
The prediction application can be found via [this link](https://challenge-app-deployment-b3zjvchs85vva9dhdan85z.streamlit.app/).<br>

#### Usage
1. Visit the online [predictions application](https://challenge-app-deployment-b3zjvchs85vva9dhdan85z.streamlit.app/).
2. Enter the details of the property for which you would like to predict the price. <br>
3. Click on predict.

#### Visuals

#### Contributors
Celina Bolaños <br>

#### Timeline
- Day 1: <br>
    - GitHub repo
    - Project file structure
    - Prepocess part of the pipeline <br><br>

- (Half) Day 2:
    - Complete preprocess functions <br><br>

- Day 3: <br>
    - Initial predictions (without scaling).
    - Modify preprocess functions to OOP. 
    - Scaling integraded into the model. <br><br>

- Day 4:

    - Initial deployment.
    - Fix bugs and app errors.<br><br>

- (Half) Day 5: <br>
    - Final deployment
    - Presentation of the application


#### Personal situation
The most challenging part of this project is -again- the model. Since I had not implemented the scaling of the values <it>inside</it> the model's 
pipeline during the previous stage, it had to be done in this part of the project. Adding a normalization layer was not that difficult after all.<br>
However, the difficulty was that the performance of the model worserned compared to scaling the data before training the model. <br>
Although different methods were tried: adding/removing layers, changing batch sizes, adding batch regularization, the performance did not improve. <br>
Because the model's performance was already insufficient, the fact that it worsened was rather frustrating and disappointing. <br>
