# miniproject-1-iris-dataset-Priyadharshini-Sakthivel
miniproject-1-iris-dataset-Priyadharshini-Sakthivel created by GitHub Classroom
The workflow consists of 7 steps from which the first 3 are more theoretical-oriented:

Formulate the problem

Describe the dataset

Selecting the multiple layer perceptron model

Build the model

Train the model

Test the model

Derive the accuracy
1. Formulate the problem:

Process and transform the iris flowers dataset to create a prediction model. This model must predict in which of the three specific flower species each flower. 

2. Data description:

Iris is a genus of flowering plants species. It takes its name from the goddess of rainbow in Greek mythology.A perceptron finds this linear discriminant function:
Discriminant function h(x): we use training data to learn a function h(x) that maps inputs x directly onto a class label y.
The Iris dataset has three classes where one class is linearly separable from the other 2; the latter two are not linearly separable from each other. Each class refers to a type of iris plant and contains 50 instances.

3. Visualization

The next step is to visualize the dataset to capture the relationships between the features and the associated classes. We have more than two features that involve relationships between them (i.e., multivariate data). We use bivariate visualisations for every two features to capture all of their relationships.

Before diving into preprocessing we have to split our data into training (80%) and test data (20%). We will use the training data (contain the classes for our iris species) to learn the model; and test data (contain only the features, without the classes) to measure the accuracy.

LabelEncoder introduced a new problem (noise) to our dataset: added numerical relationships in the features that now have become ordinal variables. That means that the model thinks that Iris-versicolor(1) is higher than Iris-setosa(0) and Iris-setosa(0) is smaller than Iris-virginica(2). To solve that we would take a three dimensional vector, rather than an one dimensional vector with 3 values ([0,1,2]). Thus, setosa would be [1,0,0], versicolor would be [0,1,0] and virginica woul dbe [0,0,1].

We can use a plot to see what was the effect of feature scaling to our data values. It rescaled the features such that they have a mean of zero and a standard deviation of one.

4. Build the model:(Multiple layer Perceptron)

A network consists of more than one layer of output nodes; that means, there is at least one hidden layer with more than oone neuroons that passes the inputs to the output layer (simplest model). The more layers you add, the more complex the model becomes, meaning that the more accurate it can become.

MLP in Species Prediction

We have 4 features as input units and 3 classes as output units. The size of the hidden layer should be the mean of these 2 so around 4 should be adequate. We add instead 10 nodes in the hidden layer hidden_layer_sizes(10) making it more complex. We shouldn’t need more than one layers as we have a really small data set (7cols, 600rows). 

solver = sgd. Adam solver tends to work better when large data sets are available, learning_rate_init=0.01: controls how much to update the weights to the right direction given the residual error, max_iter=500 : maximum number of epochs (=how many times each data point will be used until the solver convergence). 

5 : Train the model

Training = Minimize the loss function (categorical cross entropy here because oof the nature of the output)

6: Test the model

Using the appropriate metrics to evaluate your model & prevent Accuracy Paradox.
