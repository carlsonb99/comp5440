import math
from math import log
import random


class TreeNode(object):

    def __init__(self, isLeaf=False):
        self.attribute = -1
        self.value = None
        self.results = None
        self.tb = None
        self.fb = None
        self.isLeaf = isLeaf
        self.classification = None

    def predict(self, sample):

        # This function predicts the label of given sample
        branch = self

        while branch.isLeaf == False:
            if sample['attributes'][branch.attribute] == branch.value:
                # True Branch
                branch = branch.tb
            else:
                # False Branch
                branch = branch.fb

        # Once you reach the leaf, return the classification label
        return branch.classification

    def printtree(self, tree, indent=''):
        # Is this a leaf node?
        if tree.isLeaf == True:
            print tree.classification + ': ' + str(tree.results)
        else:
            # Print the criteria
            print str(tree.attribute) + ':' + str(tree.value) + '? '

            # Print the branches
            print indent + 'T->',
            self.printtree(tree.tb, indent + '  ')
            print indent + 'F->',
            self.printtree(tree.fb, indent + '  ')


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

        # Randomly choose the attribute subset
        sub_attributes = []
        for attr in attributes:
            if random.random() > .5:
                sub_attributes.append(attr)

        # Display the sub attribute set we will be using
        print sub_attributes

        # Create the tree with the training data
        self.tree_growth(records, sub_attributes)

        # Print the tree (debug)
        self.root.printtree(self.root)

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

    def classify(self, records):
        """
        This function determines the class label to be assigned to a leaf node.
        In most cases, the leaf node is assigned to the class that has the
        majority number of training records

        This function should return a label that is assigned to the node
        """
        max_count = 0
        classification = None

        for key in records.keys():
            if records[key] > max_count:
                max_count = records[key]
                classification = key

        return classification

    def class_label_count(self, records):
        """
        This function provides the count of the class labels for provided sets.
        """
        results = {}

        for record in records:
            r = record['label']
            if r not in results:
                results[r] = 0
            results[r] += 1
        return results

    def entropy(self, records):
        """
        This function finds the entropy of the provided set.
        """
        log2 = lambda x: log(x) / log(2)
        results = self.class_label_count(records)
        ent = 0.0
        for r in results.keys():
            p = float(results[r]) / len(records)
            ent = ent - p * log2(p)
        return ent

    def split_set(self, records, attribute, key):
        """
        This function splits the set into two subsets based on a given key value
        from an attribute. It will only perform a binary split, not multi-way.
        """
        left_subset = []
        right_subset = []

        # If the key value exists in the record, add it to the left subset
        # otherwise, place it in the right subset
        for record in records:
            if record['attributes'][attribute] == key:
                left_subset.append(record)
            else:
                right_subset.append(record)

        return left_subset, right_subset

    def find_best_split(self, records, attributes):
        """
        The find_best_split() function determines which attribute should be
        selected as the test condition for splitting the training records.

        This function should return multiple information:
            attribute selected for splitting
            threshhold value for splitting
            left subset
            right subset
        """

        max_gain = 0.0
        split_attr = None
        split_sets = None

        cur_score = self.entropy(records)

        # Find all of each attribute's values from sub_attributes
        for attr in range(0, len(attributes)):
            attr_values = {}

            # Go through each record and mark possible values
            for record in records:
                attr_values[record['attributes'][attributes[attr]]] = 1

            # Test splits on all of these values
            for value in attr_values.keys():
                left_subset, right_subset = self.split_set(records, attributes[attr], value)

                # Find Information Gain
                p = float(len(left_subset)) / len(records)
                gain = cur_score - p * self.entropy(left_subset) - (1 - p) * self.entropy(right_subset)

                # If there is an information gain and neither set is completely empty,
                # update the values.
                if gain > max_gain and len(left_subset) > 0 and len(right_subset) > 0:
                    max_gain = gain
                    split_attr = (attributes[attr], value)
                    split_sets = (left_subset, right_subset)

        return split_sets, split_attr, max_gain

    def tree_growth(self, records, attributes):
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

        split_sets, split_attr, max_gain = self.find_best_split(records, attributes)

        # If gain is greater than 0, we want to split again, other wise it is a leaf node
        if max_gain > 0:
            true_branch = self.tree_growth(split_sets[0], attributes)
            false_branch = self.tree_growth(split_sets[1], attributes)

            # Create a Tree Node, and set the root of the decision tree to it. (The
            # final self.root will be the tree root)
            self.root = TreeNode()
            self.root.attribute = split_attr[0]
            self.root.value = split_attr[1]
            self.root.tb = true_branch
            self.root.fb = false_branch
            return self.root
        else:
            class_label_counts = self.class_label_count(records)
            node = TreeNode(isLeaf=True)
            node.results = class_label_counts
            node.classification = self.classify(class_label_counts)
            return node
