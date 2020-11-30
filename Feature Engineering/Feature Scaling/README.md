## Feature Selection Techniques

### Top reasons to use feature selection are:

__1. It enables the machine learning algorithm to train faster.__
__2.  reduces the complexity of a model and makes it easier to interpret.__
__3. improves the accuracy of a model if the right subset is chosen.__
__4.  reduces overfitting.__

- Filter Methods
1. Pearson’s Correlation: It is used as a measure for quantifying linear dependence between two continuous variables X and Y. Its value varies from -1 to +1.
2. LDA: Linear discriminant analysis is used to find a linear combination of features that characterizes or separates two or more classes (or levels) of a categorical variable.
3. ANOVA: ANOVA stands for Analysis of variance. It is similar to LDA except for the fact that it is operated using one or more categorical independent features and one continuous dependent feature. It provides a statistical test of whether the means of several groups are equal or not.
4. Chi-Square: It is a is a statistical test applied to the groups of categorical features to evaluate the likelihood of correlation or association between them using their frequency distribution.

- Wrapper Methods
Some common examples of wrapper methods are forward feature selection, backward feature elimination, recursive feature elimination, etc.

1. Forward Selection: Forward selection is an iterative method in which we start with having no feature in the model. In each iteration, we keep adding the feature which best improves our model till an addition of a new variable does not improve the performance of the model.
2. Backward Elimination: In backward elimination, we start with all the features and removes the least significant feature at each iteration which improves the performance of the model. We repeat this until no improvement is observed on removal of features.
3. Recursive Feature elimination: It is a greedy optimization algorithm which aims to find the best performing feature subset. It repeatedly creates models and keeps aside the best or the worst performing feature at each iteration. It constructs the next model with the left features until all the features are exhausted. It then ranks the features based on the order of their elimination.

- Correlation Matrix with Heatmap
- Feature Importance
- Univariate Selection
