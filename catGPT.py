
"""
A class represents a trie

I have referred to the implementation of Trie class shown in the recording
Lecture11 Trie
"""
class CatsTrie:
    def __init__(self, sentences):
        """
        Create a CatsTrie object based on the given sentences

        I have referred to the implementation of init method shown in the 
        recording Lecture11 Trie.

        Approach Description:
        In the trie, each node will store a list of 27 characters where 26 of 
        them are alphabets from a to z and 1 of them is the terminal node. The
        terminal node is always at the index 0 of the list. Each node will 
        also store additional data which are the highest frequency among all 
        the child nodes, the reference to the child/next node that has the 
        highest frequency and the lowest lexicographical order, and the index 
        of the corresponding sentence. These additional data are stored in 
        order to retrieve the complete sentence in autoComplete method  more
        efficiently (see the approach description in autoComplete method for 
        more details).

        At the beginning, the trie only have a root node which is the starting
        point whenever we insert a new sentence. Then, we start inserting each
        sentence in the given sentences into the trie one by one.

        When inserting a sentence into the trie, it will iterate over the
        characters of the sentence one by one. For each character, it will 
        check if a child node that corresponds to the character exists in the 
        current node of the trie, i.e. child node is not None. If it does not 
        exist, we will create a new node and add it to the current node as the
        child node. Then, we will continue to the next character until we have
        gone through all the characters of the sentence. In the terminal node, 
        the highest frequency of the sentence is increment by 1 and the index
        of the corresponding sentence is stored. 

        I have used recursion to insert the sentence into the trie because we
        need to traverse back to the root and update the additional data stored
        in the nodes related to the sentence if the sentence now has the 
        highest frequency and lowest lexicographical order among all the other
        sentences inserted before it. Using the recursion method is more easier
        to implement in my opinion. 

        When traversing back to the root, we will start with the node that
        corresponds to the last character of the sentence. If the sentence now
        has the highest frequency and lowest lexicographical order, we will 
        update the additional data in the node that corresponds to the last
        character. The node will now store the frequency of the sentence, 
        the reference to the terminal node (which is 0), and the index of the 
        sentence. Then, we will continue update the additional data in the 
        other nodes as we traverse back towards to the root node. 

        :Input:
            self: a reference to the CatsTrie object
            sentences: a list of strings where the list cannot be empty and 
                       each string has at least one character from a to z

        :Output/Return: - 

        :Time complexity: O(NM) where N is the number of sentences and M is
                          the number of characters in the longest sentence
        :Aux space complexity: O(N) because there are N number of sentences
                               and N nodes where each node has O(1) aux space
        """
        self.sentences = sentences
        
        # Root node of the trie
        self.root = Node()

        # Insert each sentence into the trie
        i = 0
        for sentence in sentences:      # O(N)
            self.insert(sentence, i)    # O(M)
            i += 1
    
    def insert(self, sentence, sentence_index):
        """
        Insert a sentence into the trie recursively
        
        I have referred to the implementation of insert_recur method shown in 
        the recording Lecture11 Trie.

        :Input:
            self: a reference to the CatsTrie object
            sentence: a string that is a sentence in the sentences
            sentence_index: an integer that represents the index of the 
                            sentence in the sentences

        :Output/Return: -

        :Time complexity: O(M)
        :Aux space complexity: O(N) because insert_aux has O(N) aux space
        """
        # begin from the root
        current = self.root

        # insert this sentence into the trie
        # O(M) time
        self.insert_aux(sentence, sentence_index, current, 0)

        index = ord(sentence[0]) - 97 + 1
        
        # if this sentence has higher frequency, 
        # update the data stored in the root
        if self.root.link[index].highest_freq > self.root.highest_freq:
            self.root.highest_freq = self.root.link[index].highest_freq
            self.root.next_node_highest_freq = index
            self.root.sentence_index = sentence_index
        
        # if this sentence has the same frequency,
        # this means that there is another sentence with the same frequency
        # both has the highest frequency among all other sentences inserted

        # check if this sentence has a lower lexicographical order
        elif self.root.link[index].highest_freq == self.root.highest_freq:

            # if this sentence has a lower lexicographical order,
            # update the data stored in the root
            if self.root.next_node_highest_freq > index:
                self.root.next_node_highest_freq = index
                self.root.sentence_index = sentence_index

            # if they have the same order,
            # make sure that the sentence index stored in the root is the same
            # as the one stored in the next node
            elif self.root.next_node_highest_freq == index:
                 self.root.sentence_index = self.root.link[index].sentence_index

    def insert_aux(self, sentence, sentence_index, current, current_index):
        """
        Insert a sentence into the trie recursively

        I have referred to the implementation of insert_recur_aux method shown 
        in the recording Lecture11 Trie.

        :Input:
            self: a reference to the CatsTrie object
            sentence: a string that is a sentence in the sentences
            sentence_index: an integer that represents the index of the 
                            sentence in the sentences
            current: a Node object that refers to the current node
            current_index: an integer that refers to the current character in 
                           the sentence

        :Output/Return: - 

        :Time complexity: O(M)
        :Aux space complexity: O(N) because it iterates through the characters
                               of the sentence one by one until it reaches the 
                               base case
        """
        # base case 
        # after going through all the characters in the sentence,
        # now at the terminal
        if current_index == len(sentence):

            # if path already exist
            if current.link[0] is not None:
                # link to the terminal node
                current = current.link[0]

            # if path doesn't exist
            else:
                # create a new node
                current.link[0] = Node()
                # link to the terminal node
                current = current.link[0]

            # frequency of the sentence appears in the trie increase by 1
            current.highest_freq += 1

            current.sentence_index = sentence_index

            return
        
        # recursive step
        # insert the characters of the sentence into the trie one by one
        else:
            index = ord(sentence[current_index]) - 97 + 1

            # if path already exist
            if current.link[index] is not None:
                current = current.link[index]

            # if path doesn't exist
            else:
                # create a new node
                current.link[index] = Node()
                current = current.link[index]

            # insert the next character of the sentence into the trie
            self.insert_aux(sentence, sentence_index, current, current_index+1)

            # traverse back from last node (the last character) to the root
            
            # compare the terminal node with the current node
            if current_index == len(sentence) - 1:

                # if the sentence has higher frequency than the one stored in 
                # current node,
                # update the data stored in current node
                if current.link[0].highest_freq > current.highest_freq:
                    current.highest_freq = current.link[0].highest_freq
                    current.next_node_highest_freq = 0
                    current.sentence_index = sentence_index

                # if the sentence has the same frequency as the one stored in 
                # current node,
                # update the data stored in current node
                if current.link[0].highest_freq == current.highest_freq:
                    current.next_node_highest_freq = 0
                    current.sentence_index = sentence_index
            
            # compare the current node with the next node
            # until reach the root 
            else:
                index = ord(sentence[current_index + 1]) - 97 + 1 

                # if the sentence has higher frequency than the one stored in 
                # next node,
                # update the data stored in current node
                if current.link[index].highest_freq > current.highest_freq:
                    current.highest_freq = current.link[index].highest_freq
                    current.next_node_highest_freq = index
                    current.sentence_index = sentence_index
                
                # if the sentence has the same frequency as the one stored in 
                # next node,
                # this means that both sentences have the highest frequency 
                # among all other sentences inserted

                # check if the sentence has a lower lexicographical order than
                # the one stored in next node
                elif current.link[index].highest_freq == current.highest_freq:

                    # if it has a lower lexicographical order, 
                    # update the data stored in current node
                    if current.next_node_highest_freq > index:
                        current.next_node_highest_freq = index
                        current.sentence_index = sentence_index

                    # if they have the same lexicographical order,
                    # make sure that the sentence index stored in current node
                    # is the same as the one stored in the next node
                    elif current.next_node_highest_freq == index:
                        current.sentence_index = \
                            current.link[index].sentence_index

    def autoComplete(self, prompt):
        """
        Return a complete sentence based on the given incomplete sentence, that
        has the highest frequency and lowest lexicographical order using the
        trie

        Approach Description:
        Each node stores the next node that has the highest frequency and 
        lowest lexicographical order and the index that refers the corresponding
        sentence. For example, we have the sentences ["ac", "ab"]. The root 
        will store the reference to the next node "a". The node "a" will store
        the reference to the next node "b". This is because "ac" and "ab" has
        the same frequency but "ab" has lower lexicographical order. Hence, 
        it will store the reference to the next node "b" instead of "c". The
        node "b" will store the reference to the terminal node. 
        
        Using this approach, we can easily retrieve the complete sentence
        with the highest frequency and lowest lexicographical order. We just
        need to start from the root and get the next node until we reach a 
        terminal node.

        However, we would need to perform string concatenation to retrieve the
        complete sentence, which is extremely inefficient. 
        
        To further improve this, we can store the index of sentence that has 
        the highest frequency and lowest lexicographical order for a 
        prefix in each node. 

        By doing so, we can easily retrieve the complete sentence using the 
        index stored. For example, the root and the node "a" will store the 
        index 1 because "ab" has lower lexicographical order than "ac". If the
        prompt is "a", we will go from the root to the node "a" to check if 
        the string "a" exists in our trie. If the string exist, we will 
        retrieve the complete sentence at index 1 which is "ab".

        I have chosen to store the index of the sentence rather than the 
        sentence itself into the the nodes because string needs O(n) space
        according to https://medium.datadriveninvestor.com/understanding-big-o-space-complexity-6826478e5a9f 

        :Input:
            self: a reference to the CatsTrie object
            prompt: a string with characters from a to z, representing an 
                    incomplete sentence

        :Output/Return: a string that represents the complete sentence

        :Time complexity: O(|X| + |Y|) where X is the length of the prompt and
                          Y is the length of the most frequent sentence that
                          begins with the prompt
        :Aux space complexity: O(1)
        """
        # begin from root 
        current = self.root

        # check if the incomplete sentence exists
        # O(X) time
        for char in prompt:
            index = ord(char) - 97 + 1

            if current.link[index] == None:
                return None
            
            current = current.link[index]

        # if the incomplete sentence exists
        # return the complete sentence 
        # O(Y) time
        return self.sentences[current.sentence_index]
        
