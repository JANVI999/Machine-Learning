# Build and evaluate the machine learning model to decide suitability of a TV/OTT series for children’s entertainment.
The buzz of OTT platforms like Amazon, Hotstar, Netflix is very high among the new generation
as it provides various entertainment options with various genre (like action, romantic, comedy,
thriller) but it also has its disadvantages like the explicit content , cruel content which have
actually impacted the youth, children .
Children between the ages of 8-15 like these apps more than anyone. The reason is the OTT
platforms serve unlimited entertainment from various genres that are also children-friendly. This
content entertains children as well as educates them.
Our model has been trained in such a way which solves this problem , (by adding features like
ratings , recommendations etc we have perform various evaluation parameters on it like
Entropy, Gini index, accuracy, confusion matrix ,etc ) which predicts which movies are
watchable for children.


The features which were used in our model were
1.) Ratings :- Based on the Age limit Ratings were assigned to a movie .
(eg. 12+, 15+) so that an appropriate aged children to watch that series or
movie.
2.) Genre :- Genre of a movie like Action, comedy, Romantic , Thriller were
assigned to the movie. To avoid unnecessary drama, over action scenes ,
explicit content etc.
3. ) Recommendation :- An Age limit was set Like - 13+ were recommended
no (means 13+ age movies not watchable for children, below 13+ movies ,
series can be watched by children.)


TESTING AND EVALUATION OF MODEL

1)  Entropy :- We used Entropy to measures the impurity or uncertainty in a
group of observations. It determines how a decision tree chooses to split
data. It relates to randomness in data. In our model while implementing
Decision tree entropy was default selection.
2)  Gini Index :- It was used to determine how well a Decision Tree was split,
our accuracy for entropy and gini index was same which indicated that
Entropy and gini index of our model is same with depth 4.
3)  Accuracy Score :- It was calculated to determine the accuracy of our
Model . Which is 98.360 %.
4) Confusion Matrics :- It was calculated for better idea of our classification
model. Confusion matrix for our model is :-
5) TP (True positive -20), FN (False negative – 1), FP (False positive – 0)
TN (True negative – 40 ).

OUTCOME

1) The purpose of Training the model was to classify the movies/series which
can be watched by children based on various factors like Features,
Evaluation parameters, etc.
2) So to avoid and reduce the side effects of the OTT movies/series.
3) And The main Outcome of our model is that movies till the Ratings of Age
group 13+ can be watched by the children .
4) And Genre(Crime) is not recommended to watch for children.
5) And the accuracy of the model is 98%.

Conclusion

1) We have successfully built and evaluated a model to determine which
movies/series are watchable for children .
2) Importing necessary libraries is very important to train a model. Like numpy
library was used to support large matrix & multi-dimensional data.
Matplotlib library was used for plotting numerical data .
3) Selection of appropriate or relevant features and Evaluation parameters is
an important task while creating a model using decision tree. We used
(Ratings, Genre, Recommendations ) as features , and ( Entropy, Gini index
, accuracy score, confusion matrix ) as evaluation parameters.
4) Decision Tree was used to create a model that predicts the value of a
target variable by learning simple decision rules inferred from the features.
5) As accuracy of our model is 98% which means the model which we have
built is good.
