class LP_Node:

    def __init__(self, data=None):
        self.data = data  # data , initialized as None to allow for creation of head node
        self.play_history = None  # prev
        self.next_song = None  # next

    def __str__(self):  # allows for printing of object; format is data: x previous_song: y next_song: z
        return f"data: {self.data}, previous song: {self.play_history}, next song: {self.next_song}"

class LP_List:

    def __init__(self):
        self.head = LP_Node()
        self.length = 0

    def append(self, data):
        """
        :param data: Takes in data, could be any object we are looking to store
        :return: None, increments linked list with a new item
        """

        insertion_node = LP_Node(data)  # Node to be inserted into linked list

        temp = self.head  # set temp value to be the head ; this handles the corner case if no previous song played

        while temp.next_song is not None:  # while the next song is still a defined instance

            temp = temp.next_song  # iterate through the songs

        insertion_node.play_history = temp  # tracks the previously played songs

        temp.next_song = insertion_node  # replaces None with the insertion node

        self.length += 1

    def display(self):
        """
        :return: Returns a list of elements, creates a new list array to print
        """

        elements = []  # will contain the linked list data in one array then print it

        temp = self.head  # set comparison value to the head of the list

        while temp.next_song is not None:  # while the next pointer is towards an object

            temp = temp.next_song  # iterate to the next song

            elements.append(temp.data)  # append data to the elements list

        print(elements)

    def is_empty(self):
        """
        :return: Logical Condition. Returns True or False
        """
        return self.head.next_song is None  # Logical Condition: returns true if the head points to None

    def getprev(self):  # Gets previously played song, len(LP_List) - 2, Not implemented in my_player, incorrect output
        """
        :return: gets item at idex len(list) - 2, not the final object itself but the previous pointer of it
        """
        temp = self.head # assign temp

        if temp is not None:  # if compare value is not None

            while temp.next_song is not None:  # if the pointer is towards a new object

                temp = temp.next_song  # increment temp

            if temp.next_song is None:  # if next pointer is None : same as saying if at the end of the list

                if temp.data is not None:  # if the data exists
                    return temp.play_history.data  # returns song information of previous node
            else:
                return 'Error No LP_List item present'

    def getlast(self):
        """
        :return: Returns final item in linked list
        """

        temp = self.head  # set comparison value

        while temp.next_song is not None:  # if pointer is not None
            temp = temp.next_song  # increment temp

        if temp.next_song is None:  # if point is towards None , same as arriving at
            return temp.data


def main():  # test code for linked list functionality : should not import

    my_list = LP_List()
    my_list.append(1)

    print(my_list.getprev())
    print(my_list.getPREV(),'test 2')
    my_list.append('123')
    my_list.append('322')
    previous_song = my_list.getprev()
    print("Previous song played:", previous_song)
    my_list.append('1235')
    my_list.append('3225')
    print(my_list.getprev())

if __name__ == "__main__":
    main()