"""
A class represents a node in a trie

I have referred to the implementation of Node class shown in the recording
Lecture11 Trie
"""
class Node:
    def __init__(self):
        """
        Create a Node object

        :Input: 
            self: a reference to the Node object

        :Output/Return: -

        :Time complexity: O(1)
        :Aux space complexity: O(1)
        """
        # A list that stores the child nodes
        # 26 characters from a to z + terminal node $
        self.link = [None] * 27

        # Highest frequency among all the child nodes
        self.highest_freq = 0

        # Reference to the child node that has the highest frequency and lowest
        # lexicographical order
        self.next_node_highest_freq = None

        # Reference to the index of the sentence with the highest frequency and
        # lowest lexicographical order
        self.sentence_index = None

    def __str__(self):
        """
        Display the data stored in the Node object

        :Input: 
            self: a reference to the Node object

        :Output/Return: a string containing the highest frequency among the 
                        child nodes, the reference to the child node that has 
                        the highest frequency and the index of the most 
                        frequent sentence

        :Time complexity: O(1)
        :Aux space complexity: O(1)
        """
        return_str = \
            "Highest freq: " + str(self.highest_freq) + "\n" + \
            "Next node with highest freq: " + str(self.next_node_highest_freq) + \
            "Sentence index: " + str(self.sentence_index)

        return return_str
