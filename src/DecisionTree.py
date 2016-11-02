class TreeNode(object):
    def __init__(self, isLeaf=False):
        # Your code here

    def predict(self, sample):
        """
        This function predicts the label of given sample
        """
        # Your code here

class DecisionTree(object):
    """
    Class of the Decision Tree
    """
    def __init__(self):
        self.root = None

    def train(self, records, attributes):
        """
        This function trains the model with training records "records" and
        attribute set "attributes", the format of the data is as follows:
            records: training records, each record contains following fields:
                label - the lable of this record
                attributes - a list of attribute values
            attributes: a list of attribute indices that you can use for
                        building the tree
        Typical data will look like:
            records: [
                        {
                            "label":"p",
                            "attributes":['p','x','y',...]
                        },
                        {
                            "label":"e",
                            "attributes":['b','y','y',...]
                        },
                        ...]
            attributes: [0, 2, 5, 7,...]
        """

    def predict(self, sample):
        """
        This function predict the label for new sample by calling the predict
        function of the root node
        """
        return self.root.predict(sample)

    # def stopping_cond(self, records, attributes):
        """
        The stopping_cond() function is used to terminate the tree-growing
        process by testing whether all the records have either the same class
        label or the same attribute values.

        This function should return True/False to indicate whether the stopping
        criterion is met
        """

    # def classify(self, records):
        """
        This function determines the class label to be assigned to a leaf node.
        In most cases, the leaf node is assigned to the class that has the
        majority number of training records

        This function should return a label that is assigned to the node
        """

    # def find_best_split(self, records, attributes):
        """
        The find_best_split() function determines which attribute should be
        selected as the test condition for splitting the trainig records.

        This function should return multiple information:
            attribute selected for splitting
            threshhold value for splitting
            left subset
            right subset
        """

    # def tree_growth(self, records, attributes):
        """
        This function grows the Decision Tree recursively until the stopping
        criterion is met. Please see textbook p164 for more details

        This function should return a TreeNode
        """
        # Your code here
        # Hint-1: Test whether the stopping criterion has been met by calling function stopping_cond()
        # Hint-2: If the stopping criterion is met, you may need to create a leaf node
        # Hint-3: If the stopping criterion is not met, you may need to create a
        #         TreeNode, then split the records into two parts and build a
        #         child node for each part of the subset
