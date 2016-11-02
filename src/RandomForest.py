class RandomForest(object):
    """
    Class of the Random Forest
    """
    def __init__(self, tree_num):
        self.tree_num = tree_num
        self.forest = []

    def train(self, records, attributes):
        """
        This function will train the random forest, the basic idea of training a
        Random Forest is as follows:
        1. Draw n bootstrap samples using bootstrap() function
        2. For each of the bootstrap samples, grow a tree with a subset of
            original attributes, which is of size m (m << # of total attributes)
        """
        # Your code here
        pass

    def predict(self, sample):
        """
        The predict function predicts the label for new data by aggregating the
        predictions of each tree.

        This function should return the predicted label
        """
        # Your code here
        pass

    # def bootstrap(self, records):
        """
        This function bootstrap will return a set of records, which has the same
        size with the original records but with replacement.
        """
